# Modelo de Apresentação da Entrega Prévia

# Estrutura de Arquivos e Pastas

A estrutura aqui apresentada é uma simplificação daquela proposta pelo [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/). Também será aceito que o projeto adote a estrutura completa do Cookiecutter Data Science e isso será considerado um diferencial. A estrutura geral é a seguinte e será detalhada a seguir:

~~~
├── README.md  <- arquivo apresentando a proposta
│
├── data
│   ├── external       <- dados de terceiros em formato usado para entrada na transformação
│   ├── interim        <- dados intermediários, e.g., resultado de transformação
│   ├── processed      <- dados finais usados para a publicação
│   └── raw            <- dados originais sem modificações
│
├── notebooks          <- Jupyter notebooks ou equivalentes
│
├── slides             <- arquivo de slides em formato PDF
│
├── src                <- fonte em linguagem de programação ou sistema (e.g., Cytoscape)
│   └── README.md      <- instruções básicas de instalação/execução
│
└── assets             <- mídias usadas no projeto
~~~

Na raiz deve haver um arquivo de nome `README.md` contendo a apresentação do projeto, como detalhado na seção seguinte.

## `data`

Arquivos de dados usados no projeto, quando isso ocorrer.

## `notebooks`

Testes ou prototipos relacionados ao projeto que tenham sido executados no Jupyter.

## `src`

Projeto na linguagem escolhida, incluindo todos os arquivos de dados e bibliotecas necessários para a sua execução. Dentro dessa pasta sugerimos que você mantenha uma estrutura equivalente ao Eclipse, com uma subpasta `src` onde estarão os fontes e outra subpasta `bin` onde estarão os binários.

 Acrescente na raiz um arquivo `README.md` com as instruções básicas de instalação e execução.

## `assets`

Qualquer mídia usada no seu projeto: vídeo, imagens, animações, slides etc. Coloque os arquivos aqui (mesmo que você mantenha uma cópia no diretório do código).

# Modelo para Apresentação da Entrega Prévia do Projeto

# Projeto `<Mobile App Analysis>`

# Equipe `<Esquilos Berrantes>` - `<ESB>`
* `<Lucas Jacinto Gonçalves>` - `<240013>`
* `<Leonardo Novaes do Nascimento>` - `<220142>`
* `<Daniel Mendes dos Santos>` - `<214752>`

## Resumo do Projeto
>  O projeto Mobile App Analysis visa analisar o comportamento das duas maiores plataformas mobile atualmente: Android e iOS através dos aplicativos que são disponibilizados nas respectivas lojas. Através do processamento de ambos os datasets é possível determinar, por exemplo, qual plataforma oferece para uma determinada empresa maior lucratividade na disponibilização dos seus anúncios.  
>  Além disso, é possível observar o comportamento de um aplicativo que possui uma versão paga e outra gratuita como, por exemplo, se a versão paga possui qualidade superior quando comparado com a versão gratuita.  
>  Na plataforma do Android no qual temos os datasets referentes a 2019 e 2021 será possível observar o comportamento dos aplicativos com relação a sua categoria que obtiveram crescimento durante o atual momento de pandemia.

## Slides da Apresentação
> Coloque aqui o link para o PDF da apresentação prévia

## Modelo Conceitual Preliminar

> Coloque aqui a imagem do modelo conceitual preliminar em ER ou UML, como o exemplo a seguir:
> ![Diagrama UML](assets/uml.png)

## Modelos Lógicos Preliminares

> Coloque aqui os primeiros modelos lógicos dos bancos de dados relacionados aos modelos conceituais. Para o modelo relacional, sugere-se o formato a seguir. Para outros modelos lógicos o formato é livre, pode ser adotado aqueles apresentados em sala.

> Exemplo de modelo lógico relacional
~~~
PESSOA(_Código_, Nome, Telefone)
ARMÁRIO(_Código_, Tamanho, Ocupante)
  Ocupante chave estrangeira -> PESSOA(Código)
~~~

