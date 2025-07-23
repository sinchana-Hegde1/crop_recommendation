import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

try:
    df = pd.read_csv('Crop_recommendation.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: 'Crop_recommendation.csv' not found. Please ensure the dataset file is in the correct directory.")
    exit()

X = df.drop('label', axis=1)

y = df['label']

print("Features (X) and Target (y) are prepared.")
print("Features shape:", X.shape)
print("Target shape:", y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Data split into training and testing sets.")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)

model = RandomForestClassifier(n_estimators=20, random_state=42)

print("Training the Random Forest model...")

model.fit(X_train, y_train)
print("Model training completed.")

y_pred = model.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy on Test Set: {accuracy * 100:.2f}%")

model_filename = 'model.pkl'
with open(model_filename, 'wb') as file:
    pickle.dump(model, file)

print(f"Trained model saved successfully as '{model_filename}'.")

