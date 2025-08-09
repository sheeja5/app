import streamlit as st
import random
from typing import List, Dict

# --------------------------------------------
# Simple Streamlit Quiz + Lessons App
# Topic: Law Enforcement in India
# Single-file app. Save as streamlit_india_law_enforcement_quiz.py
# Run: pip install streamlit && streamlit run streamlit_india_law_enforcement_quiz.py
# --------------------------------------------

st.set_page_config(page_title="India Law Enforcement — Learn & Quiz", layout="centered")

# --------------------------------------------------
# Sample lessons content (brief, educational)
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
        "Complaints against police are handled by state mechanisms (e.g. human rights commissions, police complaint authorities) — recent legal frameworks emphasize accountability and transparency."
    ),
    "Investigation Basics": (
        "Investigation stages: First information report (FIR), preliminary inquiry, evidence collection, arrest (with legal safeguards), charge-sheet, and court proceedings. "
        "Investigation must follow procedure under the Criminal Procedure Code (CrPC) and relevant laws; collection of forensics and digital evidence is increasingly important."
    ),
    "Cybercrime & Modern Challenges": (
        "Cybercrime is handled under the Information Technology Act and IPC sections relating to fraud, hacking, identity theft, and harassment. "
        "Specialised cyber cells and training are critical as crimes shift online."
    ),
}

# --------------------------------------------------
# Sample question bank
QUESTION_BANK: List[Dict] = [
    {
        "category": "Indian Police System",
        "question": "Which body is primarily responsible for criminal investigation in states of India?",
        "options": ["Central Bureau of Investigation (CBI)", "State Police", "National Investigation Agency (NIA)", "Central Reserve Police Force (CRPF)"],
        "answer": "State Police",
        "explanation": "Most day-to-day criminal investigations within a state's territorial limits are handled by the State Police. Central agencies step in for inter-state, national security, or special cases."
    },
    {
        "category": "Police Ranks & Structure",
        "question": "Which of the following ranks is typically senior to Inspector in the police hierarchy?",
        "options": ["Head Constable", "Sub-Inspector", "Inspector", "Superintendent of Police"],
        "answer": "Superintendent of Police",
        "explanation": "A Superintendent of Police (SP) is senior and usually heads a district police force (or holds an equivalent leadership position)."
    },
    {
        "category": "Rights of Citizens & Police Duties",
        "question": "Which article of the Indian Constitution guarantees the right to life and personal liberty?",
        "options": ["Article 19", "Article 21", "Article 14", "Article 25"],
        "answer": "Article 21",
        "explanation": "Article 21 guarantees protection of life and personal liberty except according to procedure established by law. It is a cornerstone of civil liberties."
    },
    {
        "category": "Investigation Basics",
        "question": "What is the first step usually taken by police when a cognizable offence is reported?",
        "options": ["Charge-sheet", "Filing FIR", "Trial in court", "Forensic analysis"],
        "answer": "Filing FIR",
        "explanation": "For cognizable offences, police file a First Information Report (FIR) and begin investigation under the Criminal Procedure Code."
    },
    {
        "category": "Cybercrime & Modern Challenges",
        "question": "Which act provides many legal provisions to deal with cyber offences in India?",
        "options": ["Indian Penal Code", "Information Technology Act", "Evidence Act", "Contract Act"],
        "answer": "Information Technology Act",
        "explanation": "The Information Technology Act, 2000, and its amendments provide legal framework for offences involving computers and networks. IPC sections also apply to cyber offences where relevant."
    },
]

# Keep a copy for adding new questions in-session
if 'questions' not in st.session_state:
    st.session_state.questions = QUESTION_BANK.copy()

# App layout
st.title("🇮🇳 Learn & Quiz: Law Enforcement in India")
st.markdown("Learn the basics, then test your knowledge with quick quizzes. Perfect for students, civics enthusiasts, and curious citizens.")

with st.sidebar:
    st.header("Controls & Modes")
    mode = st.selectbox("Mode", ["Study Mode", "Quiz Mode", "Add Question", "Review Incorrect"])
    st.write("---")
    st.header("Quick Topics")
    topic = st.radio("Pick a topic to read", list(LESSONS.keys()))
    st.write("\n")
    st.button("Reset Progress", on_click=lambda: st.session_state.clear())

# Show lesson content
if mode == "Study Mode":
    st.subheader(topic)
    st.write(LESSONS[topic])
    st.info("Tip: Switch to Quiz Mode from the sidebar to test what you learned.")