> Para o modelo de grafos de propriedades, utilize este
> [modelo de base](https://docs.google.com/presentation/d/10RN7bDKUka_Ro2_41WyEE76Wxm4AioiJOrsh6BRY3Kk/edit?usp=sharing) para construir o seu.
> Coloque a imagem do PNG do seu modelo lógico como ilustrado abaixo (a imagem estará na pasta `image`):
>
> ![Modelo Lógico de Grafos](images/modelo-logico-grafos.png)

> Para o modelo de grafos de conhecimento, utilize a abordagem
> (recurso, propriedade, valor) para apresentar seu grafo exemplo.
> Coloque a imagem do PNG do seu modelo lógico como ilustrado abaixo (a imagem estará na pasta `image).
>
> Você pode usar um grafo ilustrando as classes, como este:
> ![Modelo Lógico de Grafos de Conhecimento](images/grafo-conhecimento-classes.png)
>
> Além de outro com exemplo de instâncias, como este:
> ![Modelo Lógico de Grafos](images/grafo-conhecimento-exemplo.png)

> Para modelos hierárquicos (XML e JSON), utilize um formato
> conforme o abaixo:

> ![Modelo Lógico Hierárquico](images/modelo-logico-hierarquico.png)

## Dataset Preliminar a ser Publicado
> Elencar os arquivos/bases preliminares dos datasets serão publicados publicados.

título do arquivo/base | link | breve descrição
----- | ----- | -----
`<título do arquivo/base>` | `<link para arquivo/base>` | `<breve descrição do arquivo/base>`

> Os arquivos finais do dataset publicado devem ser colocados na pasta `data`, em subpasta `processed`. Outros arquivos serão colocados em subpastas conforme seu papel (externo, interim, raw). A diferença entre externo e raw é que o raw é em formato não adaptado para uso. A pasta `raw` é opcional, pois pode ser substituída pelo link para a base original da seção anterior.
> Coloque arquivos que não estejam disponíveis online e sejam acessados pelo notebook. Relacionais (usualmente CSV), XML, JSON e CSV ou triplas para grafos.

## Bases de Dados
> Elencar as bases de dados fonte utilizadas no projeto.

título da base | link | breve descrição
----- | ----- | -----
`<título da base>` | `<link para a página da base>` | `<breve descrição da base>`

## Operações realizadas para a construção do dataset

> Coloque um link para o arquivo do notebook, programas ou workflows que executam as operações de construção do dataset:
* extração de dados de fontes não estruturadas como, por exemplo, páginas Web
* agregação de dados fragmentados obtidos a partir de API
* integração de dados de múltiplas fontes
* tratamento de dados
* transformação de dados para facilitar análise e pesquisa

> Se for notebook, ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se as operações envolverem queries executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

> Liste aqui as perguntas de pesquisa/análise e respectivas análises.
> Nem todas as perguntas precisam de queries que as implementam.
> É possível haver perguntas em que a solução é apenas descrita para
> demonstrar o potencial da base.
>
### Pergunta/Análise 1
> * Qual a diferença na quantidade de downloads considerando o ano de 2019 (pré-pandemia) e o ano de 2021 (pós-pandemia), considerando as categorias aos quais eles pertencem ?
>   
>   *  Primeiramente, a diferença na quantidade de downloads só será possível considerando a plataforma Android, uma vez que o dataset da plataforma do iOS só está disponível no ano de 2019. Dito isso, utilizando a tabela Plataforma no qual escolhemos o Android para fazer essa análise, iremos para a tabela de Aplicativos, já que uma Plataforma pode ter inúmeros aplicativos. Na tabela Aplicativos, eu seleciono o ano de 2019 e vejo a quantidade de downloads neste ano para uma determinada Categoria, por exemplo, Games. De maneira semelhante, selecionamos o ano de 2021 e pegamos a informação da quantidade de downloads neste ano. 
Por fim, para ver a análise do crescimento na quantidade de downloads considerando os anos de 2019 e 2021 de cada categoria, é realizado a divisão da quantidade de downloads do ano de 2021 pela quantidade de downloads no ano de 2019.


### Pergunta/Análise 2
> * Qual a diferença entre o fator de avaliação (normalização) entre o mesmo aplicativo no sistema Android e iOS, porém que seja pago em um sistema e gratuito em outro ?
>   
>   *  Para descobrir o fator de avaliação de um aplicativo, primeiramente iremos selecionar os Aplicativos do Android ou iOS e, em seguida,  iremos selecionar o Modelo de Monetização, mais especificamente, se um aplicativo é gratuito ou não. A partir disso, é realizada uma busca desse aplicativo na loja concorrente com o intuito de descobrir um modelo de monetização diferente para esse app, ou seja, gratuito em uma plataforma e pago em outra ou vice-versa.  Realizado a busca desse aplicativo, iremos selecionar a classificação dele com relação ao fator normativo.  Esse fator normativo de cada plataforma será comparado e a partir disso, poderemos ver se existe alguma relação no fato do aplicativo ser pago e qual o impacto disso na qualidade do produto que é oferecido ao usuário.

### Pergunta/Análise 3
> * Levando em consideração o suporte a publicidade, a monetização do aplicativo e a presença de compras dentro dos aplicativos, qual o método mais rentável de monetização ?
>   
>   * Para descobrir qual é o método de monetização mais eficiente, precisamos fazer a agregação das tabelas Apps com a tabela de Modelos de Monetização para todos terem seus respectivos modelos. Depois, podemos montar gráficos mostrando quais métodos possuem as maiores quantidades de downloads e melhores avaliações e fazer uma análise de quais métodos podem render mais monetização  . 

### Pergunta/Análise 4
> * Top 10 melhores aplicativos com suporte para propaganda para determinada empresa de um ramo específico (categoria)
>   
Para descobrir quais são os melhores aplicativos para uma determinada empresa colocar sua publicidade, iremos fazer uma agregação das tabelas Apps e Modelos de Monetização, onde só terá aplicativos com publicidade. Em seguida, iremos fazer uma outra agregação com a tabela criada anteriormente e com a tabela de Categoria para ter somente os Apps com as categorias interresantes para a empresa. Por fim, fazemos outra agregação com a tabela Classificação para obtermos as avaliações dos apps e depois ordenamos de acordo com os critérios: fator de classificação, nota, números de avaliações.

### Pergunta/Análise 5
> *  Levando em consideração a faixa etária e a plataforma, qual a categoria de aplicativo mais baixado por cada público-alvo ?
>   
>   * Explicação sucinta da análise que será feita ou conjunto de queries que
>     responde à pergunta.


> Coloque um link para o arquivo do notebook que executa o conjunto de queries. Ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se as queries forem executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.
