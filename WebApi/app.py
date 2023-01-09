# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, jsonify, request
import MLmodel.predict as model_prediction
import numpy as np
from flask_cors import CORS

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
CORS(app)

iris_targets = ['setosa', 'versicolor', 'virginica']

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'


@app.route('/prediction', methods=["POST"])
# ‘/’ URL is bound with hello_world() function.
def predict():
    input_data = [value for _, value in request.get_json().items()]
    prediction = model_prediction.predict('svm', "MLmodel/TrainedModels/", np.array(input_data).reshape(1, -1))[0]
    output = {'Prediction': iris_targets[int(prediction)]}
    return jsonify(output), 200


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)
