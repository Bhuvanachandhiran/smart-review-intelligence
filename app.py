import streamlit as st
from nlp_pipeline import ReviewAnalyzer

st.set_page_config(page_title="Smart Review AI", layout="centered")

st.title("🧠 Smart Review Intelligence System")
st.write("Analyze sentiment, emotion, and key entities from text.")

analyzer = ReviewAnalyzer()

user_text = st.text_area(
    "Enter a customer review:",
    height=150,
    placeholder="The phone camera is amazing but the battery is terrible..."
)

if st.button("Analyze Review"):
    if user_text.strip():
        result = analyzer.analyze(user_text)

        st.subheader("📊 Sentiment")
        st.write(
            f"**{result['sentiment']['label']}** "
            f"(confidence: {result['sentiment']['score']:.2f})"
        )

        st.subheader("🎭 Emotion")
        st.write(
            f"**{result['emotion']['label']}** "
            f"(confidence: {result['emotion']['score']:.2f})"
        )

        st.subheader("🏷️ Named Entities")
        if result["entities"]:
            for ent in result["entities"]:
                st.write(f"- `{ent['text']}` → {ent['label']}")
        else:
            st.write("No named entities detected.")
    else:
        st.warning("Please enter some text.")
