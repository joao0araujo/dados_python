import pandas as pd

import plotly.express as px

# Grafico de barra que analiza se filhos com  Mae e Pai que completaram o Ensino superior obtem maiores notas em redação


dadosE = pd.read_csv("https://raw.githubusercontent.com/joao0araujo/dados_python/main/enemBA.csv")

mediasup = dadosE[((dadosE['Q001']=='F') | (dadosE['Q001']=='G')) & ((dadosE['Q002']=='F') | (dadosE['Q002']=='G'))] [[
    'NU_NOTA_REDACAO']].mean()

mediasup = mediasup.reset_index()

#print(mediasup)

mediamed = dadosE[((dadosE['Q001'] != 'F') & (dadosE['Q001'] != 'G')) & ((dadosE['Q002'] != 'F') & (dadosE['Q002'] != 'G')) ] [[
    'NU_NOTA_REDACAO']].mean()

mediamed = mediamed.reset_index()


dados = dadosE[['Q001', 'Q002', 'NU_NOTA_REDACAO']].groupby(['Q001', 'Q002']).mean().reset_index()



print(dados)

#print(mediamed)


import plotly.graph_objects as go

from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2, subplot_titles=('Pais com superior', 'Pais sem superior'), shared_yaxes=True)

#primeira tabela

mediasup.columns = ['Media', 'Valor']

ola = {'NU_NOTA_REDACAO': 'Media'}

mediasup['Media'] = mediasup['Media'].map(ola)



fig.add_trace(go.Bar(x=mediasup['Media'], y=mediasup['Valor']), row=1, col= 1)



#segunta tabela

mediamed.columns = ['Media', 'Valor']

oi = {'NU_NOTA_REDACAO': 'Media'}

mediamed['Media'] = mediamed['Media'].map(oi)

medias = [mediasup.Valor , mediamed.Valor]

sup = ['Superior', 'Sem graduação']

df_resumo = pd.DataFrame({'Graduado': mediasup.Valor, 'Não graduado': mediamed.Valor})

#fig = px.scatter(dados, x='Q001', y='Q002', size='NU_NOTA_REDACAO', color='NU_NOTA_REDACAO')

#print(df_resumo)


fig.add_trace(go.Bar(x=mediamed['Media'], y=mediamed['Valor']), row=1, col= 2)

fig.update_layout(height=400, width=600, title_text="Media da redação dos participantes")

fig.show()


