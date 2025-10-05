import streamlit as st
from PIL import Image
import os
import random

def app():  # <- wrap all code inside this function
    # ---------------- Session State Initialization ----------------
    if "text_input" not in st.session_state:
        st.session_state.text_input = ""
    if "displayed_text" not in st.session_state:
        st.session_state.displayed_text = ""
    if "current_gesture_images" not in st.session_state:
        st.session_state.current_gesture_images = []

    # ---------------- Gesture folder ----------------
    GESTURE_FOLDER = "gesture"

    # ---------------- Function to get gesture images for a word ----------------
    def get_gesture_images(word):
        images = []
        for char in word.upper():
            char_folder = os.path.join(GESTURE_FOLDER, char)
            if os.path.exists(char_folder):
                imgs_list = [f for f in os.listdir(char_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
                if imgs_list:
                    img_path = os.path.join(char_folder, random.choice(imgs_list))
                    try:
                        images.append(Image.open(img_path))
                    except:
                        continue
        return images

    # ---------------- Background and container ----------------
    BACKGROUND_URL = "https://i.pinimg.com/1200x/05/fc/16/05fc162b9f326f7b0f5e260e342b84a7.jpg"
    st.markdown(f"""
    <div style="
        background-image: url('{BACKGROUND_URL}');
        background-size: cover;
        background-position: center;
        padding: 20px;
        border-radius: 15px;
    ">
    """, unsafe_allow_html=True)

    # ---------------- Custom CSS ----------------
    st.markdown("""
    <style>
    h1 {
        font-size:2.5rem; 
        font-weight:bold; 
        background: linear-gradient(90deg,#dfc5fe,#ff6f61); 
        -webkit-background-clip:text; 
        -webkit-text-fill-color:transparent; 
        margin-bottom:0.5rem;
    }
    .stButton>button {
        background: linear-gradient(90deg,#dfc5fe,#ff6f61); 
        color:white; 
        border-radius:10px; 
        padding:12px 24px; 
        font-weight:bold; 
        margin:5px;
    }
    .stButton>button:hover { transform: scale(1.05); }
    .stTextArea>div>textarea { font-size:20px; height:100px; border-radius:15px; }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- Layout ----------------
    st.markdown("<h1>🤟 Voice-to-Sign Language</h1>", unsafe_allow_html=True)
    st.markdown("Convert speech or text into sign language gestures")
    st.markdown("---")

    col1, col2 = st.columns([1,1], gap="large")

    # --- Input column ---
    with col1:
        st.markdown("### 🎤 Input")
        text_input = st.text_area("Type your message:", st.session_state.text_input, height=120)

        if st.button("🤟 Convert to Sign"):
            st.session_state.text_input = text_input.strip()
            if st.session_state.text_input:
                st.session_state.current_gesture_images = get_gesture_images(st.session_state.text_input)
                st.session_state.displayed_text = st.session_state.text_input
            else:
                st.session_state.current_gesture_images = []

    # --- Gesture display column ---
    with col2:
        st.markdown("### 🤟 Sign Display")
        if st.session_state.current_gesture_images:
            st.markdown('<div style="display:flex; flex-wrap:wrap; gap:10px; overflow-x:auto;">', unsafe_allow_html=True)
            for img in st.session_state.current_gesture_images:
                st.image(img, width=150)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.markdown("Gestures will appear here")

    # --- Quick Reference ---
    st.markdown("---")
    st.markdown("### 📖 Quick Reference (example letters)")
    cols = st.columns(6)
    example_letters = ['A','B','C','1','2','3']
    for idx, letter in enumerate(example_letters):
        with cols[idx % 6]:
            images = get_gesture_images(letter)
            if images:
                st.image(images[0], width=100)
            st.markdown(f"**{letter}**")

    # ---------------- Close background div ----------------
    st.markdown("</div>", unsafe_allow_html=True)
