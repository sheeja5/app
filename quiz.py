import streamlit as st
import random
from typing import List, Dict

# --- Page Configuration ---
st.set_page_config(page_title="India Law Enforcement — Learn & Quiz", layout="centered")

# --- Constants & Data ---
LESSONS: Dict[str, str] = {
    "Indian Police System": (
        "Overview of the organisation of law enforcement in India: the role of the Central Government, State Police, and paramilitary forces. "
        "State Police are primary law enforcement agencies; the Union has apex bodies like the Central Bureau of Investigation (CBI), National Investigation Agency (NIA), and paramilitary forces for specific roles."
    ),
    "Police Ranks & Structure": (
        "Ranks range from Constable -> Head Constable -> Sub-Inspector -> Inspector -> Superintendent of Police (SP) -> Deputy Inspector General -> Inspector General etc. "
        "Leadership, organisational structure, and distribution of responsibilities differ between states and central forces."
    ),
    "Rights of Citizens & Police Duties": (
        "Important: citizens have constitutional rights such as the right to life and personal liberty (Article 21). Police duties include protecting life and property, preventing and investigating offences, and maintaining public order. "
        "Complaints against police are handled by state mechanisms — recent legal frameworks emphasize accountability and transparency."
    ),
    "Investigation Basics": (
        "Investigation stages: FIR, preliminary inquiry, evidence collection, arrest (with safeguards), charge-sheet, and court proceedings. "
        "Must follow procedure under the Criminal Procedure Code (CrPC); forensic and digital evidence are increasingly important."
    ),
    "Cybercrime & Modern Challenges": (
        "Cybercrime is handled under the Information Technology Act and IPC sections on fraud, hacking, identity theft, and harassment. "
        "Specialised cyber cells and training are critical as crimes shift online."
    ),
}

QUESTION_BANK: List[Dict] = [
    {"category": "Indian Police System", "question": "Which body is primarily responsible for criminal investigation in states of India?", "options": ["Central Bureau of Investigation (CBI)", "State Police", "National Investigation Agency (NIA)", "Central Reserve Police Force (CRPF)"], "answer": "State Police", "explanation": "Most day-to-day criminal investigations within a state's territorial limits are handled by the State Police."},
    {"category": "Police Ranks & Structure", "question": "Which rank is typically senior to Inspector in the police hierarchy?", "options": ["Head Constable", "Sub-Inspector", "Inspector", "Superintendent of Police"], "answer": "Superintendent of Police", "explanation": "A Superintendent of Police (SP) is senior and usually heads a district police force."},
    {"category": "Rights of Citizens & Police Duties", "question": "Which article guarantees the right to life and personal liberty?", "options": ["Article 19", "Article 21", "Article 14", "Article 25"], "answer": "Article 21", "explanation": "Article 21 guarantees protection of life and personal liberty except according to procedure established by law."},
    {"category": "Investigation Basics", "question": "What is the first step usually taken by police when a cognizable offence is reported?", "options": ["Charge-sheet", "Filing FIR", "Trial in court", "Forensic analysis"], "answer": "Filing FIR", "explanation": "For cognizable offences, police file a First Information Report (FIR) before investigation."},
    {"category": "Cybercrime & Modern Challenges", "question": "Which act provides many legal provisions to deal with cyber offences?", "options": ["Indian Penal Code", "Information Technology Act", "Evidence Act", "Contract Act"], "answer": "Information Technology Act", "explanation": "The Information Technology Act, 2000, provides a legal framework for cybercrime."},
]

# --- Session State Initialization ---
def initialize_session_state():
    """Initializes all necessary session state variables."""
    if 'questions' not in st.session_state:
        st.session_state.questions = QUESTION_BANK.copy()
    if 'quiz_qs' not in st.session_state:
        st.session_state.quiz_qs = []
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'incorrect' not in st.session_state:
        st.session_state.incorrect = []
    # --- FIX: Added state to track if an answer has been submitted ---
    if 'answer_submitted' not in st.session_state:
        st.session_state.answer_submitted = False
    if 'user_choice' not in st.session_state:
        st.session_state.user_choice = None

initialize_session_state()

# --- UI: Main App ---
st.title("🇮🇳 Learn & Quiz: Law Enforcement in India")
st.markdown("Learn the basics, then test your knowledge with quick quizzes.")

# --- UI: Sidebar ---
with st.sidebar:
    st.header("Controls & Modes")
    mode = st.selectbox("Mode", ["Study Mode", "Quiz Mode", "Add Question", "Review Incorrect"])
    st.write("---")
    st.header("Quick Topics")
    topic = st.radio("Pick a topic to read", list(LESSONS.keys()))
    st.write("\n")
    if st.button("Reset Progress"):
        # --- FIX: Clear all session state keys for a full reset ---
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()


# --- Logic for Study Mode ---
if mode == "Study Mode":
    st.subheader(topic)
    st.write(LESSONS[topic])
    st.info("Tip: Switch to Quiz Mode to test what you learned.")

# --- Helper Function for Quiz ---
def get_questions_for_category(category: str = None):
    if category is None or category == "All":
        return st.session_state.questions
    return [q for q in st.session_state.questions if q['category'] == category]

