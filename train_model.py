import pandas as pd
import re
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


print("Loading dataset...")

# 1️⃣ Load dataset
df = pd.read_csv("phishing_legit_dataset.csv")

print("Dataset Loaded Successfully")
print("Shape:", df.shape)


# 2️⃣ Basic Cleaning

# Drop missing values if any
df = df.dropna(subset=['text', 'label'])

# Convert text to lowercase
df['text'] = df['text'].str.lower()

# Remove special characters
df['text'] = df['text'].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x))

# Remove extra spaces
df['text'] = df['text'].apply(lambda x: re.sub(r'\s+', ' ', x))

print("Text cleaned successfully.")


# 3️⃣ Prepare features and labels

X = df['text']
y = df['label']


# 4️⃣ Convert text to TF-IDF vectors

vectorizer = TfidfVectorizer(max_features=5000)
X_vectorized = vectorizer.fit_transform(X)

print("Text vectorized successfully.")


# 5️⃣ Train-test split

X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

print("Data split completed.")


# 6️⃣ Train Logistic Regression model

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print("Model trained successfully.")


# 7️⃣ Evaluate model

y_pred = model.predict(X_test)

print("\n==============================")
print("Model Evaluation Results")
print("==============================")

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


# 8️⃣ Save model and vectorizer

joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("\nModel and vectorizer saved successfully!")