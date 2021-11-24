import csv

google_2021_csv_file="../arquivos_csv/Google-Playstore.csv"


def import_csv(filename):
    db_aux=[]
    with open(filename) as csv_file:
        reader=csv.reader(csv_file)
        for row in reader:
            db_aux.append(row)
    return db_aux

def get_categorias(csv, categoria_index):
    categorias = {}
    for i in range(1,len(csv)):
        categorias[csv[i][categoria_index]]=None
    categorias=list(categorias.keys())
    return categorias

def get_modelo_id(publicidade, compra_no_app, gratuito):
    return 2**3*int(publicidade) + 2**2*int(compra_no_app) + 2**1*int(gratuito)

aplicativo = ['Id', 'IdCategorias', 'IdModelo', 'IdPlataforma', 'Preco', 'Nome', 'FaixaEtaria', 'Ano', 'Download']

# evil bit hack pra gerar o dicionario de categoria
# categorias_raw=get_categorias(apple_raw, 12)

# for i, cat in enumerate(categorias_raw):
#     print("\"{}\": {},".format(cat, i))

id_plataformas={"android":1,"ios":2}

cats=[
    "PRODUCTIVITY",
    "PHOTO_VIDEO",
    "ENTERTAINMENT",
    "TRAVEL",
    "SPORTS",
    "FOOD_AND_DRINK",
    "BOOKS",
    "COMMUNICATION",
    "HEALTH_AND_FITNESS",
    "FINANCE",
    "BUSINESS",
    "SOCIAL",
    "OTHERS",
    "NEWS",
    "LIFESTYLE",
    "MEDICAL",
    "GAMES",
    "SHOPPING",
    "MAPS_AND_NAVIGATION",
    "WEATHER",
    "EDUCATION"
]


id_categorias={
    "PRODUCTIVITY": 0,
    "PHOTO_VIDEO": 1,
    "ENTERTAINMENT": 2,
    "TRAVEL": 3,
    "SPORTS": 4,
    "FOOD_AND_DRINK": 5,
    "BOOKS": 6,
    "COMMUNICATION": 7,
    "HEALTH_AND_FITNESS": 8,
    "FINANCE": 9,
    "BUSINESS": 10,
    "SOCIAL": 11,
    "OTHERS": 12,
    "NEWS": 13,
    "LIFESTYLE": 14,
    "MEDICAL": 15,
    "GAMES": 16,
    "SHOPPING": 17,
    "MAPS_AND_NAVIGATION": 18,
    "WEATHER": 19,
    "EDUCATION": 20
}

categorias_conv_apple={
    "Productivity":"PRODUCTIVITY",
    "Photo & Video":"PHOTO_VIDEO",
    "Entertainment":"ENTERTAINMENT",
    "Travel":"TRAVEL",
    "Sports":"SPORTS",
    "Food & Drink":"FOOD_AND_DRINK",
    "Book":"BOOKS",
    "Music":"COMMUNICATION",
    "Health & Fitness":"HEALTH_AND_FITNESS",
    "Finance":"FINANCE",
    "Business":"BUSINESS",
    "Social Networking":"SOCIAL",
    "Utilities":"OTHERS",
    "News":"NEWS",
    "Lifestyle":"LIFESTYLE",
    "Medical":"MEDICAL",
    "Games":"GAMES",
    "Catalogs":"OTHERS",
    "Shopping":"SHOPPING",
    "Navigation":"MAPS_AND_NAVIGATION",
    "Reference":"OTHERS",
    "Weather":"WEATHER",
    "Education":"EDUCATION",
}


