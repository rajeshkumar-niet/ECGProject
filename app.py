from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from keras.models import load_model
import os

# Initialize Flask app
app = Flask(__name__)

# Load trained model (compile=False to avoid old config errors)
model = load_model("ecg_denoising_autoencoder.h5", compile=False)

@app.route("/")
def index():
    # Render the main page
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return "⚠️ No file uploaded"

    file = request.files["file"]
    if file.filename == "":
        return "⚠️ No selected file"

    if file:
        try:
            # Load ECG signal (expecting .npy format)
            ecg_signal = np.load(file)

            # Reshape if required by model
            ecg_signal = ecg_signal.reshape(1, -1, 1)

            # Make prediction
            denoised_signal = model.predict(ecg_signal)

            # TODO: You can return signal, plot, or download option
            return "✅ Prediction complete. You can visualize or save the output."
        except Exception as e:
            return f"❌ Error in prediction: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
