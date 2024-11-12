import streamlit as st
from Home import Home_page


def authentication():
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = False

    if not st.session_state['authentication_status'] :
        login_form()
    else:
        show_authentication_page()



def login_form():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.session_state['authentication_status'] = True
           # st.session_state['username'] = username
            #st.experimental_rerun()
        else:
            st.error("Username/password is incorrect")


def show_authentication_page():
    st.title("Welcome")
    #Home_page()
    #st.write(f"Hello {st.session_state['username']}")

    if st.button("Logout"):
        logout()

def logout():
    st.session_state.clear()
    #st.experimental_rerun()


#def show_authenticated_page():
   # show_authentication_page()
