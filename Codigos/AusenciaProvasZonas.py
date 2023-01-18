import pandas as pd

import plotly.express as px

#Grafico de pizza que analiza a quantidade de ausentes nas zonas rural e urbana, agrupados por dias de prova

dadosE = pd.read_csv("https://raw.githubusercontent.com/joao0araujo/dados_python/main/enemBA.csv")

rur = dadosE[dadosE['TP_LOCALIZACAO_ESC']==2][['TP_LOCALIZACAO_ESC','TP_PRESENCA_CN']].groupby('TP_PRESENCA_CN').count()

rural = dadosE[dadosE['TP_LOCALIZACAO_ESC']==2][['TP_LOCALIZACAO_ESC','TP_PRESENCA_CH']].groupby('TP_PRESENCA_CH').count()

rur = rur.reset_index()

rural = rural.reset_index()


urb = dadosE[dadosE['TP_LOCALIZACAO_ESC']==1][['TP_LOCALIZACAO_ESC','TP_PRESENCA_CN']].groupby('TP_PRESENCA_CN').count()

urbano = dadosE[dadosE['TP_LOCALIZACAO_ESC']==1][['TP_LOCALIZACAO_ESC','TP_PRESENCA_CH']].groupby('TP_PRESENCA_CH').count()

urb = urb.reset_index()

urbano = urbano.reset_index()

print(urb)
print(urbano)


rur.columns = ['Presença', 'Quantidade']
rural.columns = ['Presença', 'Quantidade']
urb.columns = ['Presença', 'Quantidade']
urbano.columns = ['Presença', 'Quantidade']

import plotly.graph_objects as go

from plotly.subplots import make_subplots


fig = make_subplots(rows=2, cols=2, subplot_titles=['Rural: Naturais e Matemática', 'Rural: Humanas e Linguagens', 'Urbano: Naturais e Matemática', 'Urbano: Humanas e Linguagens'],
specs=[[{"type": "pie"}, {"type": "pie"}],
           [{"type": "pie"}, {"type": "pie"}]])

fig.add_trace(go.Pie(values=rur['Quantidade'], labels=['Faltou', 'Presente', 'Eliminado']),
 row=1, col=1)

fig.add_trace(go.Pie(values=rural['Quantidade'],labels=['Faltou', 'Presente', 'Eliminado']), row=1, col=2)

fig.add_trace(go.Pie(values=urb['Quantidade'],labels=['Faltou', 'Presente', 'Eliminado']), row=2, col=1)

fig.add_trace(go.Pie( values=urbano['Quantidade'],labels=['Faltou', 'Presente', 'Eliminado']), row=2, col=2)

fig.update_layout(title_text="Porcentagem de ausentes nas provas por zonas",)

fig.show()