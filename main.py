from app import app
from admin.blueprint import admin

import view

app.register_blueprint(admin, url_prefix='/admin2')


if __name__ == '__main__':
    app.run()


