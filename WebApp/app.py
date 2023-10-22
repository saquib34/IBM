from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
import time
import logging

app = Flask(__name__, static_url_path='/static')

# Load the pre-trained model
model = tf.keras.models.load_model('ANN_model.h5')

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        units = [float(request.form[f'unit{i}']) for i in range(1, 7)]
        logging.debug(f'Input units: {units}')

        if any(unit < 0 for unit in units):
            logging.error('Units should be positive numbers.')
            return jsonify({'error': 'Units should be positive numbers.'}), 400

        # Add a delay to simulate processing (you can remove this line)
        time.sleep(2)

        # Prepare the input data and make a prediction
        input_data = np.array(units).reshape(1, 6)
        logging.debug(f'Input data for prediction: {input_data}')
        prediction = model.predict(input_data)
        logging.debug(f'Predicted value: {prediction}')

        # You may have to post-process the prediction depending on your model
        predicted_bill = prediction[0][0]
        logging.info(f'Predicted bill: {predicted_bill}')

        return jsonify({'predicted_bill': predicted_bill})
    except Exception as e:
        logging.error(f'An error occurred: {str(e)}')
        return jsonify({'error': 'An error occurred while making the prediction.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
