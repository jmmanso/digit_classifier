import sys
import numpy as np
from feather import ann
import preprocessing
import config



class Trainer:
    """
    Wrapper class for the training pipeline
    """

    def get_data(self):
        """
        Loads and preprocesses MNIST data.
        If not found on disk, it will download
        from the official website.
        """
        self.X_train, self.y_train, self.X_test, self.y_test =\
            preprocessing.prep_training_data()

    def train_net(self):
        """
        Trains a Multi Layer Perceptron classifier
        """
        self.mlp = ann.ANN(
            self.X_train,
            train_y=self.y_train,
            test_X = self.X_test,
            test_y = self.y_test,
            **config.mlp_params)

        self.mlp.fit(config.N_epochs)
        # Save weights as json file 
        self.mlp.save_net(config.weights_path)

    def __call__(self):
        self.get_data()
        self.train_net()


class Classifier:
    """
    Wrapper class for the evaluation pipeline.
    """
    def __init__(self):
        self.load_mlp()

    def load_mlp(self):
        """
        Loads file with trained weights and
        instantiates new MLP classifier
        """
        # Initialize ANN class
        self.mlp = ann.ANN(
            # dummy data initialization
            np.zeros((1, config.final_img_size**2)),
            train_y=np.zeros((1,10)),
            **config.mlp_params)
        # Load trained params
        self.mlp.load_net(config.weights_path)

    def predict(self, file_path):
        """
        Given a file path to an image, returns
        the predicted digit
        """
        # Format and preprocess image
        X = preprocessing.prep_http_data(file_path)
        # Pass numeric array through MLP and get
        # softmax probabilities
        probs = self.mlp.predict_proba(X.reshape(1,-1))
        # Return most likely index as the prediction
        output = {"prediction" : np.argmax(probs)}
        return output


if __name__=="__main__":
    # -t flag indicates training
    if sys.argv[1] == "-t":
        Trainer()()





#
