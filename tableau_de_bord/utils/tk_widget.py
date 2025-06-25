import streamlit as st

def select_file(label="Choisissez un fichier :"):
    uploaded_file = st.file_uploader(label, type=None, accept_multiple_files=False)
    if uploaded_file is not None:
        return uploaded_file
    return None