# Utility: select questions by category
def get_questions_for_category(category: str = None):
    if category is None or category == "All":
        return st.session_state.questions
    return [q for q in st.session_state.questions if q['category'] == category]

# Initialize session state for quiz
if 'quiz_qs' not in st.session_state:
    st.session_state.quiz_qs = []
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'incorrect' not in st.session_state:
    st.session_state.incorrect = []

if mode == "Quiz Mode":
    st.subheader("Quick Quiz — Choose category and difficulty")
    categories = ["All"] + sorted({q['category'] for q in st.session_state.questions})
    chosen_cat = st.selectbox("Category", categories)
    num_q = st.slider("Number of questions", min_value=1, max_value=min(10, len(get_questions_for_category(chosen_cat))), value=5)

    if st.button("Start Quiz") or len(st.session_state.quiz_qs) == 0:
        pool = get_questions_for_category(chosen_cat)
        st.session_state.quiz_qs = random.sample(pool, k=num_q)
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.incorrect = []

    if st.session_state.quiz_qs:
        q = st.session_state.quiz_qs[st.session_state.current_index]
        st.write(f"**Question {st.session_state.current_index + 1} of {len(st.session_state.quiz_qs)}**")
        st.write(q['question'])

        chosen = st.radio("Choose an answer:", q['options'], key=f"opt_{st.session_state.current_index}")

        if st.button("Submit Answer", key=f"submit_{st.session_state.current_index}"):
            correct = (chosen == q['answer'])
            if correct:
                st.success("Correct! ✅")
                st.session_state.score += 1
            else:
                st.error(f"Incorrect — correct answer: {q['answer']}")
                st.session_state.incorrect.append(q)

            st.write("**Explanation:**")
            st.write(q.get('explanation', 'No explanation available.'))

            # Next question button / finish
            if st.session_state.current_index + 1 < len(st.session_state.quiz_qs):
                if st.button("Next Question", key=f"next_{st.session_state.current_index}"):
                    st.session_state.current_index += 1
                    st.experimental_rerun()
            else:
                st.balloons()
                st.write(f"**Quiz finished — Score: {st.session_state.score}/{len(st.session_state.quiz_qs)}**")
                if st.session_state.incorrect:
                    st.write("You can review the incorrect questions from the sidebar (Review Incorrect).")


if mode == "Review Incorrect":
    st.subheader("Review: Questions you answered incorrectly (this session)")
    if not st.session_state.incorrect:
        st.info("You have no incorrect answers this session — try a quiz first!")
    else:
        for i, q in enumerate(st.session_state.incorrect, start=1):
            st.write(f"**{i}. {q['question']}**")
            st.write("Options: " + ", ".join(q['options']))
            st.write("Correct: " + q['answer'])
            st.write("Explanation: " + q.get('explanation', ''))
            st.write("---")


if mode == "Add Question":
    st.subheader("Add your own question to the in-session bank")
    with st.form("add_q_form"):
        cat = st.selectbox("Category", [*sorted({q['category'] for q in st.session_state.questions}), "Other"])
        if cat == "Other":
            cat = st.text_input("Enter new category")
        question_text = st.text_input("Question")
        opt1 = st.text_input("Option 1")
        opt2 = st.text_input("Option 2")
        opt3 = st.text_input("Option 3 (optional)", value="")
        opt4 = st.text_input("Option 4 (optional)", value="")
        correct = st.selectbox("Correct option", [opt1, opt2, opt3, opt4])
        explanation = st.text_area("Short explanation (why the answer is correct)")
        submitted = st.form_submit_button("Add question")
        if submitted:
            opts = [o for o in [opt1, opt2, opt3, opt4] if o and o.strip()]
            if not question_text or len(opts) < 2 or correct not in opts:
                st.error("Please provide a valid question, at least two options, and choose the correct one.")
            else:
                new_q = {
                    'category': cat if cat else 'Misc',
                    'question': question_text,
                    'options': opts,
                    'answer': correct,
                    'explanation': explanation or 'No explanation provided.'
                }
                st.session_state.questions.append(new_q)
                st.success("Question added to the session! It will be available until you refresh or reset the app.")

# Footer / extra learning resources
st.write("---")
st.markdown("**Want to learn more?** Here are study suggestions:\n\n"
            "- Read the Indian Penal Code (IPC) & Criminal Procedure Code (CrPC) summaries.\n"
            "- Look up state police websites for structure and local initiatives.\n"
            "- Explore resources on cyber law and forensic investigation basics.")

st.caption("This app is an educational toy — for authoritative legal advice or current statutes, consult official sources or a legal professional.")

# End of file
