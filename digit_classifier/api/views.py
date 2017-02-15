import os, sys
import json
import string
thisdir = os.path.dirname(__file__)
from flask import Flask, request, jsonify, render_template, flash
from werkzeug.utils import secure_filename
import forms
sys.path.append(os.path.join(thisdir, os.path.pardir))
app = Flask(__name__)



# Start model engine
import main
myclassifier = main.Classifier()


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['UPLOAD_FOLDER'] = os.path.join(thisdir, 'static/model_data')
app.config['ALLOWED_IMAGES'] = main.config.allowed_images
app.config['MAX_CONTENT_LENGTH'] = main.config.max_content_length




# define classifier function that will be used
# by web and curl routes
def image_entrypoint(request):
    """ Extracts file from request and routes the data.
    Returns a json.
    """
    # extract FileStorage object from flask.request
    f = request.files['myfile']
    filename = secure_filename(f.filename)
    extension = filename.split(".")[-1]
    if extension not in app.config['ALLOWED_IMAGES']:
        error_msg = "Error: Invalid image. Should be one of: %s"\
            % string.join(app.config['ALLOWED_IMAGES'], sep=" ")
        return {"message":error_msg, "status":404}
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], \
            "thisfile.%s" % str(extension))
        f.save(file_path)
        prediction_json = myclassifier.predict(file_path)
        return prediction_json
    except:
        error_msg = "Error: could not load file."
        return {"message":error_msg, "status":500}






# Web route
@app.route("/", methods=['GET', 'POST'])
def upload():
    form = forms.ImageForm(request.form)
    if request.method == 'POST':
        result_message = image_entrypoint(request)
        if "prediction" in result_message:
            output = "The predicted digit is %s" \
                % result_message["prediction"]
        else:
            output = json.dumps(result_message)

        flash(output)

    return render_template('index.html', form=form)



# Curl route
@app.route('/curl-api', methods=['GET','POST'])
def curl_api():
    if request.method == 'POST':
        result_message = image_entrypoint(request)
        return jsonify(**result_message)



if __name__ == '__main__':
    app.run(debug=DEBUG)
