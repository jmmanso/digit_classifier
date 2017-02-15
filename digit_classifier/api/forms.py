
from wtforms import SubmitField, Form, FileField




class ImageForm(Form):
    myfile = FileField("Upload an image")
    submit = SubmitField("Send")
