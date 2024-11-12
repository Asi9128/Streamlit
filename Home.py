import streamlit as st
from PIL import Image

def Home_page():

    st.image(r"C:\Users\HP1\Pictures\Gemini_Generated_Image_fe3y3afe3y3afe3y.jpeg", width=150)

    st.title('Embedded ML in GUI using Streamlit')

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
           # Acitivate the virtual environment
           env/scripts/activate
           
           # Run the app
           streamlit run p.py
    """)
# adding a video using the link
    st.video("https://youtu.be/ngHM70aSEA8",autoplay=True)

# adding a clickable link
    st.markdown("Watch a demo](https://youtu.be/MY4YJxn-9Og)")


# adding an image
    #st.image("https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg")
    st.image(r"C:\Users\HP1\Pictures\Gemini_Generated_Image_fe3y3afe3y3afe3y.jpeg", width=150)   
    
#another way of adding an image
# install pillow     
    #image = Image.open(r"C:\Users\HP1\Pictures\Screenshots\Screenshot 2024-10-18 230836.png")
    #st.image(image, width=400)


    st.subheader("Author: David Zodanu")

# Creating a like button

    st.header("RATE THIS APP")

    button1 = st.button("Click me!")
    #if button1:
      #  st.write("Thanks for clicking me!") 

    like = st.checkbox("Do you like this app?")

    button2 = st.button("Submit")
    if button2:
    
        if like:
            st.write("You are amazing!")
        else:
            st.write("I'm sorry. You have bad taste!")
    

    st.radio("Rate the app",("1","2","3","4","5"))


    st.divider()
    st.write("===="*25)

    st.write('NEED HELP?')
    st.write('Email: david.zodanu@azubi.org')
    st.write('GitHub: https://github.com/davidzodanu')
    st.write('Twitter: @david_zodanu')
    st.write('LinkedIn: https://www.linkedin.com/in/david-zodanu/')
    st.write('Phone: +233 0555 717 949')


