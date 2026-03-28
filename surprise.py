import streamlit as st

import streamlit as st

st.set_page_config(page_title="Happy Birthday Rony!", page_icon="❤️", layout="centered")

# --- BACKGROUND COLOR CODE ---
page_bg_color = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom right, #ffdde1, #ee9ca7); /* Soft pink gradient */
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0); /* Makes the top header bar transparent */
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)
# -----------------------------

# ... (The rest of your big text and buttons go here) ...

# Sets up the tab name and icon
st.set_page_config(page_title="Happy Birthday Rony!", page_icon="❤️", layout="centered")

# The big text with a little bit of HTML to center it and make it pop
st.markdown(
    """
    <h1 style='text-align: center; color: #ffffff;'>
        Happy birthday to the most beautiful girl in the world <br><br>
        My Beautiful Rony ❤️🎉
    </h1>
    """, 
    unsafe_allow_html=True
)

st.write("") # Just adds a little blank space for layout
st.write("")

# 1. We create a "memory" so the app remembers she opened her gift
if "present_opened" not in st.session_state:
    st.session_state.present_opened = False

# 2. The first button she clicks
# Using columns just to center the button on the screen nicely
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Click here for ur present 🎁", use_container_width=True):
        st.session_state.present_opened = True
        st.balloons() # Triggers the celebration animation!
        

# 3. What happens AFTER she clicks the button
if st.session_state.present_opened:
    st.write("---") # Draws a nice dividing line
    
    # PUT YOUR CUSTOM MESSAGE HERE
    # THE ROMANTIC MESSAGE
    st.markdown(
        """
        <div style='text-align: center; color: #7a0016; font-size: 26px; font-weight: bold; line-height: 2;'>
            كل سنة وانتي طيبة يا روحي ❤️<br>
            انا بحبك اوي اوي اوي اوي يا روحي<br>
            يا احلى روني في الدنيا<br>
            بموت فيكي اوي اوي اوي<br>           
            ربنا يخليكي ليا ياروحي و يجمعنا على خير يارب ✨
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    st.write("---")
    
# 4. The elegant transition text
    st.markdown(
        """
        <div style='text-align: center; color: #7a0016; font-size: 22px; font-style: italic; font-family: "Georgia", serif; margin-bottom: 20px;'>
            But wait, there's more...<br>
            تعالي نتفرج على كان حاجة جميلة
        </div>
        """, 
        unsafe_allow_html=True
    )
    
    # Centering the page link button using columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.page_link("pages/1_Memory_Lane.py", label="Have a look 😉", icon="📸")
