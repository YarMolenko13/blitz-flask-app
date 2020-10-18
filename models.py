from app import db
from datetime import datetime

from flask_security import UserMixin, RoleMixin


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30), nullable=False)
    l_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.String(50), default=datetime.now().strftime("%B %d,%Y"))

    def __repr__(self):
        return '<Article %r>' % self.id


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img_path = db.Column(db.String(100), default='../static/images/projects_img')
    title = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    text = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Article %r>' % self.id


class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    img_path = db.Column(db.String(100), default='../static/images/projects_img')
    date = db.Column(db.String(50), default=datetime.now().strftime("%B %d ,%Y"))
    tags = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    comments = db.relationship('Comments', uselist=False, backref='posts')

    def __repr__(self):
        return '<Article %r>' % self.id


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_post = db.Column(db.Integer, db.ForeignKey('posts.id'))
    name = db.Column(db.String(30), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(50), default=datetime.now().strftime("%B %d ,%Y %H:%M"))

    def __repr__(self):
        return '<Article %r>' % self.id


### FLASK SECURITY ###

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(70), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
