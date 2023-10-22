from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load the pre-trained model
model = tf.keras.models.load_model('ANN_model.h5')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        units = [float(request.form[f'unit{i}']) for i in range(1, 7)]
        if any(unit < 0 for unit in units):
            return jsonify({'error': 'Units should be positive numbers.'}), 400

        # Add a delay to simulate processing (you can remove this line)
        import time
        time.sleep(2)

        # Prepare the input data and make a prediction
        input_data = np.array(units).reshape(1, 6)
        prediction = model.predict(input_data)

        # Convert the prediction (which is a NumPy float32) to a native Python float
        predicted_bill = prediction.item()

        return jsonify({'predicted_bill': predicted_bill})
    except Exception as e:
        return jsonify({'error': 'An error occurred while making the prediction.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
