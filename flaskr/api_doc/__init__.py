from flask import Blueprint
from flask_restplus import Api
from flaskr.api_doc.pessoa import namespace as pessoa_ns

blueprint = Blueprint('documented_api', __name__, url_prefix='/documented_api')

api_extension = Api(
    blueprint,
    title='Flask RESTplus Teste',
    version='1.0',
    description='Testando Flask RESTplus',
    doc='/doc'
)

api_extension.add_namespace(pessoa_ns)