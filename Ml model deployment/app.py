from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the request
    data = request.form
    try:
        sepal_length = float(data['sepal_length'])
        sepal_width = float(data['sepal_width'])
        petal_length = float(data['petal_length'])
        petal_width = float(data['petal_width'])
    except ValueError:
        return jsonify({'error': 'Invalid input, ensure all values are numeric.'})

    # Prepare the input for prediction
    input_features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Make a prediction
    prediction = model.predict(input_features)

    # Return the prediction result
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
    print("Finished")
