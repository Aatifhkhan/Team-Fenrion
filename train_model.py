import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

print("Starting model training process...")

# Load dataset
df = pd.read_csv("disaster_data.csv")
print("Dataset loaded successfully.")

# Define features & labels
X = df[["temperature", "rainfall", "humidity"]]
y = df["disaster_label"]

# Split dataset for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Dataset split into training and testing sets.")

# Train the RandomForest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Model training complete.")

# Save the trained model to a file
joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as model.pkl")

# Check and print the accuracy
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
