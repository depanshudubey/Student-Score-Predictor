import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

print("Starting model training...")

# Load dataset
data = pd.read_csv("student_data.csv")

print("Dataset loaded!")
print(data.head())

# Features
X = data[
    [
        "hours_studied",
        "attendance",
        "sleep_hours",
        "previous_score"
    ]
]

# Target
y = data["final_score"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluation
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("Model trained successfully!")
print("MAE:", mae)
print("R2 Score:", r2)

# Save model
joblib.dump(model, "model.pkl")

print("model.pkl created successfully!")