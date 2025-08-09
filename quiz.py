import streamlit as st
import random
from typing import List, Dict

st.set_page_config(page_title="India Law Enforcement — Learn & Quiz", layout="centered")

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

if 'questions' not in st.session_state:
    st.session_state.questions = QUESTION_BANK.copy()

st.title("🇮🇳 Learn & Quiz: Law Enforcement in India")
st.markdown("Learn the basics, then test your knowledge with quick quizzes.")

with st.sidebar:
    st.header("Controls & Modes")
    mode = st.selectbox("Mode", ["Study Mode", "Quiz Mode", "Add Question", "Review Incorrect"])
    st.write("---")
    st.header("Quick Topics")
    topic = st.radio("Pick a topic to read", list(LESSONS.keys()))
    st.write("\n")
    st.button("Reset Progress", on_click=lambda: st.session_state.clear())

if mode == "Study Mode":
    st.subheader(topic)
    st.write(LESSONS[topic])
    st.info("Tip: Switch to Quiz Mode to test what you learned.")

def get_questions_for_category(category: str = None):
    if category is None or category == "All":
        return st.session_state.questions
    return [q for q in st.session_state.questions if q['category'] == category]

if 'quiz_qs' not in st.session_state:
    st.session_state.quiz_qs = []
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'incorrect' not in st.session_state:
    st.session_state.incorrect = []

if mode == "Quiz Mode":
    st.subheader("Quick Quiz — Choose category")
    categories = ["All"] + sorted({q['category'] for q in st.session_state.questions})
    chosen_cat = st.selectbox("Category", categories)
    available_count = len(get_questions_for_category(chosen_cat))
    num_q = st.slider("Number of questions", min_value=1, max_value=available_count, value=min(5, available_count))

    if st.button("Start Quiz") or len(st.session_state.quiz_qs) == 0:
        pool = get_questions_for_category(chosen_cat)
        num_q = min(num_q, len(pool))  # Safety check
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
            if chosen == q['answer']:
                st.success("Correct! ✅")
                st.session_state.score += 1
            else:
                st.error(f"Incorrect — correct answer: {q['answer']}")
                st.session_state.incorrect.append(q)

            st.write("**Explanation:**")
            st.write(q.get('explanation', ''))

            if st.session_state.current_index + 1 < len(st.session_state.quiz_qs):
                if st.button("Next Question", key=f"next_{st.session_state.current_index}"):
                    st.session_state.current_index += 1
                    st.experimental_rerun()
            else:
                st.balloons()
                st.write(f"**Quiz finished — Score: {st.session_state.score}/{len(st.session_state.quiz_qs)}**")
                if st.session_state.incorrect:
                    st.write("Review incorrect answers from the sidebar.")

if mode == "Review Incorrect":
    st.subheader("Review: Incorrect answers")
    if not st.session_state.incorrect:
        st.info("No incorrect answers this session.")
    else:
        for i, q in enumerate(st.session_state.incorrect, start=1):
            st.write(f"**{i}. {q['question']}**")
            st.write("Options: " + ", ".join(q['options']))
            st.write("Correct: " + q['answer'])
            st.write("Explanation: " + q.get('explanation', ''))
            st.write("---")

if mode == "Add Question":
    st.subheader("Add your own question")
    with st.form("add_q_form"):
        cat = st.selectbox("Category", [*sorted({q['category'] for q in st.session_state.questions}), "Other"])
        if cat == "Other":
            cat = st.text_input("Enter new category")
        question_text = st.text_input("Question")
        opts = [st.text_input(f"Option {i+1}") for i in range(4)]
        correct = st.selectbox("Correct option", opts)
        explanation = st.text_area("Short explanation")
        submitted = st.form_submit_button("Add question")
        if submitted:
            valid_opts = [o for o in opts if o.strip()]
            if not question_text or len(valid_opts) < 2 or correct not in valid_opts:
                st.error("Provide a valid question, at least two options, and choose the correct one.")
            else:
                new_q = {'category': cat if cat else 'Misc', 'question': question_text, 'options': valid_opts, 'answer': correct, 'explanation': explanation or 'No explanation provided.'}
                st.session_state.questions.append(new_q)
                st.success("Question added!")

st.write("---")
st.markdown("**More learning:** Read IPC & CrPC summaries, check state police websites, and explore cyber law resources.")
st.caption("Educational app — consult official sources for legal accuracy.")
