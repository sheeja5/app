import streamlit as st
import random

# ------------------ Data ------------------
learn_data = {
    "Law Enforcement Basics": [
        {
            "title": "Central Bureau of Investigation (CBI)",
            "content": "The CBI is India's premier investigating agency handling corruption, criminal cases, and special crimes. It operates under the Ministry of Personnel."
        },
        {
            "title": "Information Technology Act, 2000",
            "content": "This law deals with cybercrime, digital signatures, and electronic governance in India."
        }
    ],
    "Police Powers": [
        {
            "title": "Section 41 of the CrPC",
            "content": "Allows police to arrest without a warrant under specific conditions."
        },
        {
            "title": "Section 50 of the CrPC",
            "content": "Requires police to inform the arrested person of the grounds of arrest and their right to bail."
        }
    ]
}

quiz_data = {
    "Law Enforcement Basics": [
        {
            "question": "Which body is the central investigative agency in India?",
            "options": ["CBI", "NIA", "RAW", "IB"],
            "answer": "CBI",
            "explanation": "The Central Bureau of Investigation (CBI) is the primary investigative agency in India."
        },
        {
            "question": "Which law in India deals with cybercrime?",
            "options": ["IT Act 2000", "IPC", "CRPC", "Evidence Act"],
            "answer": "IT Act 2000",
            "explanation": "The Information Technology Act, 2000 deals with cybercrimes in India."
        }
    ],
    "Police Powers": [
        {
            "question": "Under which section of the CrPC can police arrest without a warrant?",
            "options": ["Section 41", "Section 42", "Section 46", "Section 50"],
            "answer": "Section 41",
            "explanation": "Section 41 of the Criminal Procedure Code allows arrest without a warrant under certain conditions."
        }
    ]
}

categories = list(quiz_data.keys())

# ------------------ Functions ------------------
def get_questions_for_category(category):
    return quiz_data.get(category, [])

def show_question(index):
    q = st.session_state.quiz_qs[index]
    st.write(f"**Q{index+1}: {q['question']}**")
    choice = st.radio("Choose an option:", q['options'], key=f"q_{index}")
    if st.button("Submit Answer", key=f"submit_{index}"):
        if choice == q['answer']:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Wrong! Correct answer: {q['answer']}")
            st.info(q['explanation'])
            st.session_state.incorrect.append(q)
        st.session_state.current_index += 1

def learn_mode(category):
    st.subheader(f"📚 Learn: {category}")
    for item in learn_data.get(category, []):
        st.markdown(f"### {item['title']}")
        st.write(item["content"])
    st.info("Once you finish learning, switch to Quiz Mode to test your knowledge.")

# ------------------ Streamlit UI ------------------
st.title("🇮🇳 Law Enforcement in India - Learn & Quiz")

mode = st.radio("Select Mode", ["Learn", "Quiz"])

if "quiz_qs" not in st.session_state:
    st.session_state.quiz_qs = []
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "incorrect" not in st.session_state:
    st.session_state.incorrect = []

chosen_cat = st.selectbox("Choose a category", categories)
available_count = len(get_questions_for_category(chosen_cat))

# Mode handling
if mode == "Learn":
    learn_mode(chosen_cat)

elif mode == "Quiz":
    if available_count > 0:
        num_q = st.slider(
            "Number of questions",
            min_value=1,
            max_value=available_count,
            value=min(5, available_count)
        )

        if st.button("Start Quiz"):
            pool = get_questions_for_category(chosen_cat)
            num_q = max(1, min(num_q, len(pool)))  # Safety check
            st.session_state.quiz_qs = random.sample(pool, k=num_q)
            st.session_state.current_index = 0
            st.session_state.score = 0
            st.session_state.incorrect = []

        if st.session_state.quiz_qs and st.session_state.current_index < len(st.session_state.quiz_qs):
            show_question(st.session_state.current_index)
        elif st.session_state.quiz_qs and st.session_state.current_index >= len(st.session_state.quiz_qs):
            st.success(f"🎯 Quiz completed! Your score: {st.session_state.score}/{len(st.session_state.quiz_qs)}")
            if st.session_state.incorrect:
                st.subheader("Review Incorrect Answers")
                for wrong in st.session_state.incorrect:
                    st.write(f"**{wrong['question']}**")
                    st.write(f"✅ Correct Answer: {wrong['answer']}")
                    st.info(wrong['explanation'])
    else:
        st.warning("⚠ No questions available in this category. Please choose another.")
