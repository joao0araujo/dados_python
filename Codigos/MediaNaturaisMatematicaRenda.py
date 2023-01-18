import pandas as pd

import plotly.express as px

#Grafico de barra que analiza as medias de naturais e matematica em cada grupo de renda familiar

dadosE = pd.read_csv("https://raw.githubusercontent.com/joao0araujo/dados_python/main/enemBA.csv")

renda = dadosE[['Q006', 'NU_NOTA_CN', 'NU_NOTA_MT']].groupby('Q006').mean()

#print(renda)

renda = renda.reset_index()

renda.columns = ['Renda', 'NotaCN', 'NotaMT']

cola = {'A': 'Nenhuma renda', 'B': 'Até 1 salario', 'C': 'Entre 1 e 1,5 salario', 'D': 'Entre 1,5 e 2 salarios', 
'E': 'Entre 2 e 2,5 salarios', 'F': 'Entre 2,5 e 3 salarios', 'G': 'Entre 3 e 4 salarios', 'H': 'Entre 4 e 5 salarios',
'I': 'Entre 5 e 6 salarios', 'J': 'Entre 6 e 7 salarios', 'K': 'Entre 7 e 8 salarios', 'L': 'Entre 8 e 9 salarios',
'M': 'Entre 9 e 10 salarios', 'N': 'Entre 10 e 12 salarios', 'O': 'Entre 12 e 15 salarios', 'P': 'Entre 15 e 20 salarios',
'Q': 'Acima de 20 salarios'}

renda['Renda'] = renda['Renda'].map(cola)

fig = px.bar(renda, title='Media de notas por renda familiar', x='Renda', y=['NotaCN', 'NotaMT'], barmode='group')

fig.show()