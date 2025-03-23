import streamlit as st
import requests
from translate import Translator
from gtts import gTTS
import os

# Define API endpoint URL (replace with your actual URL)
API_URL = "https://chandu24-yt-newspulse-backend.hf.space/"  # Change if your API is running elsewhere

# Function for text-to-speech conversion
def text_to_speech_hindi(text):
    translator = Translator(to_lang="hi")
    hindi_text = translator.translate(text)

    tts = gTTS(text=hindi_text, lang='hi')
    tts.save("output.mp3")

def main():
    st.title("News Sentiment Analysis Tool")
    company_name = st.text_input("Enter Company Name")

    if st.button("Fetch News & Analyze"):
        try:
            # 1. Fetch News from API
            news_url = f"{API_URL}/extract_news?company_name={company_name}"
            news_response = requests.get(news_url)
            news_response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            articles = news_response.json()

            # 2. Analyze Articles via API
            analysis_url = f"{API_URL}/analyze_articles"
            analysis_response = requests.post(analysis_url, json=articles)
            analysis_response.raise_for_status()
            output_data = analysis_response.json()

            # 3. Display Results
            st.write("## Analysis Results")

            # Display articles
            st.write("### Articles:")
            for i, article in enumerate(output_data["Articles"], 1):
                st.write(f"#### Article {i}:")
                st.write(f"Title: {article.get('title', 'No Title Found')}")  # Corrected: 'Title'
                st.write(f"Link: {article['link']}")
                st.write(f"Summary: {article['summary']}")
                st.write(f"Sentiment: {article['Sentiment']}")
                st.write(f"Topics: {', '.join(article['Topics'])}")
                st.write("")

            # Display Comparative Sentiment Score
            st.write("### Comparative Sentiment Score:")
            st.write(f"Sentiment Distribution: {output_data['Comparative Sentiment Score']['Sentiment Distribution']}")
            st.write("#### Coverage Differences:")
            for comparison in output_data['Comparative Sentiment Score']['Coverage Differences']:
                st.write(f"- Comparison: {comparison['Comparison']}")
                st.write(f"- Impact: {comparison['Impact']}")

            st.write("#### Topic Overlap:")
            st.write(f"Common Topics: {output_data['Comparative Sentiment Score']['Topic Overlap']['Common Topics']}")
            st.write(f"Unique Topics: {output_data['Comparative Sentiment Score']['Topic Overlap']['Unique Topics']}")

            # Display Final Sentiment Analysis
            st.write(f"### Final Sentiment Analysis: {output_data['Final Sentiment Analysis']}")

            # Convert Final Sentiment to Audio
            text_to_speech_hindi(output_data['Final Sentiment Analysis'])  # Use the analysis result

            st.audio("output.mp3")

        except requests.exceptions.RequestException as e:
            st.error(f"Error communicating with the API: {e}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()