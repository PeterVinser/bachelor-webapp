import streamlit as st
from data.data_handler import save_to_db
from utils.api_utils import get_control_variables, fetch_answer

TITLE = "Proszę ocenić odpowiedź kiedy się pojawi"
FRAGMENT = "**Fragment na podstawie, którego powinna zostać sformułowana odpowiedź:**"
QUESTION = "**Pytanie**"
ANSWER = "**Odpowiedź**"
FETCHING_ANSWER = "Odpowiedź jest generowana..."
CORRECT = "Poprawna"
WRONG = "Niepoprawna"

def refresh_state(query, correct):
    save_to_db(query, st.session_state.current_answer_data, correct)
    st.session_state.page_number += 1
    st.session_state.current_answer_data = None

def experiment_page():
    st.title(TITLE)
    st.write(FRAGMENT)

    passage = st.session_state.passages[st.session_state.page_number - 1]

    fragment, query = passage["context"], passage["question"]

    st.write(fragment)
    st.write(f"{QUESTION}: {query}")

    answer_component = st.empty()

    with st.empty():
        if st.session_state.current_answer_data is None:
            retrieval_type, temperature = get_control_variables()
            
            with st.spinner(FETCHING_ANSWER):
                response = fetch_answer(query, retrieval_type, temperature)

            if response:
                response["retrieval_type"] = retrieval_type
                response["temperature"] = temperature
                st.session_state.current_answer_data = response

                answer = st.session_state.current_answer_data["answer"]
                answer_component.write(f"{ANSWER}: {answer}")

                col1, col2 = st.columns(2)

                with col1:
                    st.button(CORRECT, key="correct_button", on_click=refresh_state, args=[query, True])

                with col2:
                    st.button(WRONG, key="wrong_button", on_click=refresh_state, args=[query, False])
        