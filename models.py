from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMG = "https://tinyurl.com/demo-cupcake"

class Cupcake(db.Model):
    """ Cupcake """

    __tablename__ = "cupcakes"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
    )

    flavor = db.Column(
        db.Text,
        nullable=False,
    )

    size = db.Column(
        db.Text,
        nullable=False,
    )

    rating = db.Column(
        db.Integer,
        nullable=False,
    )

    image = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_IMG
    )

    def serialize(self):
        """ Serialize to dict """

        return {
            "id": self.id,
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image
        }

def connect_db(app):
    """Connect to database."""

    app.app_context().push()
    db.app = app
    db.init_app(app)