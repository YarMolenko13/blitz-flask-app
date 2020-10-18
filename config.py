class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'something very secret'

    ### FLASK-SECURITY ###
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'



