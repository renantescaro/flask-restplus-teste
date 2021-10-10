from flask_restplus import Namespace, fields


class PessoaModel:
    def __init__(self, namespace: Namespace) -> None:
        self.namespace = namespace


    def _modelo(self, model):
        return self.namespace.model(
            name='pessoa',
            model=model )


    def post(self):
        return self._modelo({
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
        return self._modelo({
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