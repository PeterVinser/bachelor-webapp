import streamlit as st

def titular_page():
    st.title("Online Experiment")
    st.write("Welcome to this online experiment. Do you consent?")

    if st.button("I Consent"):
        st.session_state.consent_given = True
        st.session_state.page_number = 1

        st.rerun()

def experiment_page():
    st.session_state.page_number

    st.write("**Text fragment**")
    st.write("Question")
    st.write("Answer")

    if st.button("Correct"):
        st.session_state.correct_count += 1
    if st.button("Wrong"):
        st.session_state.wrong_count += 1

    if st.button("Next"):
        st.session_state.page_number += 1
        
        if st.session_state.page_number > 10:
            st.session_state.page_number = 11

        st.rerun()

def main():
    if 'consent_given' not in st.session_state:
        st.session_state.consent_given = False
    if 'page_number' not in st.session_state:
        st.session_state.page_number = 0
    if 'correct_count' not in st.session_state:
        st.session_state.correct_count = 0
    if 'wrong_count' not in st.session_state:
        st.session_state.wrong_count = 0

    if not st.session_state.consent_given:
        titular_page()
    else:
        if st.session_state.page_number <= 10:
            experiment_page()
        else:
            st.write("Thank you for your participation")

if __name__ == '__main__':
    main()