from modelos.classe_contato import Contato
from ConexaoPastas.conexao import Conexao

conn = Conexao("exemplo0511", "postgres", "postgres", "localhost", "5432")
conn.conectar()

if __name__ == "__main__":

    while(True):
        #Menu com funções
        print("1 - Listar dados dos contatos")
        print("2 - parar")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            if conn:
                conn.listar_dados_contatos(conn)
          
        elif opcao == 2:
            break
        else:
            print("Opção inválida")
