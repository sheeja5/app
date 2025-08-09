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
    "Indian Penal Code (IPC) Basics": (
        "The Indian Penal Code is the main criminal code of India. It covers all substantive aspects of criminal law. "
        "It defines various offenses and provides punishments for them, such as 'offences against the human body' (e.g., murder, assault), 'offences against property' (e.g., theft, robbery), and 'offences against the state'."
    ),
}

QUESTION_BANK: List[Dict] = [
    {"category": "Indian Police System", "question": "Which body is primarily responsible for criminal investigation in states of India?", "options": ["Central Bureau of Investigation (CBI)", "State Police", "National Investigation Agency (NIA)", "Central Reserve Police Force (CRPF)"], "answer": "State Police", "explanation": "Most day-to-day criminal investigations within a state's territorial limits are handled by the State Police."},
    {"category": "Police Ranks & Structure", "question": "Which rank is typically senior to Inspector in the police hierarchy?", "options": ["Head Constable", "Sub-Inspector", "Inspector", "Superintendent of Police"], "answer": "Superintendent of Police", "explanation": "A Superintendent of Police (SP) is senior and usually heads a district police force."},
    {"category": "Rights of Citizens & Police Duties", "question": "Which article guarantees the right to life and personal liberty?", "options": ["Article 19", "Article 21", "Article 14", "Article 25"], "answer": "Article 21", "explanation": "Article 21 guarantees protection of life and personal liberty except according to procedure established by law."},
    {"category": "Investigation Basics", "question": "What is the first step usually taken by police when a cognizable offence is reported?", "options": ["Charge-sheet", "Filing FIR", "Trial in court", "Forensic analysis"], "answer": "Filing FIR", "explanation": "For cognizable offences, police file a First Information Report (FIR) before investigation."},
    {"category": "Cybercrime & Modern Challenges", "question": "Which act provides many legal provisions to deal with cyber offences?", "options": ["Indian Penal Code", "Information Technology Act", "Evidence Act", "Contract Act"], "answer": "Information Technology Act", "explanation": "The Information Technology Act, 2000, provides a legal framework for cybercrime."},
    {"category": "Indian Penal Code (IPC) Basics", "question": "What is the primary function of the Indian Penal Code?", "options": ["Provide police investigation procedures", "Define offenses and their punishments", "Protect human rights", "Outline court trial procedures"], "answer": "Define offenses and their punishments", "explanation": "The IPC is the substantive law that defines criminal offenses and specifies their punishments."},
    {"category": "Indian Penal Code (IPC) Basics", "question": "Which category of crime does the IPC cover?", "options": ["Civil disputes only", "Administrative violations", "Offences against the human body and property", "All of the above"], "answer": "Offences against the human body and property", "explanation": "The IPC defines a wide range of crimes, including those against people, property, and the state."},
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
    if 'answer_submitted' not in st.session_state:
        st.session_state.answer_submitted = False
    if 'user_choice' not in st.session_state:
        st.session_state.user_choice = None
    if 'total_score' not in st.session_state:
        st.session_state.total_score = 0
    if 'total_quizzes' not in st.session_state:
        st.session_state.total_quizzes = 0

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

    # Add search functionality to the sidebar
    search_term = st.text_input("Search Topics", key="topic_search")
    
    # Filter topics based on search term
    filtered_lessons = {
        k: v for k, v in LESSONS.items()
        if search_term.lower() in k.lower() or search_term.lower() in v.lower()
    }
    
    if not filtered_lessons:
        st.warning("No topics match your search.")
    else:
        topic = st.radio("Pick a topic to read", list(filtered_lessons.keys()))
    
    st.write("\n")
    if st.button("Reset All Progress"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

    # Display total progress
    st.write("---")
    st.header("Overall Progress")
    st.metric(label="Total Quizzes Taken", value=st.session_state.total_quizzes)
    st.metric(label="Total Score", value=st.session_state.total_score)


# --- Logic for Study Mode ---
if mode == "Study Mode":
    if filtered_lessons:
        st.subheader(topic)
        st.write(LESSONS[topic])
        st.info("Tip: Switch to Quiz Mode to test what you learned.")

# --- Helper Function for Quiz ---
def get_questions_for_category(category: str = None):
    if category is None or category == "All":
        return st.session_state.questions
    # Safely check for the category key
    return [q for q in st.session_state.questions if q.get('category') == category]

# --- Logic for Quiz Mode (REFACTORED & HARDENED) ---
if mode == "Quiz Mode":
    st.subheader("Quick Quiz — Choose category")

    if not st.session_state.quiz_qs:
        categories = ["All"] + sorted({q.get('category', 'General') for q in st.session_state.questions})
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
            st.rerun()

    if st.session_state.quiz_qs:
        if st.session_state.current_index >= len(st.session_state.quiz_qs):
            # Final quiz results
            st.balloons()
            st.success(f"**Quiz finished! Your Score: {st.session_state.score}/{len(st.session_state.quiz_qs)}**")
            
            # Update total stats
            st.session_state.total_score += st.session_state.score
            st.session_state.total_quizzes += 1

            if st.session_state.incorrect:
                st.warning("You can review your incorrect answers from the sidebar in 'Review Incorrect' mode.")
            if st.button("Take Another Quiz"):
                st.session_state.quiz_qs = []
                st.rerun()
        else:
            q = st.session_state.quiz_qs[st.session_state.current_index]
            st.write(f"**Question {st.session_state.current_index + 1} of {len(st.session_state.quiz_qs)}**")
            # --- FIX: Use .get() for safe access to prevent KeyError ---
            st.write(f"_{q.get('category', 'General')}_")
            st.markdown(f"### {q.get('question', 'Error: Question text not found.')}")

            if not st.session_state.answer_submitted:
                options = q.get('options', [])
                if not options:
                    st.error("Error: This question has no options.")
                else:
                    user_choice = st.radio("Choose an answer:", options, key=f"opt_{st.session_state.current_index}")

                    if st.button("Submit Answer"):
                        st.session_state.user_choice = user_choice
                        st.session_state.answer_submitted = True
                        if user_choice == q.get('answer'):
                            st.session_state.score += 1
                        else:
                            st.session_state.incorrect.append(q)
                        st.rerun()
            else:
                correct_answer = q.get('answer', 'N/A')
                if st.session_state.user_choice == correct_answer:
                    st.success(f"Correct! ✅ The answer is **{correct_answer}**.")
                else:
                    st.error(f"Incorrect. You chose **{st.session_state.user_choice}**. The correct answer was **{correct_answer}**.")

                st.info(f"**Explanation:** {q.get('explanation', 'No explanation provided.')}")

                if st.button("Next Question"):
                    st.session_state.current_index += 1
                    st.session_state.answer_submitted = False
                    st.session_state.user_choice = None
                    st.rerun()


# --- Logic for Review Incorrect (HARDENED) ---
if mode == "Review Incorrect":
    st.subheader("Review: Incorrect answers")
    if not st.session_state.get('incorrect'):
        st.info("No incorrect answers this session. Well done!")
    else:
        for i, q in enumerate(st.session_state.incorrect, start=1):
            with st.container():
                # --- FIX: Use .get() for all data access to prevent errors ---
                st.write(f"**{i}. {q.get('question', 'N/A')}**")
                st.error(f"**Correct Answer:** {q.get('answer', 'N/A')}")
                st.write(f"**Explanation:** {q.get('explanation', 'No explanation provided.')}")
                st.write("---")

# --- Logic for Add Question ---
if mode == "Add Question":
    st.subheader("Add your own question")
    with st.form("add_q_form"):
        current_categories = sorted({q.get('category', 'General') for q in st.session_state.questions})
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
            correct_answer = opts[0].strip()
            valid_opts = [o.strip() for o in opts if o.strip()]
            
            if not new_cat.strip() or not question_text.strip() or len(valid_opts) < 2 or not correct_answer:
                st.error("Please provide a category, a question, and at least two options (with the correct answer in the first box).")
            else:
                random.shuffle(valid_opts)
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
