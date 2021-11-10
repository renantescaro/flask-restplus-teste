from flask import Blueprint
from flask_restx import Api
from flaskr.api.pessoa import namespace as pessoa_ns

bp = Blueprint(
    'api',
    __name__,
    url_prefix='/api')

api_extension = Api(
    bp,
    title='Flask restx Teste',
    version='1.0',
    description='Testando Flask restx',
    doc='/doc'
)

api_extension.add_namespace(pessoa_ns)