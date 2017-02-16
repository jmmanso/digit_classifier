# Digit Classifier

This package deploys a REST service that gets images of single digits via POST request and returns the predicted digit integer.

The application can be accessed here:

http://ec2-54-219-168-245.us-west-1.compute.amazonaws.com/

In the sections below we will cover the details of the application and walk through a local deployment on your machine.


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
* Images can also be of any size (within some edge limits). They will be resampled to match the original MNIST 28x28 resolution.

## Deployment on local machine

The following steps will take you to serve the application locally with a Flask server. These steps are reversible and non-invasive, in the end we will remove all of it.
Please use a OSX or Linux system.

#### Get the code
Clone the repo
```bash
git clone https://github.com/jmmanso/digit_classifier.git \
/usr/src/digit_classifier
```

Model-specific configuration can be seen and modified at `digit_classifier/config.py`.

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
bash build_all_local.sh
```

In a web browser, go to `http://localhost:5000/`, and you will see the app.

#### Cleaning up

```bash
cd /usr/src/digit_classifier/deployment_scripts
bash cleanup.sh
```
