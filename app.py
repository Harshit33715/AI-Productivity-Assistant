"""
Project 5 - AI Productivity Assistant
Combines multiple AI capabilities into one Streamlit application.

Run with:  streamlit run app.py
Requires:  pip install streamlit google-generativeai
"""

import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Productivity Assistant", page_icon="🚀", layout="wide")

st.sidebar.title("⚙️ Settings")
api_key = st.sidebar.text_input("Enter your Gemini API Key", type="password")
st.sidebar.caption("Get a free key at aistudio.google.com/apikey")

st.title("🚀 AI Productivity Assistant")


def run_gemini(prompt: str) -> str:
    if not api_key:
        return "⚠️ Please enter your Gemini API key in the sidebar."
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-flash-latest")
        return model.generate_content(prompt).text
    except Exception as e:
        return f"⚠️ Error: {e}"


tabs = st.tabs([
    "📋 Meeting Notes",
    "✅ Action Items",
    "✉️ Rewrite Email",
    "🖥️ Presentation Outline",
    "💼 LinkedIn Post",
    "💡 Brainstorm",
    "🌐 Translate",
    "📚 Study Notes",
])

# 1. Summarize meeting notes
with tabs[0]:
    st.subheader("Summarize Meeting Notes")
    notes = st.text_area("Paste raw meeting notes / transcript", height=200, key="notes_in")
    if st.button("Summarize", key="summarize_btn"):
        result = run_gemini(f"Summarize these meeting notes into clear, concise bullet points:\n\n{notes}")
        st.markdown(result)

# 2. Generate action items
with tabs[1]:
    st.subheader("Generate Action Items")
    notes2 = st.text_area("Paste meeting notes / discussion", height=200, key="action_in")
    if st.button("Generate Action Items", key="action_btn"):
        result = run_gemini(
            f"Extract clear action items from these notes. For each, list: Task, Owner (if mentioned), Deadline (if mentioned).\n\n{notes2}"
        )
        st.markdown(result)

# 3. Rewrite emails
with tabs[2]:
    st.subheader("Rewrite an Email")
    email_in = st.text_area("Paste your draft email", height=150, key="email_in")
    style = st.selectbox("Rewrite style", ["More Professional", "More Friendly", "More Concise", "More Assertive"])
    if st.button("Rewrite", key="email_btn"):
        result = run_gemini(f"Rewrite this email to be {style.lower()}. Keep the core message intact:\n\n{email_in}")
        st.markdown(result)

# 4. Presentation outlines
with tabs[3]:
    st.subheader("Create a Presentation Outline")
    topic = st.text_input("Presentation topic", key="ppt_topic")
    slides = st.slider("Number of slides", 3, 15, 8)
    if st.button("Generate Outline", key="ppt_btn"):
        result = run_gemini(f"Create a {slides}-slide presentation outline on '{topic}'. For each slide give a title and 3 bullet points.")
        st.markdown(result)
        st.caption("Tip: paste this into Gamma AI or Canva AI to generate the visual deck.")

# 5. LinkedIn posts
with tabs[4]:
    st.subheader("Generate a LinkedIn Post")
    li_topic = st.text_input("Topic", key="li_topic")
    if st.button("Generate Post", key="li_btn"):
        result = run_gemini(f"You are a professional LinkedIn writer. Write an engaging LinkedIn post about: {li_topic}")
        st.markdown(result)

# 6. Brainstorm
with tabs[5]:
    st.subheader("Brainstorm Ideas")
    brainstorm_topic = st.text_input("What do you need ideas for?", key="brain_topic")
    n_ideas = st.slider("Number of ideas", 3, 20, 10)
    if st.button("Brainstorm", key="brain_btn"):
        result = run_gemini(f"Brainstorm {n_ideas} creative ideas for: {brainstorm_topic}")
        st.markdown(result)

# 7. Translate text
with tabs[6]:
    st.subheader("Translate Text")
    text_in = st.text_area("Text to translate", height=150, key="translate_in")
    target_lang = st.text_input("Target language", value="Hindi", key="translate_lang")
    if st.button("Translate", key="translate_btn"):
        result = run_gemini(f"Translate the following text into {target_lang}, preserving tone and meaning:\n\n{text_in}")
        st.markdown(result)

# 8. Study notes
with tabs[7]:
    st.subheader("Create Study Notes")
    study_topic = st.text_area("Paste content or enter a topic to study", height=150, key="study_in")
    if st.button("Create Study Notes", key="study_btn"):
        result = run_gemini(f"Turn this into well-organized study notes with headings, bullet points, and a short summary at the end:\n\n{study_topic}")
        st.markdown(result)

st.markdown("---")
st.caption(
    "Extension ideas: connect Otter AI for meeting transcription, "
    "Gamma/Canva AI for visual slides, and n8n to auto-send summaries by email or social platforms."
)
