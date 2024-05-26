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

def experiment_page():
    st.title(TITLE)
    st.write(FRAGMENT)

    passage = st.session_state.passages[st.session_state.page_number - 1]

    fragment, query = passage["context"], passage["question"]

    st.write(fragment)
    st.write(f"{QUESTION}: {query}")

    if st.session_state.current_answer_data is None:
        retrieval_type, temperature = get_control_variables()
        
        with st.spinner(FETCHING_ANSWER):
            response = fetch_answer(query, retrieval_type, temperature)

        if response:
            response["retrieval_type"] = retrieval_type
            response["temperature"] = temperature
            st.session_state.current_answer_data = response

    if st.session_state.current_answer_data:
        answer = st.session_state.current_answer_data["answer"]
        st.write(f"{ANSWER}: {answer}")

        col1, col2 = st.columns(2)

        with col1:
            if st.button(CORRECT):
                save_to_db(query, st.session_state.current_answer_data, True)
                st.session_state.page_number += 1
                st.session_state.current_answer_data = None
                st.rerun()

        with col2:
            if st.button(WRONG):
                save_to_db(query, st.session_state.current_answer_data, False)
                st.session_state.page_number += 1
                st.session_state.current_answer_data = None
                st.rerun()