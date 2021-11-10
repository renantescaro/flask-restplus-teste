from mysql import connector
from flaskr.utils.config import Config


class Banco:
    def __init__(self):
        self.mydb    = connector.connect(
            host     = Config.get('DB_HOST'),
            user     = Config.get('DB_USUARIO'),
            password = Config.get('DB_SENHA'),
            database = Config.get('DB_BANCO') )


    def selecionar(self, query, parametros=None):
        my_cursor = self.mydb.cursor()
        my_cursor.execute(query, parametros)
        return my_cursor.fetchall()


    def executar(self, query, parametros=None):
        try:
            my_cursor = self.mydb.cursor()
            my_cursor.execute(query, parametros)
            self.mydb.commit()
            return True
        except:
            return False