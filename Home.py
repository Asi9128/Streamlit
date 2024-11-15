import streamlit as st


def Home_page():

    #st.image(r"C:\Users\HP1\OneDrive\Telcho_churn_ml.jpg")

    st.title('Integrating Machine Learning into a GUI with Streamlit')

    st.title("Telco Churn Classification App")


    st.markdown(""" 
        This app predicts whether a customer will churn or not using Machine Learning.
    """)

    st.subheader("Instructions")
    st.markdown("""
                - Upload a CSV file
                - Select features for classififcation
                - Choose a Machine Learning (ML) model from the dropdown
                - Click on Predict to get the predicted results
                - The app gives you a report on the performance of the ML model
                - The app provides a performance report with metrics such as accuracy, precision, recall, f1-score, etc.
    """)
    
    st.header("App features")
    st.markdown("""

        - **Data View**: View the uploaded data
        - **Predict View**: Get the predicted results from the ML model
        - **Dashboard**: View the performance of the ML model
    """)    

    st.subheader("User Benefits")
    st.markdown(""" 
                **Data Driven Approach**: Informed decision making based on the data
     """)
    

    st.write("### HOW TO USE THIS APP")
    with st.container(border=True):
        st.code("""
           # Activate the virtual environment
           env/scripts/activate
           
           # Run the app
           streamlit run app.py
    """)
# adding a video using the link
    #st.video("https://youtu.be/ngHM70aSEA8",autoplay=True)

# adding a clickable link
    #st.markdown("Watch a demo](https://youtu.be/MY4YJxn-9Og)")


# adding an image
    #st.image("https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg")
    #st.image(r"C:\Users\HP1\OneDrive\hands_on_keyboard.jpeg", width = 400)  
    
#another way of adding an image
# install pillow     
    #image = Image.open(r"C:\Users\HP1\Pictures\Screenshots\Screenshot 2024-10-18 230836.png")
    #st.image(image, width=400)


    st.subheader("Author: David Zodanu")

# Rating the App

    st.header("RATE THIS APP")

    rating = st.radio("Rate the app",("1","2","3","4","5"))
   
    if rating == "1":
        st.write("I'm sorry. You have bad taste!😀")    
    elif rating == "2":
        st.write("Good.You can do better!👏🏽")    
    elif rating == "3":
        st.write("You are getting there!🥳")    
    elif rating == "4": 
        st.write("You have good taste!🥂")    
    elif rating == "5":
        st.write("You are amazing!🎉")


    st.divider()
    
    st.write('NEED HELP?')
    st.write('Email: david.zodanu@azubiafrica.org')
    st.write('GitHub: https://github.com/Asi9128')
    st.write('LinkedIn: https://www.linkedin.com/in/david-zodanu/')
    st.write('Phone: +233 0555 717 949')


