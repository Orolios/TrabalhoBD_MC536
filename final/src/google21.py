from util import import_csv, id_categorias, categorias_conv_google21, id_plataformas, get_modelo_id
import csv
from math import exp
from connection import connection
from util import id_categorias, categorias_conv_google19, id_plataformas, get_modelo_id

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
    if case == "Everyone":
        return "Livre"
    elif case == "Everyone 10+":
        return "Maiores de 10 anos"
    elif case == "Teen":
        return "Maiores de 12 anos"
    elif case == "Mature 17+":
        return "Maiores de 18 anos"
    else:
        return "Livre"

google_2021_csv_file="../arquivos_csv/Google-Playstore.csv"

# categorias_raw=get_categorias(apple_raw, 12)

# for i, cat in enumerate(categorias_raw):
#     print("\"{}\": {},".format(cat, i))

categorias = {}
with open(google_2021_csv_file, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for i,row in enumerate(reader):
        if i==10000:
            break
        id_categoria= id_categorias.get(categorias_conv_google21[row['Category']],12)
        id_categoria= int(id_categoria)
        id_categoria+=1

        if row['Free']=="True":
            gratis=0
        else:
            gratis=1
        if row["Ad Supported"]=="True":
            add=1
        else:
            add=0
        if row["In App Purchases"]=="True":
            compra=1
        else:
            compra=0

        if(add==0 and gratis==0 and compra==0):
            id_modelo=1
        if(add==0 and gratis==0 and compra==1):
            id_modelo=2
        if(add==0 and gratis==1 and compra==0):
            id_modelo=3
        if(add==0 and gratis==1 and compra==1):
            id_modelo=4
        if(add==1 and gratis==0 and compra==0):
            id_modelo=5
        if(add==1 and gratis==0 and compra==1):
            id_modelo=6
        if(add==1 and gratis==1 and compra==0):
            id_modelo=7
        if(add==1 and gratis==1 and compra==1):
            id_modelo=8

        auxpreco=row["Price"]
        preco =int(float(auxpreco)*100)

        id_plataforma=id_plataformas["android"]
        nome = row['App Name'].encode('ascii', 'ignore').decode()
        faixa_etaria = publico(row['Content Rating'])
        ano = 2021

        auxdownload = row['Maximum Installs']
        # auxdownload =auxdownload.split("+")
        # auxdownload=auxdownload[0].split(",")
        # auxdownload="".join(auxdownload)
        # download=auxdownload
        download=int(auxdownload)

        quantid_votos = row["Rating Count"]

        if quantid_votos == "":
            quantid_votos=0
        else:
            quantid_votos=int(quantid_votos)

        avaliacao= row["Rating"]

        if avaliacao == "":
            avaliacao=0
        else:
            avaliacao=float(avaliacao)

        fator_class =quantid_votos*100/(1+quantid_votos)
        aplicativo_row = [id_categoria, id_modelo, id_plataforma, preco, nome, faixa_etaria, ano, download,quantid_votos,avaliacao,fator_class]
        print(i,aplicativo_row)
        query1 ="INSERT INTO Aplicativo (Nome,preco,ano,download,faixa_etaria,idCategoria,idModelo,idPlataforma) Values('{}',{},{},{},'{}',{},{},{});"
        query2 ="INSERT INTO Class (QuantidadeVotos,fator,nota,idAplicativo) Values({},{},{},{});"
        create_query_database(connection,query1,query2,aplicativo_row)
