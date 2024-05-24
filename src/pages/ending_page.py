import streamlit as st

TITLE = "Dziękuję za udział w badaniu!"
MESSAGE = "Jeśli są Państwo zainteresowani wynikami oraz opracowaniem badania, proszę o kontakt na mojego maila studenckiego."
EMAIL = f"Email: {st.secrets['e`mail']}"

def ending_page():
    st.title(TITLE)
    st.write(MESSAGE)
    st.write(EMAIL)