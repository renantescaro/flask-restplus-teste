from flask import Flask
from flaskr.api.pessoa_api import bp as bp_pessoa
from flaskr.api_doc import blueprint as documented_endpoint


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
        RESTPLUS_MASK_SWAGGER = False )


    # adicionar rotas
    app.register_blueprint(bp_pessoa)
    app.register_blueprint(documented_endpoint)
    return app