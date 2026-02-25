import pandas as pd

print("Loading dataset...")

# Load dataset
df = pd.read_csv("phishing_legit_dataset.csv")

# Basic info
print("\nShape of dataset:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

print("\nLabel Distribution:")
print(df['label'].value_counts())