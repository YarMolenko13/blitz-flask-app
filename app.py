from flask import Flask, redirect, url_for, request
from config import Configuration
from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore, Security, current_user

import math


app = Flask(__name__)
app.config.from_object(Configuration)

db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


### ADMIN ###
from models import *

class AdminMixin():
	def is_accessible(self):
		return current_user.has_role('admin')

	def inaccessible_callback(self, name, **kwarg,):
		return redirect(url_for('security.login', next=request.url))	# переадресация


class AdminView(AdminMixin, ModelView):			
	pass


class HomeAdminView(AdminMixin, AdminIndexView): 
	pass


admin = Admin(app, 'Admin', url='', index_view=HomeAdminView(name='Home'))
admin.add_view(AdminView(Posts, db.session))
admin.add_view(AdminView(Comments, db.session))
admin.add_view(AdminView(Projects, db.session))
admin.add_view(AdminView(Contact, db.session))


### FLASK-SECURITY ###

user_datastore = SQLAlchemyUserDatastore(db, User, Role)	# хранилеще для паролей, логинов и ролей
security = Security(app, user_datastore)



# >>> from app import db
# >>> from models import User
# >>> from app import user_datastore
# >>> user_datastore.create_user(email='yaroslav@mail.com', password='1382')
# >>> user = User.query.first()	  - получение пользователя из бд
# >>> user.email
# 'yaroslav@mail.com'
# >>> user_datastore.create_role(name='admin', description='administrator')   - создание роли
# <Role (transient 104854216)>
# >>> db.session.commit()
# >>> from models import Role
# >>> role = Role.query.first()		- получение роли из бд
# >>> user_datastore.add_role_to_user(user, role)     - назначене роли пользователю
# True
# >>> db.session.commit()  - применение внесений в бд