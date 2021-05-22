import streamlit as st
import pickle
import os


st.title('Are you adding to Lord of the Rings or Harry Potter?')
st.write('')
st.header('Text Predictions')

page = st.sidebar.selectbox("Select a page",
                            ('About', 'Make a prediction')
                           )
if page == 'About':
    st.write('Here is my Reddit Classification NLP Project about Famous Fantasy Stories!')
    celebrate = st.button("Click here to celebrate with me, my accomplishment!")
    if celebrate:
        st.balloons()
    
    cwd = os.getcwd()
    st.write(os.getcwd())
    st.write(type(cwd))
        
if page == 'Make a prediction':
    
    cwd = os.getcwd()
    
    st.write('Enhance either the Harry Potter, or Lord of the Rings story.  What would you like the story to include? ')
    
    with open(cwd + '/3-Reddit-NLP-Classification-LOTR-HP/app-files/reddit_pipe.pkl', mode='rb') as pickle_in: 
        pipe = pickle.load(pickle_in)
        
        user_text = st.text_input('Please input your story text: ')
    
    st.write(f"'{user_text}'")
    
    predicted_reddit = pipe.predict([user_text])[0]
    
    if predicted_reddit == 'tolkienfans':
        st.write('You have just added to the Lord of the Rings.')
    else: 
        st.write('You have just added to Harry Potter.')

        
# To run this streamlit go to the command line/terminal and type: 
# streamlit run (name-of-file)