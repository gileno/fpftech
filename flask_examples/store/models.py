from .extensions import db


class Category(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return self.name
    
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }


class Product(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    description = db.Column(db.Text())
    category_id = db.Column(
        db.Integer, db.ForeignKey('category.id'), nullable=False
    )
    category = db.relationship(
        'Category', backref=db.backref('products', lazy=True)
    )
