import streamlit as st

# Setup the page
st.set_page_config(page_title="Memory Lane", page_icon="📸", layout="centered")

st.title("A Walk Down Memory Lane 🎞️")

# --- THE PASSWORD SECTION ---
st.write("### Wait a second...")
st.write("but first what is a date have big meaning for us, yeah the one i forget some times, Ehmmm so many times 😂")

# The input box for her to type the date
secret_date = st.text_input("Enter the date (Format: DD/MM/YYYY):", type="password")

# --- WHAT HAPPENS WHEN SHE GETS IT RIGHT ---
# Checking for both 26/2/2024 and 26/02/2024 just to be safe!
if secret_date in ["26/2/2024", "26/02/2024"]:
    st.success("برااااافو على فكرة انا كمان مبنساهوش لعلمك❤️")
    st.balloons()
    
    st.write("---")
    
    # --- THE PHOTO BLOCK ---
# --- THE PHOTO BLOCK ---
    st.write("### Our Favorite Moments")
    
    # Photo 1
    st.image("specialstart.jpeg", use_container_width=True)
    st.markdown(
        "<h4 style='text-align: center; color: #ff4b4b; margin-top: 10px; margin-bottom: 40px;'>Special Start</h4>", 
        unsafe_allow_html=True
    )
    
    # Photo 2
    st.image("seniors.jpeg", use_container_width=True)
    st.markdown(
        "<h4 style='text-align: center; color: #ff4b4b; margin-top: 10px; margin-bottom: 40px;'>Seniorrrrs</h4>", 
        unsafe_allow_html=True
    )
    
    # Photo 3
    st.image("theyneverlie.jpeg", use_container_width=True)
    st.markdown(
        "<h4 style='text-align: center; color: #ff4b4b; margin-top: 10px; margin-bottom: 40px;'>They Never Lie</h4>", 
        unsafe_allow_html=True
    )

    # Photo 4
    st.image("smiley.jpeg", use_container_width=True)
    st.markdown(
        "<h4 style='text-align: center; color: #ff4b4b; margin-top: 10px; margin-bottom: 40px;'>ضحكة بسيطة خاااالص😇😇</h4>", 
        unsafe_allow_html=True
    )
    st.image("love.jpeg", use_container_width=True)
    st.markdown(
        "<h4 style='text-align: center; color: #ff4b4b; margin-top: 10px; margin-bottom: 40px;'>My Love My Love My Love</h4>", 
        unsafe_allow_html=True
    )
    st.image("doit.jpeg", use_container_width=True)
    st.markdown(
        "<h4 style='text-align: center; color: #ff4b4b; margin-top: 10px; margin-bottom: 40px;'>I'll Do It I'll Do It Inshallah</h4>", 
        unsafe_allow_html=True
    )

    st.image("heart.jpeg", use_container_width=True)
    st.markdown(
        "<h4 style='text-align: center; color: #ff4b4b; margin-top: 10px; margin-bottom: 40px;'>My Heart My Heart My Heart</h4>", 
        unsafe_allow_html=True
    )

    st.image("bald.jpeg", use_container_width=True)
    st.markdown(
        "<h4 style='text-align: center; color: #ff4b4b; margin-top: 10px; margin-bottom: 40px;'>حبيبك الأقرع</h4>", 
        unsafe_allow_html=True
    )

    st.image("baldlove.jpeg", use_container_width=True)
    st.markdown(
        "<h4 style='text-align: center; color: #ff4b4b; margin-top: 10px; margin-bottom: 40px;'>أتوقع بيحبو بعض</h4>", 
        unsafe_allow_html=True
    )
    # --- NEW CODE TO ADD THE NEXT PAGE BUTTON ---
    st.write("---") # Draws a nice line under the last photo
    
    st.markdown(
        """
        <div style='text-align: center; color: #7a0016; font-size: 22px; font-style: italic; font-family: "Georgia", serif; margin-bottom: 20px;'>
            Ready for the final surprise? 👀
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Centering the button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.page_link("pages/2_last.py", label="Click here for the finale ✨", icon="🎁")
    # ---------------------------------------------

    


    





# --- WHAT HAPPENS IF SHE GETS IT WRONG ---
elif secret_date != "":
    st.error("يعني نسيتيه وبتدايقي كمان اني بنساه الله")
