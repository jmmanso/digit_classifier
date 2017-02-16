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

The following steps will take you to serve the application locally with a Flask server. These steps are reversible and non-invasive, in the end we will remove all of it.
Please use a OSX or Linux system.

#### Get the code
Clone the repo
```bash
git clone https://github.com/jmmanso/digit_classifier.git \
/usr/src/digit_classifier
```

These are some relevant files:
* App environment configuration: `digit_classifier/deployment_scripts/config_profile.sh`
* Model-specific configuration: `digit_classifier/config.py`
* Top-level model file defining training and evaluation wrapper classes: `digit_classifier/main.py`
* The model is served to the app via: `digit_classifier/api/views.py`

#### Build the app

At a high level, the build process consists of:
* Define environment variables for the app
* Create a python virtual environment and install dependencies
* Download MNIST data
* Extract and read MNIST data (few minutes)
* Preprocess data and train classifier (few minutes)

Execute build script, which can take several minutes:

```bash
cd /usr/src/digit_classifier/deployment_scripts
sudo bash build_all_local.sh
```

In a web browser, go to `http://localhost:5000/`, and you will see the app.

#### Clean up

Remove the repo, app and virtual environment directories
```bash
cd /usr/src/digit_classifier/deployment_scripts
sudo bash cleanup.sh
rm -rf /usr/src/digit_classifier
```
