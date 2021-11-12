from connection import connection
from util import id_categorias, categorias_conv_apple, id_plataformas, get_modelo_id

def create_query_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executada!")
    except Exception as e:
        print(f"The error '{e}' occurred")

#create plataforma
#
# queries=["DROP TABLE IF EXISTS plataforma;",
# "CREATE TABLE Plataforma(id int NOT NULL PRIMARY KEY,Nome varchar(20) NOT NULL);",
# "CREATE TABLE Categoria(id int NOT NULL PRIMARY KEY,Nome varchar(20) NOT NULL);",
# "CREATE TABLE Class(id int NOT NULL PRIMARY KEY,QuantidadeVotos int,fator DECIMAL(5,2),nota DECIMAL(5,2));",
# "CREATE TABLE ModMon(id int NOT NULL PRIMARY KEY,Publicidade int,Gratuito int, CompraApp int);",
# "CREATE TABLE Aplicativo(id int NOT NULL PRIMARY KEY,Nome varchar(20) NOT NULL,preco DECIMAL(5,2),ano int, download int,faixa_etaria varchar(20),idCategoria int, FOREIGN KEY (idCategoria) REFERENCES Categoria(id),idModelo int,FOREIGN KEY (idModelo) REFERENCES ModMon(id),idPlataforma int,FOREIGN KEY (idPlataforma) REFERENCES Plataforma(id),idClass int,FOREIGN KEY (idClass) REFERENCES Class(id));"
# ]
for categoria in id_categorias.keys():
    query ="INSERT INTO Categoria (id,Nome) Values({},\'{}\');".format(id_categorias[categoria]+1,categoria)
    print(query)
    create_query_database(connection,query)
