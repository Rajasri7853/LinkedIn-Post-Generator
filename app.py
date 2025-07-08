import streamlit as st
import google.generativeai as genai

# Replace with your actual API key
GOOGLE_API_KEY = "your_api_key_here"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="LinkedIn Post Generator", layout="centered")
st.title("📝 LinkedIn Post Generator")
st.write("Give your bullet points and tone. Get a polished LinkedIn post using Gemini AI!")

bullet_points = st.text_area("Enter your bullet-point ideas (one per line)", height=200)
tone = st.selectbox("Choose Tone", ["Professional", "Casual"])

if st.button("Generate Post"):
    if bullet_points.strip():
        with st.spinner("Generating post..."):
            prompt = f"""
You're a skilled LinkedIn content writer.
Write a {tone.lower()} LinkedIn post using the following bullet points.
Make it natural, well-structured, and include 3-5 relevant hashtags.

Bullet Points:
{bullet_points}
"""
            try:
                response = model.generate_content(prompt)
                st.success("Here's your LinkedIn post:")
                st.text_area("Generated Post", value=response.text, height=300)
            except Exception as e:
                st.error(f"Gemini API Error: {str(e)}")
    else:
        st.warning("Please enter bullet points before generating.")
