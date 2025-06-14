import streamlit as st
from inference import get_model_response
from text_cleaning import remove_think_block, prettify_bullet_points
from utils import normalize_numbered_list
from data_structuring import markdown_to_json
import json

st.set_page_config(page_title="AI-Powered Advice", layout="centered")
st.title("💡 Ask AI: Smart Bullet-Pointed Answers")

# Inputs
api_key = st.text_input("🔐 Enter your Hugging Face API Key:", type="password")
query = st.text_area("📝 Enter your question:", placeholder="e.g., What are the best ways to make money online in Ghana?")

# Submission
if st.button("Submit", key="submit_btn") and api_key and query:
    try:
        raw_response = get_model_response(query, api_key)
        clean_response = remove_think_block(raw_response)
        pretty_response = prettify_bullet_points(clean_response)
        normalized = normalize_numbered_list(pretty_response)
        data = markdown_to_json(normalized)

        st.success("✅ Response Received!")

        st.subheader("📋 Cleaned Response")
        st.markdown(normalized)

        st.subheader("🧾 JSON Format")
        st.json(data)

    except Exception as e:
        st.error(f"🚫 Error: {e}")

elif st.button("Submit", key="submit_btn_alt"):
    st.warning("⚠️ Please enter both an API key and a question.")
