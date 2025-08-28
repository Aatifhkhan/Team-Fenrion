import joblib
import pandas as pd

model = joblib.load("model.pkl")

# Wrap test data in a DataFrame with column names
cols = ["temperature", "rainfall", "humidity"]

print(model.predict(pd.DataFrame([[43, 0, 20]], columns=cols)))   # heatwave
print(model.predict(pd.DataFrame([[27, 220, 90]], columns=cols))) # flood
print(model.predict(pd.DataFrame([[32, 15, 55]], columns=cols)))  # normal
