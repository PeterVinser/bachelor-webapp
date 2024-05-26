import streamlit as st
from pages.titular_page import titular_page
from pages.experiment_page import experiment_page
from pages.ending_page import ending_page
from utils.sessions_utils import init_session_state, load_data_into_session

def hide_streamlit_style():
    st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

def main():
    hide_streamlit_style()
    init_session_state()
    load_data_into_session()

    if not st.session_state.consent_given:
        titular_page()
    else:
        if st.session_state.page_number <= 10:
            experiment_page()
        else:
            ending_page()

if __name__ == '__main__':
    main()