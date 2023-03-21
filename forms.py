"""Forms for playlist app."""

from wtforms import SelectField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Optional, URL

class AddCupcakeForm(FlaskForm):
    """Form for adding playlists."""

    flavor = StringField(
        'Flavor Description', 
        validators=[InputRequired()]
    )

    size = StringField(
        'Size Description', 
        validators=[InputRequired()]
    )

    rating = StringField(
        'Rating Description', 
        validators=[InputRequired()]
    )

    image = StringField(
        'Image URL', 
        validators=[Optional(), URL()]
    )
