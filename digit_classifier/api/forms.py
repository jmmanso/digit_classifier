from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField, Form

class ImageForm2(FlaskForm):
    myfile = FileField()
    #FileField(validators=[FileRequired(), FileAllowed(['png','jpeg','gif','svg','jpg'], message = 'Invalid file extension')])
    #submit = SubmitField("Send")


class ImageForm(Form):
    myfile = FileField("Upload an image")
    submit = SubmitField("Send")
