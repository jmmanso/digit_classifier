import cPickle
from sklearn.preprocessing import OneHotEncoder
from scipy import misc
import subprocess
import numpy as np
import os
import config
import read_mnist
thisdir = os.path.dirname(__file__)






class TrainingDataLoader:


    def download_and_extract_data(self):

        if not self.rawdata_exists():
            print "Raw data files not found. Downloading data..."
            self.download()

        X_train, y_train, X_test, y_test = self.extract()

        return X_train, y_train, X_test, y_test

    def rawdata_exists(self):
        """
        Determine if data file exists in directory
        """
        if not any([not os.path.exists(_filepath)
            for _filepath in config.rawdata_filepaths.values()]):
            return True
        else:
            return False

    def download(self):
        status = 1
        for _fileurl in config.rawdata_urls:
            print "Downloading "+_fileurl
            exit_stat = subprocess.call(["wget", _fileurl, \
                "-P", config.rawdata_dir])
            status *= 1 - exit_stat
        if status!=1:
            raise Exception("Unable to download data")

    def extract(self):

        print "Extracting data from files. This might take several minutes"
        X_train, y_train = \
            read_mnist.get_labeled_data(
                config.rawdata_filepaths['training_images'],
                config.rawdata_filepaths['training_labels'])

        X_test, y_test = \
            read_mnist.get_labeled_data(
                config.rawdata_filepaths['test_images'],
                config.rawdata_filepaths['test_labels'])

        # Save as numpy arrays
        for kind, arr in {'training_images':X_train,\
            'training_labels':y_train,\
            'test_images':X_test, \
            'test_labels':y_test}.items():
            np.save(os.path.join(config.rawdata_dir, kind+'.npy'), arr)

        return X_train, y_train, X_test, y_test

    def load(self):

        try:
            X_train = np.load(os.path.join(config.rawdata_dir, 'training_images.npy'))
            y_train = np.load(os.path.join(config.rawdata_dir, 'training_labels.npy'))
            X_test = np.load(os.path.join(config.rawdata_dir, 'test_images.npy'))
            y_test = np.load(os.path.join(config.rawdata_dir, 'test_labels.npy'))
            return X_train, y_train, X_test, y_test
        except:
            print "Data is not found as numpy arrays. Will try to extract from raw source..."
            return self.download_and_extract_data()




class HttpDataLoader:

    def __init__(self,
        image_path,
        min_px_size = config.min_px_size,
        final_img_size = config.final_img_size):
        self.img = misc.imread(image_path, mode='P')
        self.min_px_size = min_px_size
        self.final_img_size = final_img_size

    def image_check(self, img):
        # get the sizes of each axis
        size0, size1 = img.shape
        # checl minimum size in pixels
        if size0 < self.min_px_size and size1 < self.min_px_size:
            return False
        else:
            return True

    def image_crop(self, img):
        """ If image is rectangular, crop to central square """
        smallest_axis_index = np.argmin(img.shape)
        largest_axis_index = (1 - smallest_axis_index)**2
        smallest_axis_px = img.shape[smallest_axis_index]
        largest_axis_px = img.shape[largest_axis_index]
        px_diff = largest_axis_px - smallest_axis_px
        side_margin = px_diff // 2
        if side_margin>0:
            if largest_axis_index == 0:
                img = img[side_margin : side_margin+smallest_axis_px]
            else:
                img = img[:, side_margin : side_margin+smallest_axis_px]
        return img

    def image_resample(self, img):
        """ Resample image to match MNIST resolution """
        img = misc.imresize(img, \
            size = (self.final_img_size, self.final_img_size))
        return img

    def load(self):
        if not self.image_check(self.img):
            return False
        img = self.image_crop(self.img)
        img = self.image_resample(img)
        return img
