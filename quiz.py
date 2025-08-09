import streamlit as st
import random

# Question bank
QUESTIONS = {
    "Traffic Rules": [
        {
            "question": "What is the legal speed limit for cars in most Indian cities?",
            "options": ["50 km/h", "60 km/h", "80 km/h", "100 km/h"],
            "answer": "50 km/h"
        },
        {
            "question": "What does a red traffic light mean?",
            "options": ["Go", "Stop", "Slow Down", "Yield"],
            "answer": "Stop"
        },
        {
            "question": "Which side should vehicles overtake from in India?",
            "options": ["Left", "Right", "Either side", "Depends on road"],
            "answer": "Right"
        },
        {
            "question": "Is wearing a seatbelt mandatory in the back seat in India?",
            "options": ["Yes", "No"],
            "answer": "Yes"
        },
        {
            "question": "What does a triangular traffic sign indicate?",
            "options": ["Warning", "Mandatory", "Information", "Speed limit"],
            "answer": "Warning"
        },
    ],
    "Cyber Crime Laws": [
        {
            "question": "Which act governs cyber crimes in India?",
            "options": ["IT Act 2000", "IPC", "Motor Vehicles Act", "Evidence Act"],
            "answer": "IT Act 2000"
        },
        {
            "question": "Phishing is related to?",
            "options": ["Fishing in rivers", "Online fraud emails", "Traffic rules", "Money laundering"],
            "answer": "Online fraud emails"
        },
        {
            "question": "What is the punishment for identity theft under IT Act?",
            "options": ["Up to 1 year", "Up to 3 years", "Up to 5 years", "No punishment"],
            "answer": "Up to 3 years"
        },
        {
            "question": "Which section deals with hacking under IT Act?",
            "options": ["66", "65", "67", "72"],
            "answer": "66"
        },
        {
            "question": "Sending obscene material online is punishable under?",
            "options": ["Section 67 IT Act", "Section 420 IPC", "Section 302 IPC", "None"],
            "answer": "Section 67 IT Act"
        },
    ],
    "Indian Penal Code": [
        {
            "question": "IPC stands for?",
            "options": ["Indian Police Code", "Indian Penal Code", "International Penal Code", "Indian People's Code"],
            "answer": "Indian Penal Code"
        },
        {
            "question": "Which section of IPC deals with murder?",
            "options": ["302", "307", "376", "420"],
            "answer": "302"
        },
        {
            "question": "Cheating is covered under which IPC section?",
            "options": ["420", "120B", "375", "304"],
            "answer": "420"
        },
        {
            "question": "Section 376 of IPC deals with?",
            "options": ["Theft", "Rape", "Murder", "Forgery"],
            "answer": "Rape"
        },
        {
            "question": "Which IPC section deals with attempt to murder?",
            "options": ["307", "302", "326", "120B"],
            "answer": "307"
        },
    ]
}

# Functions
def get_questions_for_category(cat):
    return QUESTIONS.get(cat, [])

# UI
st.title("Law Enforcement of India - Learning & Quiz")

if "quiz_qs" not in st.session_state:
    st.session_state.quiz_qs = []
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "incorrect" not in st.session_state:
    st.session_state.incorrect = []

categories = list(QUESTIONS.keys())
chosen_cat = st.selectbox("Choose a topic", categories)
available_count = len(get_questions_for_category(chosen_cat))

# This part will still throw the slider error if available_count == 0 (as before)
num_q = st.slider(
    "Number of questions",
    min_value=1,
    max_value=available_count,
    value=min(5, available_count)
)

if st.button("Start Quiz"):
    pool = get_questions_for_category(chosen_cat)
    st.session_state.quiz_qs = random.sample(pool, k=num_q)
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.incorrect = []

if st.session_state.quiz_qs and st.session_state.current_index < len(st.session_state.quiz_qs):
    q = st.session_state.quiz_qs[st.session_state.current_index]
    choice = st.radio(q["question"], q["options"], key=f"q_{st.session_state.current_index}")

    if st.button("Submit Answer"):
        if choice == q["answer"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Wrong! The correct answer was: {q['answer']}")
            st.session_state.incorrect.append(q)
        st.session_state.current_index += 1

elif st.session_state.quiz_qs and st.session_state.current_index >= len(st.session_state.quiz_qs):
    st.success(f"Quiz Completed! Your Score: {st.session_state.score}/{len(st.session_state.quiz_qs)}")
    if st.session_state.incorrect:
        st.subheader("Review Incorrect Answers")
        for wrong in st.session_state.incorrect:
            st.write(f"**Q:** {wrong['question']}")
            st.write(f"**Correct:** {wrong['answer']}")
