import os, sys
import json
import string
thisdir = os.path.dirname(__file__)
from flask import Flask, request, jsonify, render_template, flash
from werkzeug.utils import secure_filename
import forms
sys.path.append(os.path.join(thisdir, os.path.pardir))
app = Flask(__name__)



# Start model engine, which will
# load the trained weights
import main
myclassifier = main.Classifier()


# App configs
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['UPLOAD_FOLDER'] = os.path.join(thisdir, 'static/model_data')
app.config['ALLOWED_IMAGES'] = main.config.allowed_images
app.config['MAX_CONTENT_LENGTH'] = main.config.max_content_length




def image_entrypoint(request):
    """
    This function interfaces between the app routes
    (webform and curl) and the model engine. Extracts
    the data from the request, triggers model call and
    returns a result message.

    ARGUMENT: Flask request
    RETURNS: json object with messages or results
    """
    # Extract file
    f = request.files['myfile']
    # Get filename and extension
    filename = secure_filename(f.filename)
    extension = filename.split(".")[-1]
    # Check if it is an allowed extension
    if extension not in app.config['ALLOWED_IMAGES']:
        error_msg = "Error: Invalid image. Should be one of: %s"\
            % string.join(app.config['ALLOWED_IMAGES'], sep=" ")
        return {"message":error_msg, "status":404}
    try:
        # Save file to disk
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], \
            filename)
        f.save(file_path)
        # Trigger model call, passing the file path
        # of the stored image
        prediction_json = myclassifier.predict(file_path)
        return prediction_json
    except:
        error_msg = "Error: could not load file."
        return {"message":error_msg, "status":500}






# Web route
@app.route("/", methods=['GET', 'POST'])
def web_api():
    # Get the request object from the form
    form = forms.ImageForm(request.form)
    if request.method == 'POST':
        # Pass request to interface function
        result_message = image_entrypoint(request)
        # If everything went well, the message should
        # include a digit prediction
        if "prediction" in result_message:
            output = "The predicted digit is %s" \
                % result_message["prediction"]
        else:
            # Otherwise, return the message as a whole
            output = json.dumps(result_message)
        # Render message
        flash(output)

    return render_template('index.html', form=form)



# Curl route
@app.route('/curl-api', methods=['GET','POST'])
def curl_api():
    if request.method == 'POST':
        # Pass request to interface function
        result_message = image_entrypoint(request)
        # Return the full message
        return jsonify(**result_message)



if __name__ == '__main__':
    app.run(debug=DEBUG)
