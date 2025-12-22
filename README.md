# Smart Review Intelligence System

An NLP-based application that analyzes customer reviews and extracts actionable insights using transformer models and named entity recognition.

## Features
- Sentiment analysis using transformer-based models
- Emotion detection for deeper opinion understanding
- Named Entity Recognition (NER) for extracting key information
- Interactive web interface using Streamlit

## Tech Stack
- Python
- Hugging Face Transformers
- spaCy
- Streamlit
- PyTorch

## How It Works
1. User inputs a customer review
2. Transformer models analyze sentiment and emotion
3. spaCy extracts named entities such as products, organizations, and dates
4. Results are displayed in real time via a web interface

## Use Case
Designed to help businesses understand customer feedback and extract structured insights from unstructured text.

## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
