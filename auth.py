import streamlit as st
import firebase_admin
from firebase_admin import auth

def login_screen():
    st.title("🔐 Neural Scribe - Login")
    email = st.text_input("📧 Email")
    password = st.text_input("🔑 Password", type="password")
    if st.button("Login"):
        st.session_state["user"] = {"email": email}  # Fake session (Replace with Firebase Authentication)
        st.rerun()

def check_auth():
    return "user" in st.session_state

def logout():
    st.session_state.pop("user", None)
    st.rerun()
