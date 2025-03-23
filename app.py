import streamlit as st
import os
from api import fetch_news
from utils import summarize_text, analyze_sentiment, translate_to_hindi, text_to_speech_google

# Streamlit UI
st.set_page_config(page_title="News Summarization & Hindi TTS", layout="wide")

st.title("📰 News Summarization & Hindi TTS")

# User input
company = st.text_input("Enter Company Name", "Tesla")

if st.button("Fetch News"):
    with st.spinner("Fetching latest news..."):
        articles = fetch_news(company)

    if not articles:
        st.error("❌ No news found! Try another keyword.")
    else:
        st.success(f"✅ Found {len(articles)} news articles on **{company}**.")

        summaries = []
        col1, col2 = st.columns(2)  # Divide UI into two columns

        for i, article in enumerate(articles, 1):
            with col1:
                st.subheader(f"{i}. {article['title']}")
                st.write(f"[Read More]({article['url']})")

            summary = summarize_text(article['summary'])
            sentiment, score = analyze_sentiment(summary)
            hindi_summary = translate_to_hindi(summary)

            with col2:
                st.write(f"📌 **Summary:** {summary}")
                st.write(f"🔹 **Sentiment:** {sentiment} (Score: {score})")
                st.write(f"🌍 **Hindi Summary:** {hindi_summary}")

            summaries.append(f"{i}. {hindi_summary}")

        # Convert to speech
        final_text = "\n".join(summaries)
        audio_file = text_to_speech_google(final_text)

        st.audio(audio_file, format="audio/mp3", start_time=0)
        with open(audio_file, "rb") as f:
            st.download_button("⬇ Download Hindi Audio", f, file_name="news_summary.mp3")

        # Cleanup after playing
        os.remove(audio_file)
