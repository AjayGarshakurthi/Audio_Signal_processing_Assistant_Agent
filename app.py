import streamlit as st
from ibm_watsonx_orchestrate_sdk.langchain import ChatWxO

# -------------------------
# Secrets
# -------------------------

API_KEY = st.secrets["API_KEY"]
INSTANCE_URL = st.secrets["INSTANCE_URL"]
MODEL = "groq/openai/gpt-oss-120b"

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="Audio Signal Processing Assistant",
    page_icon="🎧",
    layout="wide"
)

# -------------------------
# CSS
# -------------------------

st.markdown("""
<style>

.stApp{
    background:#0e1117;
}

.main-title{
    text-align:center;
    color:white;
    font-size:38px;
    font-weight:bold;
}

.sub{
    text-align:center;
    color:#A9A9A9;
    margin-bottom:30px;
}

.user{
    background:#1f6feb;
    padding:15px;
    border-radius:12px;
    color:white;
    margin-bottom:10px;
}

.bot{
    background:#262730;
    padding:15px;
    border-radius:12px;
    color:white;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🎧 Audio Signal Processing Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='sub'>Powered by IBM watsonx Orchestrate • GPT-OSS 120B</div>", unsafe_allow_html=True)

# -------------------------
# Debug (Remove Later)
# -------------------------

st.sidebar.write("Python OK")
st.sidebar.write(f"URL Loaded: {bool(INSTANCE_URL)}")
st.sidebar.write(f"API Loaded: {bool(API_KEY)}")

# -------------------------
# Load Model
# -------------------------

@st.cache_resource
def load_model():
    return ChatWxO.from_instance_credentials(
        instance_url=INSTANCE_URL,
        api_key=API_KEY,
        auth_type="ibm_iam",
        model=MODEL,
        temperature=0.2,
        max_tokens=1000,
    )

try:
    llm = load_model()
except Exception as e:
    st.error(f"Authentication Error:\n\n{e}")
    st.stop()

# -------------------------
# Session State
# -------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# Sidebar
# -------------------------

with st.sidebar:

    st.title("⚙ Controls")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("### Suggested Questions")

    suggestions = [
        "What is an operational amplifier?",
        "Explain low-pass filter.",
        "Difference between FIR and IIR filter.",
        "What is aliasing?",
        "Explain sampling theorem."
    ]

    for q in suggestions:
        if st.button(q):
            st.session_state.prompt = q

# -------------------------
# Chat History
# -------------------------

for msg in st.session_state.messages:

    if msg["role"] == "user":
        st.markdown(
            f"<div class='user'><b>👤 You</b><br>{msg['content']}</div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"<div class='bot'><b>🤖 Assistant</b><br>{msg['content']}</div>",
            unsafe_allow_html=True,
        )

# -------------------------
# Input
# -------------------------

default = ""

if "prompt" in st.session_state:
    default = st.session_state.prompt
    del st.session_state.prompt

prompt = st.chat_input("Ask anything about Audio Signal Processing...")

if default and not prompt:
    prompt = default

# -------------------------
# Ask Model
# -------------------------

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    st.markdown(
        f"<div class='user'><b>👤 You</b><br>{prompt}</div>",
        unsafe_allow_html=True,
    )

    with st.spinner("Thinking..."):

        try:
            response = llm.invoke(prompt)
            answer = response.content
        except Exception as e:
            answer = str(e)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.markdown(
        f"<div class='bot'><b>🤖 Assistant</b><br>{answer}</div>",
        unsafe_allow_html=True,
    )
