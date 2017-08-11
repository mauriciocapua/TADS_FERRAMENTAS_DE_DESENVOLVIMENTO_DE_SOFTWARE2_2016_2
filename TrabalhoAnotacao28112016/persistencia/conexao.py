import psycopg2


class Conexao:
    def __init__(self):
        # conectei...
        self.con = psycopg2.connect("dbname=teste host=localhost user=postgres password=123")
        # abri o cursor
        self.cur = self.con.cursor()

    def fechar(self):
        # fechando o cursor
        self.cur.close()
        # fechando a conexao
        self.con.close()
