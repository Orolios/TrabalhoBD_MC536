from util import id_categorias, categorias_conv_apple, id_plataformas, get_modelo_id
import csv
from math import sqrt
from connection import connection


def create_app_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executada!")
    except Error as e:
        print(f"The error '{e}' occurred")



apple_csv_file="../arquivos_csv/AppleStore.csv"

with open(apple_csv_file, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #id_categoria = id_categorias[categorias_conv_apple[row['prime_genre']]]
        id_categoria = 0
        gratis = True if row['price'] == "0" else False
        id_modelo = get_modelo_id(publicidade=False, compra_no_app=False, gratuito=gratis)
        id_plataforma=id_plataformas["ios"]
        preco = row['price']
        nome = row['track_name'].encode('ascii', 'ignore').decode()
        faixa_etaria = row['cont_rating']
        ano = None
        download = None
        quantid_votos = int(row["rating_count_tot"])
        avaliacao= row["user_rating"]
        fator_class =quantid_votos*100/(1+quantid_votos)
        aplicativo_row = [id_categoria, id_modelo, id_plataforma, preco, nome, faixa_etaria, ano, download,quantid_votos,avaliacao,fator_class]
        print(aplicativo_row)