# --- Logic for Quiz Mode (REFACTORED) ---
if mode == "Quiz Mode":
    st.subheader("Quick Quiz — Choose category")

    # If a quiz is already in progress, don't show the setup
    if not st.session_state.quiz_qs:
        categories = ["All"] + sorted({q['category'] for q in st.session_state.questions})
        chosen_cat = st.selectbox("Category", categories, key="quiz_category_select")
        available_count = len(get_questions_for_category(chosen_cat))

        if available_count > 0:
            num_q = st.slider("Number of questions", min_value=1, max_value=available_count, value=min(5, available_count))
        else:
            st.warning("No questions available for this category yet. Add questions in 'Add Question' or choose another category.")
            num_q = 0

        if st.button("Start Quiz", disabled=(available_count == 0)):
            pool = get_questions_for_category(chosen_cat)
            st.session_state.quiz_qs = random.sample(pool, k=num_q)
            st.session_state.current_index = 0
            st.session_state.score = 0
            st.session_state.incorrect = []
            st.session_state.answer_submitted = False
            st.session_state.user_choice = None
            st.rerun() # Rerun to start the quiz immediately

    # --- This block runs if a quiz has been started ---
    if st.session_state.quiz_qs:
        # Check if quiz is finished
        if st.session_state.current_index >= len(st.session_state.quiz_qs):
            st.balloons()
            st.success(f"**Quiz finished! Your Score: {st.session_state.score}/{len(st.session_state.quiz_qs)}**")
            if st.session_state.incorrect:
                st.warning("You can review your incorrect answers from the sidebar in 'Review Incorrect' mode.")
            if st.button("Take Another Quiz"):
                # Reset for a new quiz
                st.session_state.quiz_qs = []
                st.rerun()
        else:
            # Display the current question
            q = st.session_state.quiz_qs[st.session_state.current_index]
            st.write(f"**Question {st.session_state.current_index + 1} of {len(st.session_state.quiz_qs)}**")
            st.write(f"_{q['category']}_")
            st.markdown(f"### {q['question']}")

            # --- FIX: State-driven UI ---
            # If answer not submitted, show options. Otherwise, show feedback.
            if not st.session_state.answer_submitted:
                options = q['options']
                user_choice = st.radio("Choose an answer:", options, key=f"opt_{st.session_state.current_index}")

                if st.button("Submit Answer"):
                    st.session_state.user_choice = user_choice
                    st.session_state.answer_submitted = True
                    if user_choice == q['answer']:
                        st.session_state.score += 1
                    else:
                        st.session_state.incorrect.append(q)
                    st.rerun()
            else:
                # Show feedback after submission
                if st.session_state.user_choice == q['answer']:
                    st.success(f"Correct! ✅ The answer is **{q['answer']}**.")
                else:
                    st.error(f"Incorrect. You chose **{st.session_state.user_choice}**. The correct answer was **{q['answer']}**.")

                st.info(f"**Explanation:** {q.get('explanation', 'No explanation provided.')}")

                if st.button("Next Question"):
                    st.session_state.current_index += 1
                    st.session_state.answer_submitted = False
                    st.session_state.user_choice = None
                    st.rerun()


# --- Logic for Review Incorrect ---
if mode == "Review Incorrect":
    st.subheader("Review: Incorrect answers")
    if not st.session_state.get('incorrect'):
        st.info("No incorrect answers this session. Well done!")
    else:
        for i, q in enumerate(st.session_state.incorrect, start=1):
            with st.container():
                st.write(f"**{i}. {q['question']}**")
                st.error(f"**Correct Answer:** {q['answer']}")
                st.write(f"**Explanation:** {q.get('explanation', '')}")
                st.write("---")

# --- Logic for Add Question ---
if mode == "Add Question":
    st.subheader("Add your own question")
    with st.form("add_q_form"):
        # Use a set to get unique categories and then sort them
        current_categories = sorted({q['category'] for q in st.session_state.questions})
        cat_options = current_categories + ["Create a new category..."]
        cat = st.selectbox("Category", cat_options)

        if cat == "Create a new category...":
            new_cat = st.text_input("Enter new category name:")
        else:
            new_cat = cat

        question_text = st.text_area("Question Text")
        opts = [st.text_input(f"Option {i+1} (Enter the correct answer in this first box)") for i in range(4)]
        explanation = st.text_area("Explanation (optional)")

        submitted = st.form_submit_button("Add Question to Bank")
        if submitted:
            # The correct answer is always the first option
            correct_answer = opts[0].strip()
            # Filter out empty options and shuffle them for the quiz
            valid_opts = [o.strip() for o in opts if o.strip()]
            
            if not new_cat.strip() or not question_text.strip() or len(valid_opts) < 2 or not correct_answer:
                st.error("Please provide a category, a question, and at least two options (with the correct answer in the first box).")
            else:
                random.shuffle(valid_opts) # Shuffle options before saving
                new_q = {
                    'category': new_cat.strip(),
                    'question': question_text.strip(),
                    'options': valid_opts,
                    'answer': correct_answer,
                    'explanation': explanation.strip() or 'No explanation provided.'
                }
                st.session_state.questions.append(new_q)
                st.success(f"Question added to the '{new_cat.strip()}' category!")

# --- Footer ---
st.write("---")
st.markdown("**More learning:** Read IPC & CrPC summaries, check state police websites, and explore cyber law resources.")
st.caption("Educational app — consult official sources for legal accuracy.")
