from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import pickle
import os
from abc import ABC, abstractmethod

class Model(ABC):

    @abstractmethod
    def train(self, *args, **kwargs):
        pass

    @abstractmethod
    def predict(self, *args, **kwargs):
        pass

    @abstractmethod
    def save_model(self, *args, **kwargs):
        pass

    @abstractmethod
    def load_model(self, *args, **kwargs):
        pass

class LR(Model):

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

class SVM(Model):

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



