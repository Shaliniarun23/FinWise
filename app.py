import streamlit as st

# Page configuration
st.set_page_config(
    page_title="FinWise - Smart Money, Smart Kids",
    page_icon="💸",
    layout="wide"
)

# Background image styling
page_bg_img = '''
<style>
.stApp {
background-image: url("https://images.unsplash.com/photo-1605902711622-cfb43c4437d5");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
}
.title-box {
background-color: rgba(255, 255, 255, 0.85);
padding: 2em;
border-radius: 10px;
margin-top: 2em;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title Box
st.markdown('<div class="title-box">', unsafe_allow_html=True)
st.title("💡 Welcome to FinWise")
st.subheader("UAE’s AI-Powered, Gamified Financial Literacy Platform for Students (Ages 10–18)")
st.write("Empowering youth through stories, challenges, and ethical AI.")
st.markdown('</div>', unsafe_allow_html=True)

# Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎮 Start Game Journey"):
        st.write("🚀 Redirecting to Level Selection...")

with col2:
    if st.button("📊 Parent Dashboard"):
        st.write("🔒 Feature Coming Soon...")

with col3:
    if st.button("🏫 Teacher Toolkit"):
        st.write("🛠️ Under Construction...")

st.markdown("---")
st.markdown("### ✨ Built with love, ethics, and AI — powered by Intel & Streamlit")

