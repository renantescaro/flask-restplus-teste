from flask import Blueprint
from flask_restplus import Api
from flaskr.api.pessoa import namespace as pessoa_ns

bp = Blueprint(
    'api',
    __name__,
    url_prefix='/api')

api_extension = Api(
    bp,
    title='Flask RESTplus Teste',
    version='1.0',
    description='Testando Flask RESTplus',
    doc='/doc'
)

api_extension.add_namespace(pessoa_ns)