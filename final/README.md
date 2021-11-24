# Projeto `Mobile App Analysis`

# Equipe `Esquilos Berrantes` - `ESB`
* `Lucas Jacinto Gonçalves` - `240013`
* `Leonardo Novaes do Nascimento` - `220142`
* `Daniel Mendes dos Santos` - `214752`

## Resumo do Projeto
>  O projeto Mobile App Analysis visa analisar o comportamento das duas maiores plataformas mobile atualmente: Android e iOS através dos aplicativos que são disponibilizados nas respectivas lojas. Através do processamento de ambos os datasets é possível determinar, por exemplo, qual plataforma oferece para uma determinada empresa maior lucratividade na disponibilização dos seus anúncios.  
>  Além disso, é possível observar o comportamento de um aplicativo que possui uma versão paga e outra gratuita como, por exemplo, se a versão paga possui qualidade superior quando comparado com a versão gratuita.  
>  Na plataforma do Android no qual temos os datasets referentes a 2019 e 2021 será possível observar o comportamento dos aplicativos com relação a sua categoria que obtiveram crescimento durante o atual momento de pandemia.

## Slides da Apresentação
> [Slides](slides/esb.pdf)

## Modelo Conceitual
 
> ![Diagrama UML](assets/uml.png)

## Modelos Lógicos

~~~
PLATAFORMA(_Id_, Nome)
CATEGORIA(_Id_, Nome)
APLICATIVO(_Id_, IdCategoria, IdModelo, IdPlataforma, Download, Preço, Nome, FaixaEtaria)
   IdCategoria chave estrangeira -> CATEGORIA(Id)
   IdModelo chave estrangeira -> MODELO_DE_MONETIZACAO(Id)
   IdPlataforma chave estrangeira -> PLATAFORMA(Id)
CLASSIFICACAO(_Id_, IdAplicativo, FatorClassificatorio, QuantidadeVotos, Nota)
   IdAplicativo chave estrangeira -> APLICATIVO(Id)
MODELO_DE_MONETIZACAO(_Id_, Publicidade, Gratuito, CompraNoApp)
~~~

> ![Modelo Lógico Hierárquico](assets/Modelo_hierárquico.png)

## Dataset Publicado
> Elencar os arquivos/bases preliminares dos datasets serão publicados.

título do arquivo/base | link | breve descrição
----- | ----- | -----
`<título do arquivo/base>` | `<link para arquivo/base>` | `<breve descrição do arquivo/base>`

> Os arquivos finais do dataset publicado devem ser colocados na pasta `data`, em subpasta `processed`. Outros arquivos serão colocados em subpastas conforme seu papel (externo, interim, raw). A diferença entre externo e raw é que o raw é em formato não adaptado para uso. A pasta `raw` é opcional, pois pode ser substituída pelo link para a base original da seção anterior.
> Coloque arquivos que não estejam disponíveis online e sejam acessados pelo notebook. Relacionais (usualmente CSV), XML, JSON e CSV ou triplas para grafos.
> Este é o conjunto mínimo de informações que deve constar na disponibilização do Dataset, mas a equipe pode enriquecer esta seção.

## Bases de Dados

título da base | link | breve descrição
----- | ----- | -----
`Google Play Store Apps` | `https://www.kaggle.com/lava18/google-play-store-apps` | `Dataset com 10 mil dados de Aplicativos no Play Store para a análise.`
`Google Play Store Apps` | `https://www.kaggle.com/gauthamp10/google-playstore-apps` | `Dataset com 2.3 milhões de Aplicativos na Play Store para a análise.`
`Mobile App Store ( 7200 apps)` | `https://www.kaggle.com/ramamet4/app-store-apple-data-set-10k-apps` | `Dataset com 7200 dados de Aplicativos no IOs para a análise.`

## Detalhamento do Projeto
> Apresente aqui detalhes do processo de construção do dataset e análise. Nesta seção ou na seção de Perguntas podem aparecer destaques de código como indicado a seguir. Note que foi usada uma técnica de highlight de código, que envolve colocar o nome da linguagem na abertura de um trecho com `~~~`, tal como `~~~python`.
> Os destaques de código devem ser trechos pequenos de poucas linhas, que estejam diretamente ligados a alguma explicação. Não utilize trechos extensos de código. Se algum código funcionar online (tal como um Jupyter Notebook), aqui pode haver links. No caso do Jupyter, preferencialmente para o Binder abrindo diretamente o notebook em questão.
### Teste
~~~python
df = pd.read_excel("/content/drive/My Drive/Colab Notebooks/dataset.xlsx");
sns.set(color_codes=True);
sns.distplot(df.Hemoglobin);
plt.show();
~~~

