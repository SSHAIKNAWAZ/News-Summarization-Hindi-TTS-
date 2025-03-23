
# News Summarization & Hindi TTS - Documentation

## Project Overview
This project is designed to extract news articles related to a given company, summarize them, analyze their sentiment, translate the summary into Hindi, and generate a Hindi text-to-speech (TTS) output. The application is built using Streamlit for the frontend, with various NLP techniques implemented in the backend.

## Features
- Fetches latest news articles using NewsAPI
- Summarizes the extracted news content
- Performs sentiment analysis on summarized text
- Extracts key topics from the summary
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
  - `keybert` for key topic extraction
  - `googletrans` for language translation
  - `gTTS` for text-to-speech
  - `beautifulsoup4` for web scraping (if required later)

## Installation & Setup
### 1. Clone the Repository
```sh
git clone https://github.com/your-repository-link.git
cd news-summarization-hindi-tts
```
### 2. Install Dependencies
```sh
pip install -r requirements.txt
```
### 3. Run the Application
```sh
streamlit run app.py
```

## Code Structure
```
news-summarization-hindi-tts/
│── api.py                   # Fetches news articles using NewsAPI
│── utils.py                 # Contains summarization, sentiment analysis, translation, key topics extraction, and TTS functions
│── app.py                   # Streamlit frontend application
│── requirements.txt         # List of required dependencies
│── README.md                # Documentation
```

## Model Details
### **Summarization Model**
- Uses a pre-trained transformer model from Hugging Face (e.g., `facebook/bart-large-cnn`).
- Extracts key points from the news article.

### **Sentiment Analysis**
- Uses NLTK's `VADER` sentiment analysis model.
- Categorizes text as Positive, Neutral, or Negative.

### **Key Topics Extraction**
- Uses `KeyBERT` to extract the most relevant topics from the summary.

### **Hindi Translation**
- Uses Google Translate API (`googletrans`) to convert English summaries to Hindi.

### **Text-to-Speech (TTS)**
- Uses `gTTS` (Google Text-to-Speech) to generate an MP3 audio file of the Hindi summary.

## API Development
The project includes APIs for fetching news, summarization, sentiment analysis, key topics extraction, translation, and text-to-speech conversion.

### API Endpoints
#### **1. Fetch News**
- **Endpoint:** `fetch_news(company_name)`
- **Description:** Fetches the latest 5 news articles about the given company.
- **Response Format:**
  ```json
  [
    {
      "title": "Article Title",
      "key_topics": ["Topic1", "Topic2"],
      "summary": "Short summary of the article.",
      "sentiment": "Positive",
      "sentiment_score": 0.1779,
      "hindi_summary": "हिन्दी में सारांश"
    }
  ]
  ```

#### **2. Summarization**
- **Function:** `summarize_text(text)`
- **Description:** Summarizes the input text using a Hugging Face transformer model.
- **Returns:** Shortened summary of the input text.

#### **3. Sentiment Analysis**
- **Function:** `analyze_sentiment(text)`
- **Description:** Uses NLTK's VADER sentiment analysis to classify text as Positive, Neutral, or Negative.
- **Returns:** Sentiment category and sentiment score.

#### **4. Key Topics Extraction**
- **Function:** `extract_key_topics(text, num_keywords=3)`
- **Description:** Extracts the most important topics from the given text using `KeyBERT`.
- **Returns:** A list of key topics.

#### **5. Hindi Translation**
- **Function:** `translate_to_hindi(text)`
- **Description:** Translates the given text from English to Hindi using Google Translate API.
- **Returns:** Hindi-translated text.

#### **6. Text-to-Speech (TTS)**
- **Function:** `text_to_speech_google(text, filename="news_summary.mp3")`
- **Description:** Converts Hindi text into a speech audio file.
- **Returns:** Filename of the generated MP3 file.

## API Usage
- The APIs can be tested using Postman by making requests to the backend service.
- Example Postman Request for fetching news:
  ```sh
  GET http://localhost:5000/fetch_news?company_name=amazon
  ```

## Assumptions & Limitations
### **Assumptions**
- NewsAPI provides relevant articles based on the given company name.
- The summarization model correctly captures the essence of the news article.
- Google Translate provides an accurate Hindi translation.
- TTS output is clear and understandable.

### **Limitations**
- NewsAPI has rate limits, so too many requests may fail.
- Sentiment analysis might not be 100% accurate for complex news content.
- Google Translate may not always provide perfect translations.
- `gTTS` might have pronunciation issues for certain Hindi words.

## Deployment Plan
1. **Local Testing:** Ensure all functionalities work as expected.
2. **Containerization (Optional):** Use Docker to package the application.
3. **Deployment on Hugging Face Spaces:**
   - Push code to GitHub
   - Deploy using Hugging Face Spaces
   - Test and verify

## Future Improvements
- Support for multiple languages.
- Improved summarization with fine-tuned models.
- Enhanced sentiment analysis with deep learning models.
- Integration with real-time news sources.


This documentation will be continuously updated as new features are added.

