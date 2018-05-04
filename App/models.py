from App.ext import db


class HomeBaner(db.Model):
    __tablename__ = 'axf_wheel'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(256))
    name = db.Column(db.String(256))
    trackId = db.Column(db.String(32))

    def __repr__(self):
        return '%s %s %s' % (self.image, self.name, self.trackId)
