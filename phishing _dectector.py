import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
# CSV should contain:
# text,label
# "Congratulations! You won a prize",phishing
# "Meeting at 10 AM tomorrow",legitimate

data = pd.read_csv("emails.csv")

# Features and labels
X = data["text"]
y = data["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("classifier", MultinomialNB())
])

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Save trained model
joblib.dump(model, "phishing_model.pkl")

print("\nModel saved as phishing_model.pkl")

# Predict custom email
while True:
    email = input("\nEnter an email message (or type 'exit'): ")

    if email.lower() == "exit":
        break

    result = model.predict([email])[0]

    if result.lower() == "phishing":
        print("⚠️ Warning: This email is likely PHISHING.")
    else:
        print("✅ This email appears LEGITIMATE.")