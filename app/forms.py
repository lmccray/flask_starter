from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField,  SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, Length, DataRequired
from flask_wtf.file import FileField, FileRequired, FileField, FileAllowed
from werkzeug.utils import secure_filename

class UserForm(FlaskForm):
    propertytitle = StringField('Property Title', validators=[InputRequired(), Length(max=40)])
    numbedrooms = StringField('No. of Bedrooms', validators=[InputRequired(), Length(max=40)])
    numbathrooms = StringField('No. of Bathrooms', validators=[InputRequired(), Length(max=40)])
    location = StringField('Location', validators=[InputRequired(), Length(max=40)])
    price = StringField('Price', validators=[InputRequired(), Length(max=70)])
    propertytype = SelectField('Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=150)])
    photo= FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png','jpeg'], 'Only images allowed!')])
    submit= SubmitField('Add Property')