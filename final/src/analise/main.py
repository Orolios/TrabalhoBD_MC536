import database
import functions

def main ():
    # Analysis of downloads for each monetization model
    functions.downloadsModels()
    functions.downloadsCategory()
    functions.conteudo_pago_e_gratuito()
    functions.Quantidade_Downloads_por_Quantidade_Aplicativos()
    functions.Avaliacoes_por_categoria()
    functions.top10()
    functions.comparar_android_ios()
    functions.downloads_faixaEtaria()

main()
