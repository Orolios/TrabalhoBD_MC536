import matplotlib.pyplot as plt
import database
from prettytable import PrettyTable

def bar_graphs(tabela, name):
    # Create figure
    figure = plt.figure()
    axes = figure.add_subplot(1, 1, 1)

    # Add title and axis names
    plt.title(name[0])
    plt.xlabel(name[1])
    plt.ylabel(name[2])

    # create the columns
    axes.bar(
        range(len(tabela)),
        [linha[1] for linha in tabela],
        tick_label = [linha[0] for linha in tabela])
    return figure

def bar_graphs_dupla(tabela1, tabela2, name):

    largura = 0.25

    r1 = range(len(tabela1))
    r2 = [x + largura for x in r1]
    # Create figure
    figure = plt.figure(figsize=(10,5))
    axes = figure.add_subplot(1, 1, 1)

    # Add title and axis names
    plt.title(name[0])
    plt.xlabel(name[1])
    plt.ylabel(name[2])
    #plt.ylim([0,5])

    # create the columns
    axes.bar(
        r1,
        [linha[1] for linha in tabela1],
        tick_label = [linha[0] for linha in tabela1],
        width=largura,
        label=name[3])
    axes.bar(
        r2,
        [linha[1] for linha in tabela2],
        tick_label = [linha[0] for linha in tabela2],
        width=largura,
        label=name[4])
    plt.legend()
    return figure


def downloadsModels():
    print()
    select = database.get_downloadsModels()
    print(select,"DASDSDASDASDASDA")
    bar_graphs(select, ["Downloads", "Modelos", "Numero de Downloads"])
    plt.show()

def conteudo_pago_e_gratuito():
    select1, select2 = database.get_faixaEtaria_preco()
    print(select1)
    print(select2)
    bar_graphs_dupla(select1, select2, ["Numero de aplicativos pagos e gratuitos", "Faixa Etaria", "Numero de aplicativos", "Pagos", "Gratuito"])
    plt.show()

def downloadsCategory():
    select = database.get_downloadsCategory()
    print(select)
    bar_graphs(select, ["Downloads", "Categorias", "Numero de Downloads"])
    plt.show()

def Quantidade_Downloads_por_Quantidade_Aplicativos():
    select1, select2 = database.get_downloads_quantidade_aplicativos()
    print(select1)
    print(select2)
    bar_graphs_dupla(select1, select2, ["Numeros de intalações para cada tipo", "Quantidades de Downloas", "Numero de aplicativos", "Pagos", "Gratuito"])
    plt.show()

def Avaliacoes_por_categoria():
    select1 = database.get_avaliacoes_categoria()
    print(select1)
    bar_graphs(select1, ["Numero de avaliacoes por categoria", "categorias", "Numero de avaliacoes"])
    plt.show()

def top10():
    select1 = database.get_top10()
    x = PrettyTable(["Nome", "Avaliação", "Categoria", "Faixa Etária", "Downloads", "Quantidades de avaliações"])
    for i in range(10):
        x.add_row(select1[i])
    print(x)


def comparar_android_ios():
    select1, select2 = database.get_comparar_android_ios()
    x = PrettyTable(["Nome", "Preço no Android", "Nota no Android", "Nota no iOS"])
    for i in range(len(select1)):
        x.add_row(select1[i])
    print(x)
    y = PrettyTable(["Nome", "Preço no iOS", "Nota no Android", "Nota no iOS"])
    for i in range(len(select1)):
        y.add_row(select2[i])
    print(y)

def downloads_faixaEtaria():
    select = database.get_faixaEtaria_Downloads()
    print(select)
    bar_graphs(select, ["Downloads Por Faixa Etária", "Faixa Etária", "Quantidade de Downloads"])
    plt.show()
