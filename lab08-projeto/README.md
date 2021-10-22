# Equipe `<Esquilos Berrantes>` - `<ESB>`
* `<Lucas Jacinto Gonçalves>` - `<240013>`
* `<Leonardo Novaes do Nascimento>` - `<220142>`
* `<Daniel Mendes dos Santos>` - `<214752>`

## Modelo Lógico Combinado do Banco de Dados de Grafos
> ![Modelo Lógico de Grafo](images/grafo.png)

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

> Liste aqui as perguntas de pesquisa/análise combinadas e revisadas dos membros da equipe e respectivas análises.
>
### Pergunta/Análise 1
> * Pergunta 1:
>   A categoria do aplicativo Android mais bem avaliado (classificado) possui monetização ?
>  * A análise do modelo lógico de grafo referente a essa pergunta se encaixa na modalidade de centralidade, pois um aplicativo Android que é bem avaliado na loja possui um grau de importância significativa em comparação com outros aplicativos de mesma categoria que não são tão bem avaliados, por exemplo. Ou seja, a partir das conexões dos aplicativos do grafo que fazem parte de uma mesma categoria eu possuo um app que possui maior importância ou que sua importância se destaque frente aos outros apps. 

### Pergunta/Análise 2
> * Pergunta 2:
>   Qual é a diferença no número de instalações para cada categoria entre aplicativos monetizados e não monetizados?
>   * A análise do modelo lógico de grafo referente a essa pergunta, assim como o da pergunta acima, se encaixa na modalidade de centralidade,uma vez que, o app Android é um nó com  betweenness centrality e closeness centrality, logo, ratifica-se sua importância ao se tratar os dados analizados nas extremidades. Nesse sentido, para chegarmos em uma resposta para essa questão precisa-se por intermédio desse nó estabelecer a relação entre essas extremidades. 
  Diante disso, pode-se futuramente remodelar esse modelo combinado de grafo a fim descentraliza-lo e liberá-lo dessa da dependência desse nó, como por exemplo, a criação de relacionamentos 1 a 1 das extremidades a aumentar a modularidade e os motifs do modelo de forma a torná-lo mais legível e interpretável.

 
### Pergunta/Análise 3
> * Pergunta 3: 
>   Qual categoria tem o maior ganho de dinheiro para cada plataforma?
>   
>   *Para essa análise pode ser utilizada a rede complexa na imagem onde podemos identificar comunidades de aplicativos. Estas são delimitadas pelo nó que indica a plataforma
>   dos aplicativos e pelo nó da categoria referente aquela comunidade (esse seria o senso mais forte). Logo, podemos analisar cada comunidade isoladamente para encontrar o
>   total de dinheiro ganho em cada categoria das plataformas. Por fim, podemos comparar os resultados.
