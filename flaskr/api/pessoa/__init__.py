import json
from flask import request
from flask_restplus import Namespace, Resource
from flaskr.dao.pessoa_dao import PessoaDao
from flaskr.model.pessoa_model import PessoaModel
from flaskr.utils.debug import Debug

namespace    = Namespace('pessoas', '')
pessoa_model = PessoaModel(namespace)
erro         = json.dumps({'status':False})


@namespace.route('')
class PessoaApi(Resource):
    @namespace.response(500, erro)
    def get(self):
        '''Listagem de pessoas'''
        return PessoaDao().todas()


    @namespace.expect(pessoa_model.post(), validate=True)
    @namespace.response(500, erro)
    def post(self):
        '''Insere nova pessoa'''
        nome = request.json['nome']
        data_nascimento = request.json['data_nascimento']

        status = PessoaDao().inserir(nome, data_nascimento)
        return json.dumps({'status', status})