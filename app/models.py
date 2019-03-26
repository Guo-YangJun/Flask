from manage import db

class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(32))
    author = db.Column(db.String(32))
    picture = db.Column(db.String(32))
    time = db.Column(db.DATETIME)
    types = db.Column(db.String(32))
    content  = db.Column(db.TEXT)
    description = db.Column(db.TEXT)

    def __repr__(self):
        return self.title

class Image(db.Model):
    __tablename__ = "image"
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(32))
    picture = db.Column(db.String(32))
    time = db.Column(db.DATETIME)
    description = db.Column(db.TEXT)

    def __repr__(self):
        return self.label