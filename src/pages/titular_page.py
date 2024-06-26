import streamlit as st

TITLE = "Badanie odpowiedzi Dużych Modeli Językowych z użyciem zewnętrznych baz wiedzy"
WELCOME_MESSAGE = """Witam w badaniu poświęconym wspomaganiu Modeli Językowych dodatkowymi źródłami wiedzy.
Badanie to jest prowadzone w ramach mojej pracy licencjackiej.
Po wyrażaniu zgody na udział w badaniu pojawi się kilka przykładów pytań oraz wygenerowanych odpowiedzi odnoszących się do tego samego fragmentu tekstu, dostępnego na każdej stronie.
Odpowiedzi są generowane na podstawie informacji znalezionych przez system w czasie rzeczywisty, przez co model językowy może się mylić lub nie znać odpowiedzi.
Państwa zadaniem jest zidentyfikować, czy odpowiedź jest poprawna zgodnie z podanym fragmentem wybierająć **Poprawna**, bądź **Niepoprawna**.
Państwa odpowiedzi będą całkowicie anonimowe."""
CONSENT_MESSAGE = "Wyrażam zgodę."

def refresh_state():
    st.session_state.consent_given = True
    st.session_state.page_number = 1

def titular_page():
    st.title(TITLE)
    
    st.write(WELCOME_MESSAGE)

    st.button(CONSENT_MESSAGE, on_click=refresh_state)