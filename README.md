# Digit Classifier

This package deploys a REST service that gets images of single digits via POST request and returns the predicted digit integer.

The application can be accessed here:

http://ec2-54-219-168-245.us-west-1.compute.amazonaws.com/

In the sections below we will cover some of the details of the application and walk through a local deployment on your machine.


### What are the app components?
* Platform: Ubuntu on EC2
* Server: Apache, ModWSGI
* Web application: Flask, Jinja2, WTForms, Bootstrap
* ML engine: Python pipeline, including Multi Layer Perceptron for image classification (also written by me)  

### What are the endpoints?
The service can be accessed either via web-form or cURL call.

### What is special about this app?

The classifier is trained with the MNIST data found at:
http://yann.lecun.com/exdb/mnist/
which contains 60000 images of 28x28 pixels in size.

However, the app pipeline has extended capability to process digit images from other sources. In particular:
* Part of the training image set has been inverted, thus this classifier works well with black or white backgrounds.
* Rectangular images are accepted. They will be cropped to a central square of maximum size.
* Images can also be of any size (within some edge limits; more than 10px and less than 1 Mb). They will be resampled to match the original MNIST 28x28 resolution.

## Deployment on local machine

The following steps will take you to serve the application locally with a Flask server. Please use a OSX or Linux system.

### Quick deploy

The entire application can be built with these commands

```bash
git clone https://github.com/jmmanso/digit_classifier.git /usr/local/opt/digit_classifier
cd /usr/local/opt/digit_classifier/deployment_scripts
sudo bash build_all_local.sh
```

These deployment steps are discussed below.

### Get the code
Clone the repo
```bash
git clone https://github.com/jmmanso/digit_classifier.git /usr/local/opt/digit_classifier
```

If you wish to inspect the app configuration, here are some relevant files:
* App environment configuration: `digit_classifier/deployment_scripts/config_profile.sh`
* Model-specific configuration: `digit_classifier/digit_classifier/config.py`
* Top-level model file defining training and evaluation wrapper classes: `digit_classifier/digit_classifier/main.py`
* The model is served to the app via: `digit_classifier/digit_classifier/api/views.py`

### Build the app

At a high level, the build process consists of:
* Define environment variables for the app
* Create a python virtual environment and install dependencies
* Download MNIST data
* Extract and read MNIST data (few minutes)
* Preprocess data and train classifier (few minutes)

Execute build script, which can take several minutes:

```bash
cd /usr/local/opt/digit_classifier/deployment_scripts
sudo bash build_all_local.sh
```

You will be able to see the training process in the terminal, something like this:
```bash
Epoch 0 train_accuracy: 0.677  test_accuracy: 0.865
Epoch 1 train_accuracy: 0.888  test_accuracy: 0.897
Epoch 2 train_accuracy: 0.909  test_accuracy: 0.923
Epoch 3 train_accuracy: 0.923  test_accuracy: 0.932
Epoch 4 train_accuracy: 0.931  test_accuracy: 0.936
```

Once the job is finished, in a web browser go to `http://localhost:5000/`, and you will see the app.

### Clean up

Remove the repo, app and virtual environment directories
```bash
cd /usr/local/opt/digit_classifier/deployment_scripts
sudo bash cleanup.sh
rm -rf /usr/local/opt/digit_classifier
```
