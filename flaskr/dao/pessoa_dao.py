from flaskr.dao.banco import Banco


class PessoaDao(Banco):
    def __init__(self) -> None:
        super().__init__()


    def _setar(self, linha):
        return {
            'id'              : linha[0],
            'nome'            : linha[1],
            'data_nascimento' : linha[2].strftime('%Y-%m-%d') }


    def todas(self):
        query = """
            SELECT *
            FROM pessoas
            """
        pessoas = []
        for linha in self.selecionar(query):
            pessoas.append(self._setar(linha))
        return pessoas


    def inserir(self, nome, data_nascimento):
        query = """
            INSERT INTO pessoas
                (nome, data_nascimento)
            VALUES
                (%s, %s)
            """
        return self.executar(query, (nome, data_nascimento,))