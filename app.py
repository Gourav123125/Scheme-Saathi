import streamlit as st
from utils import extract_profile
from matcher import match_schemes

st.set_page_config(
    page_title="Scheme Sathi",
    page_icon="icon.png"
)
st.markdown("""
<style>

/* FULL PAGE BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #eef2ff 0%, #f9fafb 100%);
}

/* MAIN CONTAINER */
[data-testid="stAppViewContainer"] {
    background: transparent;
}

/* CONTENT AREA */
[data-testid="stMain"] {
    background: transparent;
}

/* HERO SECTION */
.hero {
    background: linear-gradient(135deg, #4f46e5, #6366f1);
    padding: 32px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 30px;
}

/* CARDS */
.card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}

/* BUTTON */
button[kind="primary"] {
    background: linear-gradient(135deg, #4f46e5, #6366f1);
    border-radius: 14px;
    height: 48px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero">
<h1>🤝 Scheme Saathi</h1>
<p>Find government welfare schemes you may be eligible for</p>
</div>
""", unsafe_allow_html=True)

user_input = st.text_area(
    "Tell us about yourself",
)

if st.button("🔍 Find Eligible Schemes", use_container_width=True):
    profile = extract_profile(user_input)
    results = match_schemes(profile)

    if not results:
        st.error("No schemes matched your details.")
    else:
        for scheme in results:
            st.markdown(f"""
            <div class="card">
            <h4>🔹 {scheme['name']}</h4>
            <p><b>Benefit:</b> {scheme['benefit']}</p>
            <a href="{scheme['link']}" target="_blank">Apply / Learn More</a>
            </div>
            """, unsafe_allow_html=True)