categorias_conv_google19 = {
    "ART_AND_DESIGN":"COMMUNICATION",
    "AUTO_AND_VEHICLES":"AUTO_AND_VEHICLES",
    "BEAUTY":"OTHERS",
    "BOOKS_AND_REFERENCE":"BOOKS",
    "BUSINESS":"BUSINESS",
    "COMICS":"OTHERS",
    "COMMUNICATION":"COMMUNICATION",
    "DATING":"OTHERS",
    "EDUCATION":"EDUCATION",
    "ENTERTAINMENT":"ENTERTAINMENT",
    "EVENTS":"OTHERS",
    "FINANCE":"FINANCE",
    "FOOD_AND_DRINK":"FOOD_AND_DRINK",
    "HEALTH_AND_FITNESS":"HEALTH_AND_FITNESS",
    "HOUSE_AND_HOME":"OTHERS",
    "LIBRARIES_AND_DEMO":"BOOKS",
    "LIFESTYLE":"LIFESTYLE",
    "GAME":"GAMES",
    "FAMILY":"OTHERS",
    "MEDICAL":"MEDICAL",
    "SOCIAL":"SOCIAL",
    "SHOPPING":"SHOPPING",
    "PHOTOGRAPHY":"PHOTO_VIDEO",
    "SPORTS":"SPORTS",
    "TRAVEL_AND_LOCAL":"TRAVEL",
    "TOOLS":"OTHERS",
    "PERSONALIZATION":"OTHERS",
    "PRODUCTIVITY":"PRODUCTIVITY",
    "PARENTING":"OTHERS",
    "WEATHER":"WEATHER",
    "VIDEO_PLAYERS":"PHOTO_VIDEO",
    "NEWS_AND_MAGAZINES":"NEWS",
    "MAPS_AND_NAVIGATION":"MAPS_AND_NAVIGATION",
}

categorias_conv_google21 = {
'Adventure':"GAMES",
'Tools':"OTHERS",
'Productivity':"PRODUCTIVITY",
'Communication':"COMMUNICATION",
'Social':"SOCIAL",
'Libraries & Demo':"BOOKS",
'Lifestyle':"LIFESTYLE",
'Personalization':"OTHERS",
'Racing':"GAMES",
'Maps & Navigation':"MAPS_AND_NAVIGATION",
'Travel & Local':"TRAVEL",
'Food & Drink':"FOOD_AND_DRINK",
'Books & Reference':"BOOKS",
'Medical':"MEDICAL",
'Puzzle':"GAMES",
'Entertainment':"ENTERTAINMENT",
'Arcade':"GAMES",
'Auto & Vehicles':"AUTO_AND_VEHICLES",
'Photography':"PHOTO_VIDEO",
'Health & Fitness':"HEALTH_AND_FITNESS",
'Education':"EDUCATION",
'Shopping':"SHOPPING",
'Board':"GAMES",
'Music & Audio':"COMMUNICATION",
'Sports':"SPORTS",
'Beauty':"OTHERS",
'Business':"BUSINESS",
'Educational':"GAMES",
'Finance':"FINANCE",
'News & Magazines':"NEWS",
'Casual':"GAMES",
'Art & Design':"COMMUNICATION",
'House & Home':"OTHERS",
'Card':"GAMES",
'Events':"OTHERS",
'Trivia':"GAMES",
'Weather':"WEATHER",
'Strategy':"GAMES",
'Word':"GAMES",
'Video Players & Editors':"PHOTO_VIDEO",
'Action':"GAMES",
'Simulation':"GAMES",
'Music':"COMMUNICATION",
'Dating':"OTHERS",
'Role Playing':"GAMES",
'Casino':"GAMES",
'Comics':"OTHERS",
'Parenting':"OTHERS",
}

models=[
[0,0,0,"Sem monetização/Sem Sados Suficientes"],
[0,0,1,"Aplicativo focado em comercio"],
[0,1,0,"Aplicativo pago"],
[0,1,1,"Aplicativo pago e com comercio"],
[1,0,0,"Aplicativo focado em Publicidade"],
[1,0,1,"Aplicativo com Publicidade e Comercio"],
[1,1,0,"Aplicativo pago e com Publicidade"],
[1,1,1,"Totalmente Monetizado"],
]


# Estruturacao de quais Modelos existem
# 000 -1
# 001 -2
# 010 -3
# 011 -4
# 100 -5
# 101 -6
# 110 -7
# 111 -8
