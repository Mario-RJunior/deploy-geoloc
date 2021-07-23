import psycopg2
import re


class Bd:
    def conectar(self):
        """
        Função para conectar ao servidor.
        """
        try:

            with open('dados-bd-heroku.txt') as f:
                dados = f.readlines()

            dados = [re.findall(': [a-zA-Z0-9\-\.\:/@]+', cont)[0].replace(': ', '').strip() for cont in dados]

            conn = psycopg2.connect(
                database=dados[1],
                host=dados[0],
                user=dados[2],
                password=dados[4])

            return conn

        except psycopg2.Error as e:
            print(f'Erro na conexão ao MySQL Server: {e}.')

    def desconectar(self, conn):
        """
        Função para desconectar do servidor.
        """
        if conn:
            conn.close()

    def listar(self, data):
        """
        Função para listar as informações dos pacientes.
        """

        sql = f"SELECT * FROM visitas WHERE data_visita = '{data}';"

        conn = self.conectar()
        cursor = conn.cursor()
        cursor.execute(sql)
        pacientes = cursor.fetchall()  # Vai pegar o resultado do comando anterior e transformar em uma lista!

        ids = []
        nomes = []
        ruas = []
        numeros = []
        bairros = []
        cidades = []
        estados = []
        datas = []

        if len(pacientes) > 0:

            for paciente in pacientes:
                ids.append(paciente[0])
                nomes.append(paciente[1])
                ruas.append(paciente[2])
                numeros.append(paciente[3])
                bairros.append(paciente[4])
                cidades.append(paciente[5])
                estados.append(paciente[6])
                datas.append(paciente[7])

        else:
            print('Registro não encontrado!')
        self.desconectar(conn)

        return ids, nomes, ruas, numeros, bairros, cidades, estados, datas
