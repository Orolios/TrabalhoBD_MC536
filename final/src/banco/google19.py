from util import import_csv, get_categorias, id_categorias, categorias_conv_google19, id_plataformas, get_modelo_id
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

google_2019_csv_file="../arquivos_csv/googleplaystore.csv"

var=0
with open(google_2019_csv_file, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        id_categoria= id_categorias.get(categorias_conv_google19[row['Category']],12)
        id_categoria= int(id_categoria)
        id_categoria+=1
        gratis = True if row['Type'] == "Free" else False

        preco=0
        auxmodel = row['Type']
        if(auxmodel=="Free"):
            id_modelo=1
        if(auxmodel=="Paid"):
            id_modelo=3
            auxpreco = row['Price']
            auxpreco = auxpreco.split("$")[1]
            preco =int(float(auxpreco)*100)
        # print(preco,type(preco))


        # id_modelo = get_modelo_id(publicidade=False, compra_no_app=False, gratuito=gratis)
        id_plataforma=id_plataformas["android"]
        nome = row['App'].encode('ascii', 'ignore').decode()
        faixa_etaria = publico(row['Content Rating'])
        ano = 2019
        auxdownload = row['Installs']
        auxdownload =auxdownload.split("+")
        auxdownload=auxdownload[0].split(",")
        auxdownload="".join(auxdownload)
        download=auxdownload
        download=int(download)
        # print(download, type(download))
        quantid_votos = int(row["Reviews"])
        avaliacao= row["Rating"]
        if(download!=0):
            var=var+quantid_votos/download/10000
        fator_class =quantid_votos*100/(1+quantid_votos)
        aplicativo_row = [id_categoria, id_modelo, id_plataforma, preco, nome, faixa_etaria, ano, download,quantid_votos,avaliacao,fator_class]
        print(aplicativo_row)
        query1 ="INSERT INTO Aplicativo (Nome,preco,ano,download,faixa_etaria,idCategoria,idModelo,idPlataforma) Values('{}',{},{},{},'{}',{},{},{});"
        query2 ="INSERT INTO Class (QuantidadeVotos,fator,nota,idAplicativo) Values({},{},{},{});"
        create_query_database(connection,query1,query2,aplicativo_row)
print(var)
