import streamlit as st
import eyetyper
import sign_language

# ------------------ Page Config ------------------
st.set_page_config(page_title="Oculis", layout="wide")

# ------------------ Initialize Session State ------------------
if 'page' not in st.session_state:
    st.session_state.page = "main"

def go_to_eyetyper():
    st.session_state.page = "eyetyper"

def go_to_sign_language():
    st.session_state.page = "sign_language"

# ------------------ Custom CSS ------------------
st.markdown("""
<style>
/* RESET */
html, body, [class*="css"] {
    margin: 0;
    padding: 0;
    font-family: 'Poppins', sans-serif;
    overflow-x: hidden;
}

/* HIDE DEFAULT HEADER/FOOTER */
header, footer {visibility: hidden;}

/* NAVBAR */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 60px;
    background: #1a1a1a;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 5%;
    z-index: 10;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);       
    font-family: 'Bebas Neue', 'Montserrat', sans-serif;
    font-size: 3rem;
    color: #dfc5fe;
    text-shadow: 
        2px 2px 0 #000,
        4px 4px 10px rgba(0,0,0,0.3),
        0 0 20px rgba(255,111,97,0.5);
    letter-spacing: 2px;
}

.navbar h1 {
    font-size: 2rem;
}

/* SECTION 1 */
.section1 {
    background-color: #111;
    color: white;
    display: flex;
    justify-content: space-between;
    padding: 80px 10%;
    position: relative;
    z-index: 5; /* ensures buttons clickable */
}

.left-content {
    max-width: 45%;
}

.left-content h1 {
    font-size: 3rem;
    font-weight: 700;
}

.left-content p {
    margin-top: 1rem;
    font-size: 1rem;
    color: #aaa;
}

.btn-container {
    margin-top: 1rem;
    position: relative;
    z-index: 10; /* ensures buttons above overlays */
}

.btn-primary {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 12px 22px;
    border-radius: 8px;
    cursor: pointer;
    margin-right: 10px;
}

.btn-secondary {
    background-color: #000;
    color: white;
    border: 1px solid #555;
    padding: 12px 22px;
    border-radius: 8px;
    cursor: pointer;
}

/* Illustration */
.illustration img {
    width: 90%;
    max-width: 420px;
}

/* SECTION 2 - SPLIT */
.section2 {
    display: flex;
    height: 100vh;
    width: 100%;
    position: relative;
    gap: 10px;
    margin-top: 50px;
}

.split-left, .split-right {
    flex: 1;
    background-size: cover;
    background-position: center;
    position: relative;
    border: 4px solid rgba(223,197,254,0.7);
    border-radius: 12px;
    transition: all 0.3s ease;
    z-index: 2;
}

.split-left:hover, .split-right:hover {
    box-shadow: 0 0 30px rgba(223,197,254,0.8);
    transform: scale(1.02);
}

.split-left {
    background-image: url('https://i.pinimg.com/736x/bf/d7/42/bfd742154476f9fba8fdb0a1e7af6554.jpg');
}

.split-right {
    background-image: url('https://i.pinimg.com/736x/b4/e4/9e/b4e49ef7346393e499076427503ad62b.jpg');
}

/* Split-text overlay */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');

.split-text {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    align-items: stretch;
    justify-content: stretch;
    z-index: 1; /* keep below buttons */
    font-family: 'Playfair Display', serif; 
    font-weight: 700;
    color: #f5ecd3;
    text-shadow: 3px 3px 12px rgba(0,0,0,0.7);
    pointer-events: none; /* allow clicks through */
}

.split-text div {
    font-size: 3rem;
    display: flex;
}

.split-text div:first-child {
    justify-content: flex-start;
    align-items: flex-end;
    padding: 20px;
}

.split-text div:last-child {
    justify-content: flex-end;
    align-items: flex-start;
    padding: 20px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ NAVBAR ------------------
st.markdown("""
<div class="navbar">
    <h1>Oculis</h1>
</div>
""", unsafe_allow_html=True)

# ------------------ MAIN PAGE ------------------
if st.session_state.page == "main":

    # SECTION 1
    st.markdown("""
    <div class="section section1">
        <div class="left-content">
            <p style="color:#bbb; font-size:1.4rem;">GAZE. SPEAK. EXPRESS.</p>
            <h1>Empowering<br>Communication<br>for Everyone.</h1>
            <p>Discover tools that bridge the gap.</p>
            <div class="btn-container">
                <button class="btn-primary" onclick="document.location.reload();">Try Voice to Sign</button>
                <button class="btn-secondary" onclick="document.location.reload();">Explore EyeTyper</button>
            </div>
        </div>
        <div class="illustration">
            <img src="https://i.pinimg.com/736x/1c/9f/a2/1c9fa2074c337575273bae1daf800442.jpg" alt="Illustration">
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Native Streamlit buttons to switch pages
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Try Voice to Sign"):
            go_to_sign_language()
    with col2:
        if st.button("Explore EyeTyper"):
            go_to_eyetyper()

    # SECTION 2 - SPLIT
    st.markdown("""
    <div class="section section2">
        <div class="split-left"></div>
        <div class="split-right"></div>
        <div class="split-text">
            <div>Voice to Sign Language</div>
            <div>EyeTyper</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------ EYE TYPER PAGE ------------------
elif st.session_state.page == "eyetyper":
    eyetyper.app()
    if st.button("Back to Main"):
        st.session_state.page = "main"

# ------------------ SIGN LANGUAGE PAGE ------------------
elif st.session_state.page == "sign_language":
    sign_language.app()
    if st.button("Back to Main"):
        st.session_state.page = "main"
