News Sentiment Analysis Tool
A web-based application built with Streamlit that fetches, analyzes, and summarizes news articles related to a given company, providing sentiment analysis and topic extraction. Additionally, it converts the final sentiment analysis result into Hindi audio using gTTS.

Features
✅ Fetches real-time news related to a company.
✅ Performs sentiment analysis on the fetched articles.
✅ Extracts key topics and generates comparative sentiment scores.
✅ Provides a detailed breakdown of sentiment distribution and topic overlap.
✅ Converts final sentiment analysis into Hindi audio using Google Text-to-Speech (gTTS).

Tech Stack
Frontend: Streamlit

Backend API: Hosted on Hugging Face Spaces

Libraries Used:

streamlit – for UI

requests – for API communication

translate – for text translation

gtts – for text-to-speech conversion

Installation
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/news-sentiment-analysis.git
cd news-sentiment-analysis
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Application
bash
Copy
Edit
streamlit run app.py
How It Works
1️⃣ User inputs a company name.
2️⃣ App fetches the latest news articles related to the company via API.
3️⃣ Sentiment analysis is performed on the news articles.
4️⃣ Topics are extracted and a comparative sentiment score is generated.
5️⃣ The final sentiment analysis is converted into Hindi audio.
6️⃣ Users can listen to the sentiment summary.

API Endpoints Used
/extract_news → Fetches news articles for the given company.

/analyze_articles → Analyzes sentiment and topics from the articles.

Example Usage
Input: Tesla

Output:

Latest news articles about Tesla.

Sentiment analysis (Positive/Negative/Neutral).

Topic extraction.

Audio output summarizing the sentiment in Hindi.



Future Enhancements
📌 Add support for multiple languages for sentiment translation.
📌 Improve sentiment accuracy using deep learning models.
📌 Enhance news extraction using multiple APIs (Google News, Bing News, etc.).


Contributors
Yarrapothu Sai Chandu (https://github.com/YSChandu)
