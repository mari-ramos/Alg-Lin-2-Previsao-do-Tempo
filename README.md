# Alg-Lin-2-Previsao-do-Tempo
Algoritmo desenvolvido para a previsão de chuvas na cidade de Sydney, Austrália. Trabalho proposto nas aulas de Álgebra Linear, os materiais ofertados foram duas planilhas, uma de teste e outra para ser utilizada no código,  contendo os dados coletados referentes ]á umidade, velocidade e direção do vento, se choveu no dia ou não, etc.

INTRODUÇÃO

Este relatório tem como objetivo relatar o desenvolvimento do sistema e a solução encontrada para resolver o problema apresentado, sendo este a chance de ocorrência de chuva no dia seguinte à última amostra, o dia 26 de Junho do ano de 2017, em Sydney, Austrália. Foram fornecidas duas bases de dados, uma de treinamento e outra de teste, com diversos tipos de dados entre os anos de 2008 e 2017 que influenciam na ocorrência de chuva.

DESENVOLVIMENTO DO SISTEMA

  A partir das bases de dados apresentadas, uma de teste e outra de treinamento, junto ao método dos mínimos quadrados, foi possível tratar o problema abordado. Levando como base os conhecimentos adquiridos na disciplina de Álgebra Linear 2, mais especificamente do método dos mínimos quadrados, através da equação normal, θ = (X , a qual tem


como definição encontrar parâmetros de hipótese, através de dados de entrada e dados de saída. Baseado nisso, o próximo passo foi definir quais colunas seriam relevantes para o método, a atribuição de valores para elementos que não fossem numéricos, como “NA” (Not Applicable ), “Yes”, “No” e os dezesseis tipos de direção do vento e a definição de quais colunas seriam utilizadas como dados de entrada e dados de saída.
    
    Através da análise das colunas, foi possível concluir que as colunas de “Data” e “Localização” não seriam necessárias na implementação da equação normal, uma vez que se seus valores fossem levados em consideração na equação, não teriam uma influência significativa no resultado final, em sua acurácia e nem em sua precisão, o fato do analisador saber que as medições foram feitas em dias sucessivos e em um mesmo local já é o suficiente para achar a solução. Para os elementos não numéricos, o valor atribuído para os dados classificados como “NA” foi o número 0, para “Yes”, foi utilizado o número 1, para o “No”, foi o número 0, e para as dezesseis direções do vento, foi utilizado os ângulos formados por cada uma delas, de 0 a 337.5, com um intervalo de 22.5. Após a retirada das colunas de “Data” e “Localização” e da atribuição de valores para dados não numéricos, as colunas “MinTemp”, “MaxTemp”, “Rainfall”, “Evaporation”, “Sunshine”, “WinndGustDir”, “WindGustSpeed”, “WindDir9am”, “WindDir3pm”, “WindSpeed9am”, “WindSpeed3pm”, “Humidity9am”, “Humidity3pm”, “Pressure9am”, “Pressure3pm”, “Cloud9am”, “Cloud3pm”, “Temp9am”, “Temp3pm” e “RainToday” foram denominadas como dados de entrada nas duas bases de dados, uma vez que são os dados obtidos através das medições. Para uma coluna ser classificada como um dado de saída, ela tem que possuir as informações que o analisador quer saber, são as respostas para o problema, a partir disso fica evidente que os dados correspondentes a se choveu no dia seguinte às medições ou não fazem parte dos dados de saída.
    
