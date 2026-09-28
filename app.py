from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained ML model
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    # Get values from the form
    hours = float(request.form["hours"])
    attendance = float(request.form["attendance"])
    sleep = float(request.form["sleep"])
    previous = float(request.form["previous"])

    # Create DataFrame with the same feature names
    # used while training the model
    input_data = pd.DataFrame([{
        "hours_studied": hours,
        "attendance": attendance,
        "sleep_hours": sleep,
        "previous_score": previous
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Round prediction
    prediction = round(prediction, 2)

    # Send prediction back to webpage
    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)