import streamlit as st
from data.data_handler import get_passages

def init_session_state():
    if 'passages_loaded' not in st.session_state:
        st.session_state.data_loaded = False

    if 'passages' not in st.session_state:
        st.session_state.passages = []

    if 'consent_given' not in st.session_state:
        st.session_state.consent_given = False
    if 'page_number' not in st.session_state:
        st.session_state.page_number = 0

    if 'current_answer_data' not in st.session_state:
        st.session_state.current_answer_data = None
    
def load_data_into_session():
    if not st.session_state.data_loaded:
        st.session_state.passages = get_passages()
        st.session_state.passages_loaded = True