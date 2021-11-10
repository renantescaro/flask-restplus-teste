from waitress import serve
from flaskr import create_app
from flaskr.utils.config import Config


app = create_app()
serve(app, host=Config.get('APLICACAO_IP'), port=Config.get('APLICACAO_PORTA'))