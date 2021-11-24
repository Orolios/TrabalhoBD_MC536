from connection import connection

# connecting to the database

# cursor
crsr = connection.cursor()

# print statement will execute if there
# are no errors
print("Connected to the database")

excluir_Apps_ios_free = """DROP VIEW IF EXISTS Apps_ios_free;"""
excluir_Apps_ios_pagos = """DROP VIEW IF EXISTS Apps_ios_pagos;"""
excluir_Apps_adroids_pagos = """DROP VIEW IF EXISTS Apps_adroids_pagos;"""
excluir_Apps_2019 = """DROP VIEW IF EXISTS Apps_2019;"""
excluir_Apps_adroids_free = """ DROP VIEW IF EXISTS Apps_adroids_free;"""

# execute the statement
crsr.execute(excluir_Apps_2019)
crsr.execute(excluir_Apps_ios_pagos)
crsr.execute(excluir_Apps_ios_free)
crsr.execute(excluir_Apps_adroids_pagos)
crsr.execute(excluir_Apps_adroids_free)




view_q2 = """
CREATE VIEW Apps_2019 AS
SELECT Aplicativo.id, Aplicativo.nome, Aplicativo.Idcategoria, Aplicativo.download, Class.nota, Class.quantidadeVotos, Class.fator
FROM Aplicativo, Class
WHERE Aplicativo.ano = '2019' AND Aplicativo.id = Class.idAplicativo AND Aplicativo.idPlataforma = '0';
"""
select_Android_pagos = """
CREATE VIEW Apps_adroids_pagos AS
SELECT Aplicativo.nome, Aplicativo.preco, Class.fator AS Nota_Android
FROM Aplicativo, Class
WHERE Aplicativo.idPlataforma = 0 AND Class.idAplicativo = Aplicativo.id AND Aplicativo.preco <> 0;
"""
select_ios_free = """
CREATE VIEW Apps_ios_free AS
SELECT Aplicativo.nome, Class.fator AS Nota_Ios
FROM Aplicativo, Class
WHERE Aplicativo.idPlataforma = 1 AND Class.idAplicativo = Aplicativo.id AND Aplicativo.preco = 0;
"""
select_android_free = """
CREATE VIEW Apps_adroids_free AS
SELECT Aplicativo.nome, Class.fator AS Nota_Android
FROM Aplicativo, Class
WHERE Aplicativo.idPlataforma = 0 AND Class.idAplicativo = Aplicativo.id AND Aplicativo.preco = 0;
"""
select_ios_pago ="""
CREATE VIEW Apps_ios_pagos AS
SELECT Aplicativo.nome, Aplicativo.preco, Class.fator AS Nota_Ios
FROM Aplicativo, Class
WHERE Aplicativo.idPlataforma = 1 AND Class.idAplicativo = Aplicativo.id AND Aplicativo.preco <> 0;
"""
crsr.execute(view_q2)
crsr.execute(select_Android_pagos)
crsr.execute(select_ios_free)
crsr.execute(select_android_free)
crsr.execute(select_ios_pago)

connection.commit()

# Criando as queries para cada avaliação.

select_top10 = """
SELECT Aplicativo.nome, Class.fator, Categoria.Nome, Aplicativo.faixa_etaria, Aplicativo.download, Class.quantidadeVotos
FROM Aplicativo, Class, Categoria
WHERE Aplicativo.id = Class.idAplicativo AND Aplicativo.idCategoria = Categoria.id
ORDER BY Class.fator DESC, Class.quantidadeVotos DESC, Class.nota DESC
LIMIT 1, 10;
"""
select_comparar_android_pago = """SELECT Apps_adroids_pagos.nome, Apps_adroids_pagos.preco, Apps_adroids_pagos.Nota_Android, Apps_ios_free.Nota_Ios
FROM Apps_adroids_pagos, Apps_ios_free
WHERE Apps_adroids_pagos.nome = Apps_ios_free.nome;
"""
select_comparar_ios_pago = """
SELECT Apps_adroids_free.nome, Apps_ios_pagos.preco, Apps_adroids_free.Nota_Android, Apps_ios_pagos.Nota_Ios
FROM Apps_adroids_free, Apps_ios_pagos
WHERE Apps_adroids_free.nome = Apps_ios_pagos.nome;
"""
select_conteudo_pago_pFaixa = """
SELECT Aplicativo.faixa_etaria, COUNT(*)
FROM Aplicativo
WHERE Aplicativo.preco <> 0
GROUP BY Aplicativo.faixa_etaria;
"""
select_conteudo_gratuito_pFaixa = """
SELECT Aplicativo.faixa_etaria, COUNT(*)
FROM Aplicativo
WHERE Aplicativo.preco = 0
GROUP BY Aplicativo.faixa_etaria;
"""
select_conteudo_paga_pQuantidadeDownloads = """
SELECT Aplicativo.download, COUNT(*)
FROM Aplicativo
WHERE Aplicativo.preco <> 0
GROUP BY Aplicativo.faixa_etaria;
"""
select_conteudo_gratuito_pQuantidadeDownloads = """
SELECT Aplicativo.download, COUNT(*)
FROM Aplicativo
WHERE Aplicativo.preco = 0
GROUP BY Aplicativo.faixa_etaria;
"""
select_avaliacoes_categoria = """
SELECT categoria.nome, SUM(Class.quantidadeVotos)
FROM Aplicativo, categoria, Class
WHERE Aplicativo.idCategoria = categoria.id AND Class.idAplicativo = Aplicativo.id
GROUP BY categoria.nome;
"""
select_downloads_categorias = """
SELECT categoria.nome AS Categorias, SUM(Apps_2019.download) AS Donwloads
FROM Apps_2019, categoria
WHERE Apps_2019.Idcategoria = categoria.id
GROUP BY Apps_2019.Idcategoria;
"""
select_downloads_modelos = """
SELECT Ap.idModelo AS Modelo, SUM(Ap.download) AS Downloads
FROM Aplicativo Ap
GROUP BY Ap.idModelo;
"""
select_faixaEtaria_Downloads = """
SELECT A.faixa_etaria, SUM(A.download)
FROM Aplicativo A
GROUP BY A.faixa_etaria;
"""

print(connection.cursor().execute(select_top10))
def get_faixaEtaria_Downloads():
    cursor=connection.cursor()
    return cursor.execute(select_faixaEtaria_Downloads)

def get_comparar_android_ios():
    cursor=connection.cursor()
    return cursor.execute(select_comparar_android_pago), connection.execute(select_comparar_ios_pago)

def get_top10():
    cursor=connection.cursor()
    return cursor.execute(select_top10)

def get_faixaEtaria_preco():
    cursor=connection.cursor()
    return cursor.execute(select_conteudo_pago_pFaixa), connection.execute(select_conteudo_gratuito_pFaixa)

def get_downloadsModels():
    print(connection,"Aqui carai")
    cursor=connection.cursor()
    return cursor.execute(select_downloads_modelos).fetchall()

def get_downloadsCategory():
    return cursor.execute(select_downloads_categorias)

def get_downloads_quantidade_aplicativos():
    return cursor.execute(select_conteudo_paga_pQuantidadeDownloads), connection.execute(select_conteudo_gratuito_pQuantidadeDownloads)

def get_avaliacoes_categoria():
    return cursor.execute(select_avaliacoes_categoria)
