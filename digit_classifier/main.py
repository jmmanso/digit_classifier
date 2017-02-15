import sys
import numpy as np
from feather import ann
import preprocessing
import config



class Trainer:

    def get_data(self):
        self.X_train, self.y_train, self.X_test, self.y_test =\
            preprocessing.prep_training_data()

    def train_net(self):

        self.mlp = ann.ANN(
            self.X_train,
            train_y=self.y_train,
            test_X = self.X_test,
            test_y = self.y_test,
            **config.mlp_params)

        self.mlp.fit(config.N_epochs)
        self.mlp.save_net(config.weights_path)

    def __call__(self):
        self.get_data()
        self.train_net()


class Classifier:

    def __init__(self):
        self.load_mlp()

    def load_mlp(self):
        # Initialize ANN class
        self.mlp = ann.ANN(
            # dummy data initialization
            np.zeros((1, config.final_img_size**2)),
            train_y=np.zeros((1,10)),
            **config.mlp_params)
        # Load trained params
        self.mlp.load_net(config.weights_path)

    def predict(self, file_path):

        X = preprocessing.prep_http_data(file_path)

        probs = self.mlp.predict_proba(X.reshape(1,-1))
        output = {"prediction" : np.argmax(probs)}
        return output


if __name__=="main":
    # -t flag indicates training
    if sys.argv[1] == "-t":
        Trainer()()





#
