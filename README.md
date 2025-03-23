
# News Summarization & Hindi TTS - Documentation

## Project Overview
This project is designed to extract news articles related to a given company, summarize them, analyze their sentiment, translate the summary into Hindi, and generate a Hindi text-to-speech (TTS) output. The application is built using Streamlit for the frontend, with various NLP techniques implemented in the backend.

## Features
- Fetches latest news articles using NewsAPI
- Summarizes the extracted news content
- Performs sentiment analysis on summarized text
- Translates the summary into Hindi
- Converts the Hindi summary to speech using Google TTS
- Provides an interactive UI using Streamlit

## Tech Stack
- **Frontend:** Streamlit
- **Backend:** Python (Flask APIs, NLP models)
- **APIs:** NewsAPI for fetching news articles
- **Libraries Used:**
  - `requests` for API calls
  - `nltk` for sentiment analysis
  - `transformers` for text summarization
  - `googletrans` for language translation
  - `gTTS` for text-to-speech
  - `beautifulsoup4` for web scraping (if required later)

## Installation & Setup
### 1. Clone the Repository
```bash
git clone https://github.com/your-repository-link.git
cd news-summarization-hindi-tts
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

## Code Structure
```plaintext
news-summarization-hindi-tts/
│── api.py                   # Fetches news articles using NewsAPI
│── utils.py                 # Contains summarization, sentiment analysis, translation, and TTS functions
│── app.py                   # Streamlit frontend application
│── requirements.txt         # List of required dependencies
│── README.md                # Documentation
```

## API Endpoints
### 1. Fetch News
- **Endpoint:** `fetch_news(company_name)`
- **Description:** Fetches latest 5 news articles about the given company.
- **Response Format:**
```json
[
  {
    "title": "Article Title",
    "url": "https://example.com",
    "summary": "Short summary of the article."
  }
]
```

### 2. Summarization
- **Function:** `summarize_text(text)`
- **Description:** Summarizes the input text using a Hugging Face transformer model.
- **Returns:** Shortened summary of the input text.

### 3. Sentiment Analysis
- **Function:** `analyze_sentiment(text)`
- **Description:** Uses NLTK's VADER sentiment analysis to classify text as Positive, Neutral, or Negative.
- **Returns:** Sentiment category and sentiment score.

### 4. Hindi Translation
- **Function:** `translate_to_hindi(text)`
- **Description:** Translates the given text from English to Hindi using Google Translate API.
- **Returns:** Hindi-translated text.

### 5. Text-to-Speech (TTS)
- **Function:** `text_to_speech_google(text, filename="news_summary.mp3")`
- **Description:** Converts Hindi text into a speech audio file.
- **Returns:** Filename of the generated MP3 file.

## Deployment Plan
1. **Local Testing:** Ensure all functionalities work as expected.
2. **Containerization (Optional):** Use Docker to package the application.
3. **Deployment on Hugging Face Spaces:**
   - Push code to GitHub
   - Deploy using Hugging Face Spaces
   - Test and verify

## Future Improvements
- Support for multiple languages
- Improved summarization with fine-tuned models
- Enhanced sentiment analysis with deep learning models
- Integration with real-time news sources