> Se usar Orange para alguma análise, você pode apresentar uma captura do workflow, como o exemplo a seguir e descrevê-lo:
![Workflow no Orange](images/orange-zombie-meals-prediction.png)

> Coloque um link para o arquivo do notebook, programas ou workflows que executam as operações que você apresentar.

> Aqui devem ser apresentadas as operações de construção do dataset:
* extração de dados de fontes não estruturadas como, por exemplo, páginas Web
* agregação de dados fragmentados obtidos a partir de API
* integração de dados de múltiplas fontes
* tratamento de dados
* transformação de dados para facilitar análise e pesquisa

> Se for notebook, ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src` (por exemplo, arquivos do Orange ou Cytoscape). Se as operações envolverem queries executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.

## Evolução do Projeto
> O Projeto Mobile App Analysis foi escolhido com o objetivo de analisar os aplicativos Android e iOS com relação a vários fatores como: aplicativos mais bem avaliados com relação a sua categoria, relação de aplicativos pagos e gratuitos, quantidade de downloads por plataformas referentes aos apps. Primeiramente pensamos em utilizar o modelo lógico de grafos, porém devido a debates com os membros do grupo sobre a estrutura do arquivo CSV, determinamos que o modelo de documentos seria o candidato ideal, ao contrário do modelo de grafos. Utilizamos também o Modelo Tabular no qual importamos os arquivos brutos do site Kaggle, onde utilizamos operações de construção do nosso dataset sobre esses arquivos em CSV como: tratamento de dados através da exclusão dos aplicativos que não possuem avaliação e quantidade de downloads informados, integração dos dados através da construção de tabelas utilizando SQL e transformação de dados para facilitar a análise e pesquisa. 
> Durante o desenvolvimento do nosso projeto, aprendemos a utilizar bibliotecas para a geração de gráficos que sustentariam nossa análise, bem como aprendemos a utilizar Python com SQL e integrar com o banco de dados que estávamos construindo. 
> Um dos desafios enfrentados pelo nosso grupo durante o processo de modelagem do banco, foi que precisaríamos construir um modelo que permitisse trabalhar com os aplicativos Android e iOS que são de plataformas diferentes e, portanto, precisam ser tratados de forma diferentes. Por exemplo,  criamos uma tabela denominada Plataforma com um ID referente ao Android e outro ao iOS. Essa tabela é utilizada pela tabela Aplicativos e dessa forma, nos possibilitou análises elaboradas envolvendo as duas plataformas para um mesmo aplicativo.
> Para a construção do banco de dados da loja da Google referente ao ano de 2021 limitamos o número de aplicativos para próximo de 10.000, pois devido a gigante quantidade de aplicativos nesta plataforma neste ano, duraria dias para o processamento completo, inviabilizando a entrega do projeto dentro do prazo determinado,  portanto, a limitação sobre a quantidade dos aplicativos construída para esse banco em específico precisou ser imposta.


## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

> Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de detalhamento do projeto (o que for mais pertinente).

> Liste aqui as perguntas de pesquisa/análise e respectivas análises. Nem todas as perguntas precisam de queries que as implementam. É possível haver perguntas em que a solução é apenas descrita para demonstrar o potencial da base. Abaixo são ilustradas três perguntas, mas pode ser um número maior a critério da equipe.
>
### Perguntas/Análise com Resposta Implementada

> As respostas às perguntas podem devem ser ilustradas da forma mais rica possível com tabelas resultantes, grafos ou gráficos que apresentam os resultados. Os resultados podem ser analisados e comentados. Veja um exemplo de figura ilustrando uma comunidade detectada no Cytoscape:

> ![Comunidade no Cytoscape](images/cytoscape-comunidade.png)

#### Pergunta/Análise 1
> * Pergunta 1
>   
>   * Quais são os Top 10 aplicativos mais bem avaliados com suporte para propaganda com relação às categorias às quais eles pertencem ? 

#### Pergunta/Análise 2
> * Pergunta 2
>   
>   * Relacionando aplicativos pagos com os aplicativos gratuitos. 

#### Pergunta/Análise 3
> * Pergunta 3
>   
>   * Levando em consideração a faixa etária e a plataforma no qual o aplicativo pertence, qual a categoria de aplicativo mais baixado por cada público-alvo ? 

### Perguntas/Análise Propostas mas Não Implementadas

#### Pergunta/Análise 1
> * Pergunta 1
>   
>   * Qual a diferença na quantidade de downloads considerando o ano de 2019 (pré-pandemia) e o ano de 2021 (pós-pandemia), considerando as categorias aos quais eles pertencem ?

> Coloque um link para o arquivo do notebook que executa o conjunto de queries. Ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se as queries forem executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.
