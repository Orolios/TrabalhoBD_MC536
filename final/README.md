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
> [Slides](slides/esb.pdf)

## Modelo Conceitual

> Coloque aqui a imagem do modelo conceitual final em ER ou UML, como o exemplo a seguir:
> ![ER Taxi](images/er-taxi.png)

## Modelos Lógicos

> Coloque aqui os modelos lógicos dos bancos de dados relacionados aos modelos conceituais. Para o modelo relacional, sugere-se o formato a seguir. Para outros modelos lógicos, sugere-se aqueles apresentados em sala.

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

## Dataset Publicado
> Elencar os arquivos/bases preliminares dos datasets serão publicados.

título do arquivo/base | link | breve descrição
----- | ----- | -----
`<título do arquivo/base>` | `<link para arquivo/base>` | `<breve descrição do arquivo/base>`

> Os arquivos finais do dataset publicado devem ser colocados na pasta `data`, em subpasta `processed`. Outros arquivos serão colocados em subpastas conforme seu papel (externo, interim, raw). A diferença entre externo e raw é que o raw é em formato não adaptado para uso. A pasta `raw` é opcional, pois pode ser substituída pelo link para a base original da seção anterior.
> Coloque arquivos que não estejam disponíveis online e sejam acessados pelo notebook. Relacionais (usualmente CSV), XML, JSON e CSV ou triplas para grafos.
> Este é o conjunto mínimo de informações que deve constar na disponibilização do Dataset, mas a equipe pode enriquecer esta seção.

## Bases de Dados
> Elencar as bases de dados fonte utilizadas no projeto.

título da base | link | breve descrição
----- | ----- | -----
`<título da base>` | `<link para a página da base>` | `<breve descrição da base>`

## Detalhamento do Projeto
> Apresente aqui detalhes do processo de construção do dataset e análise. Nesta seção ou na seção de Perguntas podem aparecer destaques de código como indicado a seguir. Note que foi usada uma técnica de highlight de código, que envolve colocar o nome da linguagem na abertura de um trecho com `~~~`, tal como `~~~python`.
> Os destaques de código devem ser trechos pequenos de poucas linhas, que estejam diretamente ligados a alguma explicação. Não utilize trechos extensos de código. Se algum código funcionar online (tal como um Jupyter Notebook), aqui pode haver links. No caso do Jupyter, preferencialmente para o Binder abrindo diretamente o notebook em questão.

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
> Relatório de evolução, descrevendo as evoluções na modelagem do projeto, dificuldades enfrentadas, mudanças de rumo, melhorias e lições aprendidas. Referências aos diagramas, modelos e recortes de mudanças são bem-vindos.
> Podem ser apresentados destaques na evolução dos modelos conceitual e lógico. O modelo inicial e intermediários (quando relevantes) e explicação de refinamentos, mudanças ou evolução do projeto que fundamentaram as decisões.
> Relatar o processo para se alcançar os resultados é tão importante quanto os resultados.

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises

> Apresente os resultados da forma mais rica possível, com gráficos e tabelas. Mesmo que o seu código rode online em um notebook, copie para esta parte a figura estática. A referência a código e links para execução online pode ser feita aqui ou na seção de detalhamento do projeto (o que for mais pertinente).

> Liste aqui as perguntas de pesquisa/análise e respectivas análises. Nem todas as perguntas precisam de queries que as implementam. É possível haver perguntas em que a solução é apenas descrita para demonstrar o potencial da base. Abaixo são ilustradas três perguntas, mas pode ser um número maior a critério da equipe.
>
### Perguntas/Análise com Resposta Implementada

> As respostas às perguntas podem devem ser ilustradas da forma mais rica possível com tabelas resultantes, grafos ou gráficos que apresentam os resultados. Os resultados podem ser analisados e comentados. Veja um exemplo de figura ilustrando uma comunidade detectada no Cytoscape:

> ![Comunidade no Cytoscape](images/cytoscape-comunidade.png)

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
>   * Para descobrir quais são os melhores aplicativos para uma determinada empresa colocar sua publicidade, iremos fazer uma agregação das tabelas Apps e Modelos de Monetização, onde só terá aplicativos com publicidade. Em seguida, iremos fazer uma outra agregação com a tabela criada anteriormente e com a tabela de Categoria para ter somente os Apps com as categorias interresantes para a empresa. Por fim, fazemos outra agregação com a tabela Classificação para obtermos as avaliações dos apps e depois ordenamos de acordo com os critérios: fator de classificação, nota, números de avaliações.

### Pergunta/Análise 5
> *  Levando em consideração a faixa etária e a plataforma, qual a categoria de aplicativo mais baixado por cada público-alvo ?
>   
>   * Primeiro será feito duas agregação com as tabelas Plataforma e Apps para criar duas  tabelas com os apps de Ios e Android separados. Depois, será feito um group by para reunir o total de downloads sobre as faixas etárias para cada plataforma e por fim podemos montar os gráficos para analisar o impacto da idade mínima no desempenho dos aplicativos.

> Coloque um link para o arquivo do notebook que executa o conjunto de queries. Ele estará dentro da pasta `notebook`. Se por alguma razão o código não for executável no Jupyter, coloque na pasta `src`. Se as queries forem executadas atraves de uma interface de um SGBD não executável no Jupyter, como o Cypher, apresente na forma de markdown.
