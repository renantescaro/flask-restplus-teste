import json
from flask import request, jsonify
from flask_restx import Namespace, Resource
from flaskr.models_db.pessoa_model_db import Pessoa, db
from flaskr.models_api.pessoa_model_api import PessoaModelApi
from flaskr.utils.debug import Debug

namespace    = Namespace('pessoas', '')
pessoa_model = PessoaModelApi(namespace)
erro         = json.dumps({'status':False})


@namespace.route('/<int:id>')
class PessoaParametrosApi(Resource):
    @namespace.response(500, erro)
    def get(self, id):
        '''Pessoa por Id'''
        return jsonify(Pessoa.query.filter_by(id=id).first())


    @namespace.response(500, erro)
    def delete(self, id):
        '''Deleta pessoa por Id'''
        pessoa = Pessoa.query.filter_by(id=id).first()
        db.session.delete(pessoa)
        db.session.commit()
        return {'status':True}


@namespace.route('')
class PessoaApi(Resource):
    @namespace.response(500, erro)
    def get(self):
        '''Listagem de pessoas'''
        return jsonify(Pessoa.query.all())


    @namespace.expect(pessoa_model.post(), validate=True)
    @namespace.response(500, erro)
    def post(self):
        '''Insere nova pessoa'''
        pessoa      = Pessoa()
        pessoa.nome = request.json['nome']
        pessoa.data_nascimento = request.json['data_nascimento']

        db.session.add(pessoa)
        db.session.commit()
        return {'status':True}


    @namespace.expect(pessoa_model.put(), validate=True)
    @namespace.response(500, erro)
    def put(self):
        '''Atualiza dados de uma pessoa ja existente'''
        id = request.json['id']
        pessoa:Pessoa = Pessoa.query.filter_by(id=id).first()
        pessoa.nome   = request.json['nome']
        pessoa.data_nascimento = request.json['data_nascimento']

        db.session.commit()
        return {'status':True}