"""
This file runs the Flask application we are using as an API endpoint.
"""

from flask import Flask

# Create a flask
app = Flask(__name__)


# Create an API end point
@app.route('/predict', methods=['GET'])
def get_prediction():
   return "Prediction API here!"


if __name__ == '__main__':
    # Run the app at 0.0.0.0:3333
    app.run(port=3333, host='0.0.0.0')