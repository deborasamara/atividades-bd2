import psycopg2
from psycopg2 import sql
from modelos.classe_contato import Contato

class Conexao:
    
    def __init__(self, nome_db, usuario, senha, host, porta):
        self.nome_db = nome_db
        self.usuario = usuario
        self.senha = senha
        self.host = host
        self.porta = porta
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                database=self.nome_db,
                user=self.usuario,
                password=self.senha,
                host=self.host,
                port=self.porta
            )
            print("Conexão ao banco de dados PostgreSQL realizada com sucesso")
        except OperationalError as e:
            print(f"Ocorreu um erro ao conectar ao banco de dados: {e}")

    # Função para Listar dados dos contatos
    def listar_dados_contatos(self, conn):
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM contatos")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
        except Exception as e:
            print(f"Erro ao ler dados: {e}")
        
    

