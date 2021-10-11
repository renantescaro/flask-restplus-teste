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
    

    def por_id(self, id:int):
        query = """
            SELECT *
            FROM pessoas
            WHERE id = %s
            """
        retorno_bd = self.selecionar(query, (id,))
        if len(retorno_bd) > 0:
            return self._setar(retorno_bd[0])
        return None


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
    

    def deletar_por_id(self, id):
        query = """
            DELETE FROM pessoas
            WHERE id = %s 
            """
        return self.executar(query, (id,))