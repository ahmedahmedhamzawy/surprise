import streamlit as st

# Setup the final page
st.set_page_config(page_title="The Grand Finale", page_icon="💝", layout="centered")

# --- BACKGROUND COLOR CODE (Keeping it consistent!) ---
page_bg_color = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(to bottom right, #ffdde1, #ee9ca7);
}
[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# --- BIG "HELLO HONEY" HEADER ---
st.markdown(
    """
    <div style='text-align: center; color: #7a0016; font-size: 55px; font-weight: bold; font-family: "Georgia", serif; margin-top: 30px; margin-bottom: 30px;'>
        Hello Honey ❤️
    </div>
    """, 
    unsafe_allow_html=True
)

st.write("---") # A nice elegant divider line

# --- THE FINAL PARAGRAPH ---
st.markdown(
    """
    <div style='text-align: center; color: #7a0016; font-size: 24px; line-height: 2; font-family: "Georgia", serif; margin-bottom: 40px;'>
        انا بحبك اوي اوي اوي اوي يا روحي <br>
        بموت فيكي اوي اوي اوي اوي يا احلى روني <br>
        يا رب السنة الجاية نكون سوا يارب و نحتفل بيه سوا😇 <br>
        Thats all for now  Honey <br>
        may i have some new surprises for my love next time😉
    </div>
    """, 
    unsafe_allow_html=True
)

# --- THE GRAND FINALE BUTTON ---
st.write("")
st.write("")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Happy Birthday Rony! 🎉", use_container_width=True):
        st.balloons()
        st.snow() # Triggers both for a massive screen celebration!
        st.success("I love you!")