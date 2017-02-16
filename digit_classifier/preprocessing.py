import numpy as np
from sklearn.preprocessing import OneHotEncoder
import config
import data_loader



def prep_training_data():
    """
    Loads and preprocesses raw training images.

    RETURNS
        tuple of ndarrays: training data, training labels,
        test data, test labels
    """
    # Get the data
    X_train, y_train, X_test, y_test =\
        data_loader.TrainingDataLoader().load()
    # Scale data values
    T = Transformer()
    X_train = T.image_scaler(X_train)
    X_test = T.image_scaler(X_test)
    # Create image negatives
    X_train = T.image_random_flipper(X_train)
    X_test = T.image_random_flipper(X_test)
    # Flatten
    X_train = X_train.reshape(X_train.shape[0],\
        X_train.shape[1]**2)
    X_test = X_test.reshape(X_test.shape[0],\
        X_test.shape[1]**2)
    # Encode labels
    encoder = LabelEncoder()
    y_train = encoder.dense2onehot(y_train)
    y_test = encoder.dense2onehot(y_test)
    return X_train, y_train, X_test, y_test

def prep_http_data(file_path):
    """
    Loads and preprocesses a raw image for classification
    """
    # Get the formatted image
    X = data_loader.HttpDataLoader(file_path).load()
    # Scale data values
    X = Transformer().image_scaler(X)
    # Flatten
    X = X.ravel()
    return X



class Transformer:
    """
    Preprocessing transformations for already formatted data
    """

    def image_scaler(self, img_array):
        """
        Scales and offsets pixel values.
        ARGUMENTS
            img_array: ndarray, shape (Nsamples, Width, Height).
            Sequence of image arrays.
        RETURNS
            Ndarray of same shape with values scaled and centered
            within (-1, 1)
        """
        img_array = img_array/255.
        img_array = img_array - 0.5
        return img_array

    def image_random_flipper(self, img_array):
        """
        Randomly returns the negative of some images.
        This is a form of data diversification, to account
        for dark/white backrounds and digits.
        ARGUMENTS
            img_array: ndarray, shape (Nsamples, Width,
             Height). Sequence of image arrays. Should have values between (-1, 1).
        RETURNS
            ndarray of shape where half the rows have
            subarray's values inverted.
        """
        # Determine which images will be inverted,
        # this produces an array with 1 and -1:
        flip_sign = (2*np.random.random(len(img_array)))\
            .astype('int')*2-1
        # Invert
        img_array = np.array([img_array[i]*flip_sign[i] \
            for i in range(flip_sign.size)])

        return img_array



class LabelEncoder(OneHotEncoder):
    """
    Transformation from a dense sequence of
    labels to sparse one-hot representation
    """

    def __init__(self, label_index_base=config.label_index_base):
        """
        Initialize base class and fit canonical label list
        """
        OneHotEncoder.__init__(self)
        self.fit([[l] for l in set(label_index_base)])

    def dense2onehot(self, label_indices):
        """
        Transforms dense list of indices to one-hot representation
        """
        onehot_labels = \
            self.transform(np.array(label_indices)).toarray()
        return onehot_labels
