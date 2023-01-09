from sklearn.datasets import load_iris
import models_pool
import os
import json
from sklearn.metrics import accuracy_score,confusion_matrix
from models_mapping import models_mapping

# load dataset
X, y = load_iris(return_X_y=True)

# Initialize model
## Load config_training file
with open("./TrainedModels/config_training.json", 'r') as f:
  config = json.load(f)

## Create model
model_name = config["model"]
model_class = models_mapping[model_name.upper()]
model = model_class(**config[model_name.upper()])

# train model
model.train(X, y)

# check performance
print(accuracy_score(y, model.predict(X)))
print(confusion_matrix(y, model.predict(X)))


# save model
## Create directory for model weights
path = os.path.join("./TrainedModels/", model_name.upper())
model.save_model(path)