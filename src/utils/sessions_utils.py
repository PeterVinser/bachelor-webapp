import streamlit as st
from data.data_handler import get_passage


def init_session_state():
    if 'passage_loaded' not in st.session_state:
        st.session_state.data_loaded = False
    
    if 'fragment' not in st.session_state:
        st.session_state.fragment = ''
    
    if 'queries' not in st.session_state:
        st.session_state.queries = []

    if 'consent_given' not in st.session_state:
        st.session_state.consent_given = False
    if 'page_number' not in st.session_state:
        st.session_state.page_number = 0

    if 'current_answer_data' not in st.session_state:
        st.session_state.current_answer_data = None
    
def load_data_into_session():
    if not st.session_state.data_loaded:
        passage = get_passage()
        st.session_state.fragment = passage['context']
        st.session_state.queries = passage['queries']
        st.session_state.passage_loaded = True

        st.session_state.queries_count = len(passage['queries'])