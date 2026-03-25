import streamlit as st
import time

# Sets the browser tab title
st.set_page_config(page_title="Happy Birthday!", page_icon="🎂")

# The main header
st.title("Happy Birthday to the most amazing girl! 🎉")

# A button to trigger the surprise
if st.button("Click here for your present"):
    with st.spinner("Loading something special..."):
        time.sleep(2) # Adds a little dramatic suspense
    
    st.balloons() # Literally makes balloons fly up the screen!
    st.success("I love you!")
    
    # You can easily add an image from your computer
    # st.image("our_favorite_picture.jpg", caption="Best day ever.")