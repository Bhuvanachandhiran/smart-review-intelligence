from transformers import pipeline
import spacy

class ReviewAnalyzer:
    def __init__(self):
        # Sentiment model (binary, fast, reliable)
        self.sentiment_model = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

        # Emotion model (adds depth beyond sentiment)
        self.emotion_model = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            top_k=1
        )

        # Named Entity Recognition
        self.nlp = spacy.load("en_core_web_sm")

    def analyze(self, text):
        sentiment = self.sentiment_model(text)[0]
        emotion = self.emotion_model(text)[0][0]

        doc = self.nlp(text)
        entities = [
            {"text": ent.text, "label": ent.label_}
            for ent in doc.ents
        ]

        return {
            "sentiment": sentiment,
            "emotion": emotion,
            "entities": entities
        }
