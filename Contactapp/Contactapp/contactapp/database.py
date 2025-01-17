from contactapp import db, login_manager, app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(20), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    contacts = db.relationship('Contacts', backref='user_', lazy=True)

    def get_reset_token(self, expire_secs=1800):
        s = Serializer(app.config['SECRET_KEY'], expire_secs)
        return s.dumps({'user_id': self.id})

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.email}','{self.password}','{self.id}','{self.contacts}')"


class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True, )
    number = db.Column(db.String(13), nullable=False)
    contact_name = db.Column(db.String(20), nullable=False, default=number)
    contact_mail = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Contact('{self.id}', '{self.contact_name}', '{self.number}','{self.contact_mail}', '{self.user_id}')"
