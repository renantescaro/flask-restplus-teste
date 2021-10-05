from flask import jsonify, Blueprint

bp = Blueprint(
    'pessoa',
    __name__,
    template_folder='templates' )


class PessoaApi:
    @bp.route('/', methods=['GET'])
    def listagem():
        return jsonify({'pessoas':'aaa'})
    

    @bp.route('/', methods=['POST'])
    def inserir():
        return jsonify({'pessoas':'aaa'})