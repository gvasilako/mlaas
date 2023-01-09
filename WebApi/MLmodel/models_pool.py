from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import pickle
import os


class LR:

    def __init__(self, *args, **kwargs):
        self.estimator = LogisticRegression(*args, **kwargs)

    def train(self, X, y):
        self.estimator.fit(X, y)

    def predict(self, X):
        return self.estimator.predict(X)

    def save_model(self, path):
        # save model weights
        weights_dir = os.path.join(path, "Weights")
        os.makedirs(weights_dir, exist_ok=True)
        pickle.dump(self.estimator, open(weights_dir + "/model.pkl", "wb"))

    def load_model(self, path):
        # load model weights
        weights_dir = os.path.join(path, "Weights")
        self.estimator = pickle.load(open(weights_dir + "/model.pkl", "rb"))
        return self

class SVM:

    def __init__(self, *args, **kwargs):
        self.estimator = SVC(*args, **kwargs)

    def train(self, X, y):
        self.estimator.fit(X, y)

    def predict(self, X):
        return self.estimator.predict(X)

    def save_model(self, path):
        # save model weights
        weights_dir = os.path.join(path, "Weights")
        os.makedirs(weights_dir, exist_ok=True)
        pickle.dump(self.estimator, open(weights_dir + "/model.pkl", "wb"))

    def load_model(self, path):
        # load model weights
        weights_dir = os.path.join(path, "Weights")
        self.estimator = pickle.load(open(weights_dir + "/model.pkl", "rb"))
        return self



