from MLmodel import models_pool
from MLmodel.models_mapping import models_mapping

import numpy as np

def predict(model_name,save_models_path, X):
    # load pretrained models
    model = models_mapping[model_name.upper()]()
    path = save_models_path + model_name.upper()
    model.load_model(path)

    return model.predict(X)

if __name__ == "__main__":
    X = np.random.normal(size = 40).reshape(-1, 4)
    print(predict('svm', "./TrainedModels/",X))