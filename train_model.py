import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("disaster_data.csv")
X = df[["temperature", "rainfall", "humidity"]]
y = df["disaster_label"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model, "model.pkl")
print("✅ Model trained and saved as model.pkl")
print("Accuracy:", model.score(X_test, y_test))
