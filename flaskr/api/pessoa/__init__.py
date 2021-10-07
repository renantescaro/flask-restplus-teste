import json
from flask_restplus import Namespace, Resource, fields

namespace = Namespace('pessoas', '')
erro = json.dumps({'status':False})

post_pessoa = namespace.model('pessoa', 
    {
        'id': fields.Integer(
            required=True,
            description='Identificador único'
        ),
        'nome': fields.String(
            required=True,
            description='Nome da pessoa'
        )
    }
)

@namespace.route('')
class PessoaApi(Resource):
    @namespace.response(500, erro)
    def get(self):
        '''Listagem de pessoas'''
        return {'pessoas': 'teste'}


    @namespace.expect(post_pessoa)
    @namespace.response(500, erro)
    def post(self):
        '''Insere nova pessoa'''
        return {'status':True}