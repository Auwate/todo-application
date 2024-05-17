from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DATABASE_URI = "sqlite:///test.db" # SQLite


# Creating Item table
class Item (db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __init__(self, id: int, name: str, description: str = None) -> None:
        self.id = id
        self.name = name
        self.description = description


def init_db(app) -> None:

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

    db.init_app(app)

    with app.app_context():
        db.create_all()
