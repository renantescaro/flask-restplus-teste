from flask import Flask
from flaskr.utils.config import Config
from flaskr.models_db import db
from flaskr.api import bp as bp_api


def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path = '/static',
        static_folder   = 'static',
        instance_relative_config = True )

    app.config.from_mapping(
        SECRET_KEY   = 'super secret key',
        SESSION_TYPE = 'filesystem',
        JSONIFY_PRETTYPRINT_REGULAR = False,
        SQLALCHEMY_DATABASE_URI = Config.get('DATABASE_URI')  )


    # adicionar rotas
    db.init_app(app)
    app.register_blueprint(bp_api)

    with app.app_context():
        db.create_all()

    return app