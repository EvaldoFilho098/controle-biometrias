from datetime import datetime
import mysql.connector
from datetime import datetime


class Model:
    def __init__(self):
        self.conn = False               # Conector para fazer a ligação com o banco
        self.cursor = False             # Cursor para executar comandos

    ## CONECTAR BANCO 
    def conectar(self):
        
        try:

            self.conn = mysql.connector.connect(
                host="192.168.99.243",
                port="3306",
                user="Evaldo",
                password="@meta123!",
                database="griaule-db"
            )
            self.cursor = self.conn.cursor()

        except Exception as e:

            print("Não Foi Possivel Estabelecer Conexão com o Banco de Dados!!", e, sep='\n')
            self.conn, self.cursor = False, False
        
    ## DESCONECTAR BANCO
    def desconectar(self):

        if type(self.conn) != bool:
            self.conn.close()
        self.conn = False
        self.cursor = False

    ## EXECUTAR COMANDOS NO BANCO DE DADOS
    def executar(self, comando, return_=False):

        try:
            self.conectar()
            self.cursor.execute(comando)

            if return_ :
                return self.cursor.fetchall()
            else:
                self.conn.commit()

            self.desconectar()

        except Exception as e:

            print("Não Foi Possivel Realizar operação com o Banco de Dados!!", e, sep='\n')
            self.conn, self.cursor = False, False

    ## GERAR A DATA
    def data_atual(self):
        data = datetime.now()
        return data.strftime('%Y-%m-%d')
    
    ## FORMATAR DATA
    def data_formatada(self, data):
        return datetime.strptime(data, '%d/%m/%Y')
    
    ## CADASTRO DO AGR
    def novo_agr(self, nome_agr, cpf_agr):

        comando = "INSERT INTO agrs_cadastrados (nome_agr, cpf_agr, data_cadastro) VALUES (\"{}\", \"{}\", \"{}\")".format(nome_agr.upper(), cpf_agr, self.data_atual())
        
        self.executar(comando)
    
    ## CADASTRO NO GRIAULE
    def cadastro_griaule(self, id_agr):
        
        data = self.data_atual()

        comando = "INSERT INTO agrs_griaule (FK_id_agr, data_cadastro_griaule) VALUES ({}, \"{}\")".format(id_agr, data)
        self.executar(comando)
        comando = "UPDATE agrs_cadastrados SET cadastro_griaule = {} WHERE (id_agr = '{}');".format(1, id_agr)
        self.executar(comando)

    ## CADASTRO DAS BIOMETRIAS
    def cadastro_biometria(self, id_agr):

        data = self.data_atual()

        comando = "INSERT INTO agrs_biometria (FK_id_agr, data_cadastro_biometria) VALUES ({}, \"{}\")".format(id_agr, data)
        self.executar(comando)
        comando = "UPDATE agrs_cadastrados SET cadastro_biometria = {} WHERE (id_agr = '{}');".format(1, id_agr)
        self.executar(comando)
           
    ## CADASTRO DO TREINAMENTO
    def cadastro_treinamento(self, id_agr):
        
        data = self.data_atual()

        comando = "INSERT INTO agrs_treinamento (FK_id_agr, data_cadastro_treinamento) VALUES ({}, \"{}\")".format(id_agr, data)
        self.executar(comando)
        comando = "UPDATE agrs_cadastrados SET cadastro_treinamento = {} WHERE (id_agr = '{}');".format(1, id_agr)
        self.executar(comando)
        
    ## CONTAGEM DE AGRs
    def contagem(self, tabela):
        """Contagem de agrs com determinado staus em determinada ac 

        Args:
            nome_ac (str): nome da ac
            status (str): status para pesquisa

        Returns:
            (int): quantidade encontrada
        """

        comando = "SELECT COUNT(*) FROM {} ".format(tabela)

        return self.executar(comando, True)[0][0]

    ## DELETAR AGR
    def deletar_agr(self, id):

        comando = "DELETE FROM agrs_cadastrados WHERE id_agr = '{}'".format(id)
        self.executar(comando)

    ## GERAR E EXECUTAR SELECT
    def buscar(self, tabela, colunas=None, filtros={}, qtd='todos'):

        comando = "SELECT "

        ## INSERE TODAS AS COLUNAS
        if colunas:
            for coluna in colunas:
                comando += coluna + ","
            comando = comando[:-1] + " FROM " + tabela
        else:
            comando += "* FROM " + tabela

        ## INSERE OS FILTROS
        if filtros != {}:
            comando += " WHERE "

            for item in filtros.items():
                if "nome" in item[0].lower() :
                    comando += "{} LIKE '%{}%' AND ".format(item[0], item[1])
                elif "cpf" in item[0].lower():
                    comando += "{} LIKE '%{}%' AND ".format(item[0], item[1])
                else:
                    comando += str(item[0]) + " = '" + str(item[1]) + "' AND "

            comando = comando[:-5]

        ## EXECUTA
        self.conectar()
        self.cursor.execute(comando)

        ## PEGA RESULTADOS
        if qtd == 'todos':
            lista = []
            for linha in self.cursor.fetchall():
                lista.append(linha)

            return lista

        elif qtd == 'um':
            return self.cursor.fetchone()
        
        ## DESCONECTA 
        self.desconectar()
    
    ## DESFAZ A ETAPA SELECIONADA
    def desfazer_etapa(self, id_agr, etapa):

        comando = "UPDATE agrs_cadastrados SET cadastro_{} = {} WHERE (id_agr = '{}')".format(etapa, 0, id_agr)
        self.executar(comando)
        comando = "DELETE FROM agrs_{} WHERE FK_id_agr = '{}'".format(etapa, id_agr)
        self.executar(comando)
            

