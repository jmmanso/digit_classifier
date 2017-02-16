"""
Main configuration file for the digit_classifier app
"""

import os
thisdir = os.path.dirname(__file__)



### DIRECTORIES AND TAGS
rawdata_baseurl = 'http://yann.lecun.com/exdb/mnist/'
rawdata_files = \
    {'training_images' : 'train-images-idx3-ubyte.gz',
    'training_labels' : 'train-labels-idx1-ubyte.gz',
    'test_images' : 't10k-images-idx3-ubyte.gz',
    'test_labels' : 't10k-labels-idx1-ubyte.gz'}

rawdata_urls = [rawdata_baseurl + _f \
    for _f in rawdata_files.values()]

rawdata_dir = 'rawdata/'
rawdata_filepaths = {key : os.path.join(rawdata_dir, val)
    for key, val in rawdata_files.items()}

### IMAGE REQUIREMENTS
# Minimum size for uploaded images
min_px_size = 10 #px
# Size to which images will be resampled
final_img_size = 28 #px
#
allowed_images = ['png','jpeg','gif','jpg']
# Maximum allowed image size in bytes
max_content_length = 1 * 1024 * 1024

### TRAINING
label_index_base = [0,1,2,3,4,5,6,7,8,9]
# Neural net params
mlp_params = {
    'hidden_depths':[100, 40],
    'eta':0.03,
    'lamb':5.0,
    'batch_size':50,
    'initzero':False,
    'activation_type':'tanh',
    'softmax':True,
    'cost_type':'Xentropy'}

# Number of training epochs
N_epochs = 5
# file path for trained weights
weights_path = os.path.join(thisdir,\
    'api/static/model_data/mlp.param')




#
