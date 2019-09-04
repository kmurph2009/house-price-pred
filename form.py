from flask_wtf import FlaskForm
from wtforms import IntegerField,DecimalField,SubmitField
from wtforms.validators import DataRequired


class Prediction(FlaskForm):
    bedrooms = IntegerField('number of Bedrooms',validators = [DataRequired()])
    bathrooms = IntegerField('number of bathrooms',validators = [DataRequired()])
    sqft_living = IntegerField('sqft living',validators = [DataRequired()])
    sqft_lot = IntegerField('sqft lot',validators = [DataRequired()])
    floors= IntegerField('floors',validators = [DataRequired()])
    sqft_above = IntegerField('sqft above',validators = [DataRequired()])
    sqft_Lot15= IntegerField('sqft lot15',validators = [DataRequired()])
    yr_built = IntegerField('yr built',validators = [DataRequired()])
    condition = IntegerField('condition',validators = [DataRequired()])
    zipcode = IntegerField('zipcode',validators = [DataRequired()])
    submit = SubmitField('Predict')
