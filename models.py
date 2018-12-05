from . import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String)
    name = db.Column(db.String, index=True, nullable=False)
    description = db.Column(db.String)
    brand = db.Column(db.String)

    def __repr__(self):
        return '<Product {}>'.format(self.name)
