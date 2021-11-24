from util import id_categorias, categorias_conv_apple, id_plataformas, get_modelo_id
import csv
from math import sqrt
from connection import connection


def create_query_database(connection, query1, query2,aplicativo_row):
    # aplicativo_row = [id_categoria, id_modelo, id_plataforma, preco, nome, faixa_etaria, ano, download,quantid_votos,avaliacao,fator_class]
    # query2 ="INSERT INTO Class (QuantidadeVotos,fator,nota,idAplicativo) Values({},{},{},{});"
    # query1 ="INSERT INTO Aplicativo (Nome,preco,ano,download,faixa_etaria,idCategoria,idModelo,idPlataforma) Values('{}',{},{},{},{},{},{});"
    if(aplicativo_row[9]=="NaN"):
        return
    try:
        query1=query1.format(aplicativo_row[4],aplicativo_row[3],aplicativo_row[6],aplicativo_row[7],aplicativo_row[5],aplicativo_row[0],aplicativo_row[1],aplicativo_row[2])
        # print(query1,query2)

        cursor = connection.cursor()
        cursor.execute(query1)
        connection.commit()
        id = cursor.lastrowid
        query2=query2.format(aplicativo_row[8],aplicativo_row[10],aplicativo_row[9],id)
        print(query1,query2)
        cursor.execute(query2)
        connection.commit()

    except Exception as e:
        print(f"The error '{e}' occurred")

def publico(case):
    if case == "4+":
        return "Livre"
    elif case == "9+":
        return "Maiores de 10 anos"
    elif case == "12+":
        return "Maiores de 12 anos"
    elif case == "17+":
        return "Maiores de 18 anos"
    else:
        return "Livre"

apple_csv_file="../arquivos_csv/AppleStore.csv"

with open(apple_csv_file, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id_categoria = id_categorias[categorias_conv_apple[row['prime_genre']]]
        id_categoria = int(id_categoria) +1
        gratis = True if row['price'] == "0" else False
        id_plataforma=id_plataformas["ios"]

        auxpreco = row['price']
        if(auxpreco=='0'):
            id_modelo=1
            preco=0
        else:
            id_modelo=3
            auxpreco = auxpreco
            preco =int(float(auxpreco)*100)


        nome = row['track_name'].encode('ascii', 'ignore').decode()
        faixa_etaria = publico(row['cont_rating'])


        ano = 2019
        quantid_votos = int(row["rating_count_tot"])
        download = quantid_votos*25

        avaliacao= float(row["user_rating"])
        fator_class =quantid_votos*100/(1+quantid_votos)
        aplicativo_row = [id_categoria, id_modelo, id_plataforma, preco, nome, faixa_etaria, ano, download,quantid_votos,avaliacao,fator_class]
        # print(aplicativo_row)
        query1 ="INSERT INTO Aplicativo (Nome,preco,ano,download,faixa_etaria,idCategoria,idModelo,idPlataforma) Values('{}',{},{},{},'{}',{},{},{});"
        query2 ="INSERT INTO Class (QuantidadeVotos,fator,nota,idAplicativo) Values({},{},{},{});"
        create_query_database(connection,query1,query2,aplicativo_row)
