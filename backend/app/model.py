import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample model (for demonstration)
vectorizer = CountVectorizer()
classifier = MultinomialNB()

def train():
    # Training data
    texts = ["error in module", "warning in system", "failure in network"]
    labels = [0, 1, 0]  # 0 = Error, 1 = Warning

    vectors = vectorizer.fit_transform(texts)
    classifier.fit(vectors, labels)

def predict_log(log: str):
    vector = vectorizer.transform([log])
    prediction = classifier.predict(vector)
    return "ERROR" if prediction[0] == 0 else "WARNING"

# Train model initially
train()
