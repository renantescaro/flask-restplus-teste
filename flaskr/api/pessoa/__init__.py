import json
from flask import request
from flask_restx import Namespace, Resource
from flaskr.dao.pessoa_dao import PessoaDao
from flaskr.model.pessoa_model import PessoaModel
from flaskr.utils.debug import Debug

namespace    = Namespace('pessoas', '')
pessoa_model = PessoaModel(namespace)
erro         = json.dumps({'status':False})


@namespace.route('/<int:id>')
class PessoaParametrosApi(Resource):
    @namespace.response(500, erro)
    def get(self, id):
        '''Pessoa por Id'''
        return PessoaDao().por_id(id)
    
    @namespace.response(500, erro)
    def delete(self, id):
        '''Deleta pessoa por Id'''
        status = PessoaDao().deletar_por_id(id)
        return {'status':status}


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
        return {'status':status}


    @namespace.expect(pessoa_model.put(), validate=True)
    @namespace.response(500, erro)
    def put(self):
        '''Atualiza dados de uma pessoa ja existente'''
        id   = request.json['id']
        nome = request.json['nome']
        data_nascimento = request.json['data_nascimento']

        status = PessoaDao().atualizar(id, nome, data_nascimento)
        return {'status':status}