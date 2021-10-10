from flaskr.dao.banco import Banco
from typing import List


class PessoaDao(Banco):
    def __init__(self) -> None:
        super().__init__()


    def _setar(self, linha):
        return {
            'id'              : linha[0],
            'nome'            : linha[1],
            'data_nascimento' : linha[2].strftime('%Y-%m-%d') }


    def todas(self) -> List:
        query = """
            SELECT *
            FROM pessoas
            """
        pessoas = []
        for linha in self.selecionar(query):
            pessoas.append(self._setar(linha))
        return pessoas


    def inserir(self, nome, data_nascimento) -> bool:
        query = """
            INSERT INTO pessoas
                (nome, data_nascimento)
            VALUES
                (%s, %s)
            """
        return self.executar(query, (nome, data_nascimento,))


    def atualizar(self, id, nome, data_nascimento) -> bool:
        query = """
            UPDATE pessoas
            SET nome = %s, data_nascimento = %s
            WHERE id = %s
            """
        return self.executar(query, (nome, data_nascimento, id,))