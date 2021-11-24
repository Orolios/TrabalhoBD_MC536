from connection import connection
from util import id_categorias, categorias_conv_apple, id_plataformas, get_modelo_id,cats,models

def create_query_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit();
        print("Query executada!")
    except Exception as e:
        print(f"The error '{e}' occurred")

def insert_categorias_database(connection, array):
    cursor = connection.cursor()
    print(array)
    try:
        for x in array:
            query = ("INSERT INTO Categoria (Nome) values('{}');".format(x))
            cursor.execute(query)
        query = ("INSERT INTO Plataforma (Nome) values('{}');".format("Android"))
        cursor.execute(query)
        query = ("INSERT INTO Plataforma (Nome) values('{}');".format("Ios"))
        cursor.execute(query)

        connection.commit()
        print("Queries executada!")

    except Exception as e:
        print(f"The error '{e}' occurred")

def insert_modelos_database(connection, array):
    cursor = connection.cursor()
    try:
        for x in array:
            query = ("INSERT INTO ModMon (Publicidade,Gratuito,CompraApp,Tipo) values({},{},{},'{}');".format(x[0],x[1],x[2],x[3]))
            cursor.execute(query)
        connection.commit()
        print("Queries executada!")

    except Exception as e:
        print(f"The error '{e}' occurred")

queries=[
"CREATE TABLE Plataforma(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,Nome varchar(20) NOT NULL);",
"CREATE TABLE Categoria(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,Nome varchar(20) NOT NULL);",
"CREATE TABLE ModMon(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,Publicidade int,Gratuito int, CompraApp int,Tipo varchar(80));",
"CREATE TABLE Aplicativo(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,Nome varchar(255) NOT NULL,preco DECIMAL(5,2),ano int, download int,faixa_etaria varchar(20),idCategoria int, FOREIGN KEY (idCategoria) REFERENCES Categoria(id) ON DELETE CASCADE,idModelo int,FOREIGN KEY (idModelo) REFERENCES ModMon(id) ON DELETE CASCADE,idPlataforma int,FOREIGN KEY (idPlataforma) REFERENCES Plataforma(id) ON DELETE CASCADE );",
"CREATE TABLE Class(id int NOT NULL AUTO_INCREMENT PRIMARY KEY,QuantidadeVotos int,fator DECIMAL(5,2),nota DECIMAL(5,2),idAplicativo int,FOREIGN KEY (idAplicativo) REFERENCES Aplicativo(id) ON DELETE CASCADE);"
]
for i in queries:
    print(i)
    create_query_database(connection,i)

insert_categorias_database(connection,cats)
insert_modelos_database(connection,models)
