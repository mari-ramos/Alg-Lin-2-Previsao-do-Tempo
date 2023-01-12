# Álgebra Linear 2 - Trabalho de Previsão do Tempo
Mariana Ramos, maribramos@poli.ufrj.br.<br>
Prof: Marcello L. R. de Campos. <br>
Universidade Federal do Rio de Janeiro, Rio de Janeiro, Brasil.<br>
<hr>

### **RESUMO**
<p> Este trabalho contempla a utilização de métodos provenientes da disciplina de Álgebra Linear 2, combinados a módulos e ferramentas open source da linguagem de programação Python aplicados às bases de dados oferecidas referentes a medições influentes à ocorrência de chuva em Sydney, Austrália, de forma simplificada, sucinta, levando em consideração valores de acurácia e precisão. O método utilizado para a regressão linear foi o de mínimos quadrados, junto ao numpy, pandas e sklearn, ferramentas da linguagem Python, utilizadas através do VSCode, para a construção do código para a obtenção da solução, salva em formato .csv, com um r2 de aproximadamente 0,39, uma precisão de aproximadamente 81% e uma acurácia de 82%.</p>

### **INTRODUÇÃO**

<p> Este relatório tem como objetivo relatar o desenvolvimento do sistema e a solução encontrada para resolver o problema apresentado, sendo este a chance de ocorrência de chuva no dia seguinte à última amostra, o dia 26 de Junho do ano de 2017, em Sydney, Austrália. Foram fornecidas duas bases de dados, uma de treinamento e outra de teste, com diversos tipos de dados entre os anos de 2008 e 2017 que influenciam na ocorrência de chuva. </p>

### **DESENVOLVIMENTO DO SISTEMA**

<p> A partir das bases de dados apresentadas, uma de teste e outra de treinamento, junto ao método dos mínimos quadrados, foi possível tratar o problema abordado. Levando como base os conhecimentos adquiridos na disciplina de Álgebra Linear 2, mais especificamente do método dos mínimos quadrados, através da equação normal, $\ θ = (X^T*X^-1)*(X^T*Y)$, a qual tem como definição encontrar parâmetros de hipótese, através de dados de entrada e dados de saída. Baseado nisso, o próximo passo foi definir quais colunas seriam relevantes para o método, a atribuição de valores para elementos que não fossem numéricos, como “NA” (Not Applicable), “Yes”, “No” e os dezesseis tipos de direção do vento e a definição de quais colunas seriam utilizadas como dados de entrada e dados de saída.</p>

<p> Através da análise das colunas, foi possível concluir que as colunas de “Data” e “Localização” não seriam necessárias na implementação da equação normal, uma vez que se seus valores fossem levados em consideração na equação, não teriam uma influência significativa no resultado final, em sua acurácia e nem em sua precisão, o fato do analisador saber que as medições foram feitas em dias sucessivos e em um mesmo local já é o suficiente para achar a solução. Para os elementos não numéricos, o valor atribuído para os dados classificados como “NA” foi o número 0, para “Yes”, foi utilizado o número 1, para o “No”, foi o número 0, e para as dezesseis direções do vento, foi utilizado os ângulos formados por cada uma delas, de 0 a 337.5, com um intervalo de 22.5. Após a retirada das colunas de “Data” e “Localização” e da atribuição de valores para dados não numéricos, as colunas “MinTemp”, “MaxTemp”, “Rainfall”, “Evaporation”, “Sunshine”, “WinndGustDir”, “WindGustSpeed”, “WindDir9am”, “WindDir3pm”, “WindSpeed9am”, “WindSpeed3pm”, “Humidity9am”, “Humidity3pm”, “Pressure9am”, “Pressure3pm”, “Cloud9am”, “Cloud3pm”, “Temp9am”, “Temp3pm” e “RainToday” foram denominadas como dados de entrada nas duas bases de dados, uma vez que são os dados obtidos através das medições. Para uma coluna ser classificada como um dado de saída, ela tem que possuir as informações que o analisador quer saber, são as respostas para o problema, a partir disso fica evidente que os dados correspondentes a se choveu no dia seguinte às medições ou não fazem parte dos dados de saída. </p>

<p>A etapa seguinte para o desenvolvimento do sistema foi a de definir a melhor maneira de lidar com as duas bases de dados e como inserir os dados na equação normal para achar a resolução do problema. Foi observado que em ambas as planilhas fornecidas há o mesmo número de colunas de dados de entrada, todavia apenas na de treinamento, a denominada “weatherAUS_training.csv”, há dados de saída. A partir disso foi desenvolvido um programa para lidar da melhor maneira com as planilhas, utilizando o método de mínimos quadrados e, consequentemente, achar a solução do problema, o qual é se vai chover no dia seguinte à última medição ou não.</p>

