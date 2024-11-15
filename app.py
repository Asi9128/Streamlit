import streamlit as st
from Home import Home_page
from Data import data_page
from Predict import predict_page
from Dashboard import dashboard_page
from auth import authentication
# from History import history_page

# Authentication and login logic
def authentication():
    if 'authentication_status' not in st.session_state:
        st.session_state['authentication_status'] = False

    if not st.session_state['authentication_status']:
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
        else:
            st.error("Username/password is incorrect")

def show_authentication_page():
    st.title("Welcome")
    st.toast("You are logged in 🎉.", icon="✅")
    st.balloons()
    #st.write("You are logged in 🎉.")
    if st.button("Logout"):
        logout()

def logout():
    st.session_state.clear()

# Main function for handling navigation
def main():
    # Call authentication function
    authentication()

    # Only display navigation if authenticated
    if st.session_state.get('authentication_status'):
        # Sidebar navigation
        st.sidebar.title("Navigator")
        st.sidebar.write("Select a page to view:")
        
        # Sidebar navigation options
        page = st.sidebar.selectbox("Navigate", ["Home 🏠", "Data 📈", "Predict 🪄", "Dashboard 📊", "History ⏰"])

        # Display the selected page content
        if page == "Home 🏠":
            Home_page()
        elif page == "Data 📈":
            data_page()
        elif page == "Predict 🪄":
            predict_page()
        elif page == "Dashboard 📊":
            dashboard_page()
        # elif page == "History⏰":
            # history_page()

# Run the main function
if __name__ == "__main__":
    main()





