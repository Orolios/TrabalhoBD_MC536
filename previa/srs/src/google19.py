from util import import_csv, get_categorias, id_categorias, categorias_conv_google19, id_plataformas, get_modelo_id
import csv
from math import exp

google_2019_csv_file="../arquivos_csv/googleplaystore.csv"


with open(google_2019_csv_file, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #id_categoria = id_categorias[categorias_conv_google19[row['Category']]]
        id_categoria = 0
        gratis = True if row['Type'] == "Free" else False
        id_modelo = get_modelo_id(publicidade=False, compra_no_app=False, gratuito=gratis)
        id_plataforma=id_plataformas["android"]
        preco = row['Price']
        nome = row['App'].encode('ascii', 'ignore').decode()
        faixa_etaria = row['Content Rating']
        ano = 2019
        download = row['Installs']

        quantid_votos = int(row["Reviews"])
        avaliacao= row["Rating"]

        fator_class =quantid_votos*100/(1+quantid_votos)

        aplicativo_row = [id_categoria, id_modelo, id_plataforma, preco, nome, faixa_etaria, ano, download,quantid_votos,avaliacao,fator_class]

        print(aplicativo_row)
