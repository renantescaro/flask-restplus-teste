from flask_restx import Namespace, fields


class PessoaModelApi:
    def __init__(self, namespace: Namespace) -> None:
        self.namespace = namespace


    def post(self):
        return self.namespace.model(
            name='pessoa_post',
            model={
            'nome': fields.String(
                required=True,
                description='Nome da pessoa'
            ),
            'data_nascimento': fields.Date(
                required=True,
                description='Data de nascimento no formato yyyy-mm-dd'
            )
        })


    def put(self):
        return self.namespace.model(
            name='pessoa_put',
            model={
            'id': fields.Integer(
                required=True,
                description='Identificador único'
            ),
            'nome': fields.String(
                required=True,
                description='Nome da pessoa'
            ),
            'data_nascimento': fields.Date(
                required=True,
                description='Data de nascimento no formato yyyy-mm-dd'
            )
        })