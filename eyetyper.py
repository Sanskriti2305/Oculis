import streamlit as st
from streamlit_webrtc import webrtc_streamer

# -------------------- APP FUNCTION --------------------
def app():
    st.set_page_config(page_title="EyeTyper", layout="wide")

    # ---------------- Styles ----------------
    st.markdown("""
    <style>
    /* Background image for entire app */
    .stApp {
        background-image: url('https://i.pinimg.com/1200x/a8/66/e7/a866e7bff2215fd41fb082313dd24565.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        font-family: 'Arial Black', Gadget, sans-serif;
    }

    /* Title style */
    #title {
        text-align: center;
        color: #FAD0C4;
        font-size: 60px;
        font-weight: bold;
        text-shadow: 4px 4px 10px #000000;
    }

    /* Text area style */
    .stTextArea>div>textarea {
        font-size: 30px;
        font-weight: bold;
        height: 120px;
        background-color: rgba(31,41,55,0.8);
        color: #FAD0C4;
        border-radius: 15px;
    }

    /* Button style */
    .stButton>button {
        height: 120px;
        width: 120px;
        margin: 5px;
        font-size: 32px;
        font-weight: bold;
        background-color: rgba(59,66,82,0.8);
        color: #FAD0C4;
        border-radius: 15px;
        text-shadow: 2px 2px 5px #000000;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: rgba(129,161,193,0.8);
        transform: scale(1.1);
    }

    /* Shift webcam slightly up */
    .webcam-container {
        position: absolute;   /* absolute positioning */
        top: 20px;            /* distance from top */
        right: 20px;          /* distance from right */
        width: 300px; 
    }
    </style>
    """, unsafe_allow_html=True)

    # ---------------- Title ----------------
    st.markdown('<div id="title">EyeTyper</div>', unsafe_allow_html=True)

    # ---------------- Session State ----------------
    if "text" not in st.session_state:
        st.session_state.text = ""

    # ---------------- Layout ----------------
    col1, col2 = st.columns([3,1])

    # Webcam column (slightly shifted)
   
    with col2:
        st.markdown("""
        <div style="display:flex; justify-content:flex-end; align-items:flex-start;">
        """, unsafe_allow_html=True)

        webrtc_streamer(key="example", media_stream_constraints={"video": True, "audio": False})

        st.markdown("</div>", unsafe_allow_html=True)

    # Keyboard and text column
    with col1:
        st.text_area("Typed Text", st.session_state.text, max_chars=None)

        # Keyboard layout
        keys_layout = [
            ["Q","W","E","R","T","Y","U","I","O","P"],
            ["A","S","D","F","G","H","J","K","L"],
            ["Z","X","C","V","B","N","M","←","Space","Clear"]
        ]

        # Render keys
        for row in keys_layout:
            cols = st.columns(len(row))
            for i, key in enumerate(row):
                if cols[i].button(key, key=f"btn_{key}"):
                    if key == "Space":
                        st.session_state.text += " "
                    elif key == "←":
                        st.session_state.text = st.session_state.text[:-1]
                    elif key == "Clear":
                        st.session_state.text = ""
                    else:
                        st.session_state.text += key

# -------------------- RUN APP --------------------
if __name__ == "__main__":
    app()
