from mysql import connector
from flaskr.utils.config import Config


class Banco:
    def __init__(self):
        self.mydb    = connector.connect(
            host     = Config.get('host'),
            user     = Config.get('user'),
            password = Config.get('password'),
            database = Config.get('database') )


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