<p>Para elaborar o programa foi utilizada a linguagem de alto nível, Python, por ser próxima da linguagem humana, flexível e muito utilizada, com grandes contribuições da comunidade e uma infinidade de módulos eficientes. No código foi utilizado o numpy, uma biblioteca voltada para operações com matrizes, o pandas, uma outra biblioteca utilizada como ferramenta para manipulação de dados assim como para análise de dados e o sklearn, outra ferramenta voltada para análise de dados. Foi implementado os comandos referentes às primeiras etapas do processo, já detalhadas, como a retirada de colunas e substituição de valores. Após isso, foi denominado os dados de entrada e saída na base de dados de treinamento, onde foi criada as variáveis “y_train” para os dados de saída, correspondentes a coluna “RainTomorrow”, e “x_train” para os dados de entrada, todas as colunas utilizadas menos a “RainTomorrow”, depois disso, foi executada a equação normal para achar os parâmetros de hipótese ou, como foi denominado no código, o coeficiente (coefficients) através do numpy: coefficients = np. linalg. inv(x_train. T. dot(x_train)). dot(x_train. T). dot(y_train), sendo esta uma equação de solução única, uma vez que ela tem solução e o parâmetro de hipótese, ou coeficiente, possui inversa pela esquerda, sendo pelo menos uma função injetiva, a qual possui o número 0 como único elemento pertencente ao conjunto do espaço nulo. Após ser obtido o valor do coeficiente, ele foi multiplicado pelos dados de entrada, x_train, utilizando também o numpy, para a predição de chuva nos dias seguintes às medições, valor atribuído à variável “y_predict” e a uma nova coluna denominada “RainTomorrow_predict” com valores menores que 0 a maiores que 1, e que através de uma análise foi classificado que valores menores que 0,5 são sinônimo de que não teria ocorrência de chuvas e maiores ou iguais a 0,5 como um indicador de que teria chuva no dia seguinte. Esta nova coluna foi criada com a finalidade de ter a acurácia e precisão do método utilizado ao compará-la com a coluna “RainTomorrow” e o número de acertos.</p>

<p>Como as medições das duas tabelas são feitas sucessivamente e em um mesmo local, possuindo o mesmo número de colunas nos dados de entrada, foi utilizado para a obtenção dos dados de saída do arquivo de teste, que nada mais são do que a solução do problema, a mesma lógica para a criação de uma nova coluna, a “RainTomorrow_predict” para o arquivo de treinamento. Para isso, no arquivo de treinamento, foi criada uma nova coluna “Rain Tomorrow”, a qual foi utilizado todos os dados provenientes da coluna “RainToday”, com exceção da primeira linha, ficando com 175 dados copiados e 1 dado inserido manualmente, o elemento da última linha, correspondendo a 176 dias, a partir disso foi multiplicado os dados de entrada pelo coeficiente adquirido pelos dados de treinamento para a obtenção da predição e o estabelecimento da nova coluna, solução do problema, “RainTomorrow_predict”, definido em 0, para a não ocorrência de chuvas, e 1 para a ocorrência de chuvas, seguindo o mesmo padrão estabelecido para os dados de treinamento. Sendo este, o produto gerado, uma coluna com 176 linhas com dados de predição de chuva, com 1’s e 0’s, que ao ser comparado com a coluna “RainTomorrow”, utilizando os comandos de acurácia e precisão do sklearn, fica evidente o desempenho do método e da execução do programa.</p>

### **RESULTADOS**

<p>Com base no método dos mínimos quadrados, a implementação da equação normal através do numpy, umas das bibliotecas utilizadas para a construção do programa em Python, estabelecido para a solução do problema da previsão da ocorrência de chuvas aos dias seguintes das amostras presentes do arquivo de teste fornecido, foi criado uma nova coluna de predição onde os valores maiores ou iguais a 0,5 foram considerados como um “Sim”, que terá ocorrência de chuva, sendo atribuído o valor 1 e os valores menores que 0,5 foram considerados como um “Não”, que não terá uma ocorrência de chuva, com um valor 0. Logo após isso, houve uma comparação com a coluna “RainTomorrow” onde aproximadamente 99,43% dos dados são provenientes da coluna “RainToday”, sendo assim confiáveis, que através da biblioteca sklearn forneceu que há um r2 de aproximadamente 0.399, uma acurácia de aproximadamente 82% e uma precisão de aproximadamente 81%. A partir da coluna obtida junto ao método utilizado e aos resultados de r2, acurácia e precisão, é possível determinar que, pela última linha da coluna “RainTomorrow_predict” no arquivo atualizado de teste, não terá ocorrência de chuva no dia seguinte à última medição, o dia 26 de Junho do ano de 2017, em Sydney, Austrália.</p>

### **CONCLUSÕES**

<p>Para o desenvolvimento do sistema a ser utilizado, levando em consideração o melhor método através dos conhecimentos adquiridos pela disciplina de Álgebra Linear 2, as substituições de valores não numéricos nas tabelas dos arquivos fornecidos, as bibliotecas e a melhor linguagem de programação, foi necessário um aprofundamento no entendimento de métodos de predição, sua relação com o conteúdo estudado em Álgebra Linear 2, assim como poder entender as maneiras de como o conteúdo passado em sala de aula é aplicado para além da universidade. Foi importante também uma dedicação para saber um pouco mais de como o método de mínimos quadrados é utilizado através de computadores e sistemas em geral e principalmente pelas bibliotecas comumente empregadas nos códigos que lidam com dados,assim como os comandos e os melhores módulos para a obtenção de resultados mais satisfatórios. Outro ponto crucial foi ter esta primeira visão, simplificada, do aprendizado de máquina e da manipulação de dados em geral, assuntos em alta, com uma grande demanda de profissionais na área e importantes para as gerações atual e futuras.</p>

### **REFERÊNCIAS**

Disponível em: https://math.stackexchange.com/questions/1338258/rain-forecast-model-and-least-squares Acesso em: 06 nov. 2022.<br>
Disponível em: https://medium.com/@dkatzman_3920/how-to-deal-with-missing-or-na-values-in-the-dataset-7d8f1693450d Acesso em: 06 nov. 2022.<br>
Disponível em: https://pandas.pydata.org/docs/user_guide/index.html#user-guide Acesso em: 06 nov. 2022.<br>
Disponível em: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html Acesso em: 06 nov. 2022.<br>
Disponível em: https://www.geeksforgeeks.org/python-linear-regression-using-sklearn/ Acesso em: 06 nov. 2022.<br>
Disponível em: https://math.stackexchange.com/questions/901484/unique-least-square-solutions Acesso em: 06 nov. 2022.<br>
