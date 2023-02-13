import pandas as pd
import numpy as np
import funzioni as fn
#import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

tab = pd.read_csv('pollution_us_2011_2013.csv')
poll = tab[['State Code', 'Date Local', 'NO2 Mean']]

ard, arm = fn.stato(poll, 4)
utd, utm = fn.stato(poll, 49)
nmd, nmm = fn.stato(poll, 35)
cod, com = fn.stato(poll, 8)
wyd, wym = fn.stato(poll, 46)

arizona = np.full(len(ard), 'AZ')
utah = np.full(len(utd), 'UT')
new_mexico = np.full(len(nmd), 'NM')
colorado = np.full(len(cod), 'CO')
wyoming = np.full(len(wyd), 'WY')

data = np.concatenate((ard, utd, nmd, cod, wyd))
no2 = np.concatenate((arm, utm, nmm, com, wym))
stati = np.concatenate((arizona, utah, new_mexico, colorado, wyoming))

df = pd.DataFrame()
df['date'] = data
df['states'] = stati
df['no2'] = no2
df['date'] =pd.to_datetime(df['date']).dt.date.astype(str)
df = df.sort_values('date')

fig = px.choropleth(df,
                   locations='states',
                   locationmode='USA-states',
                   scope='usa',
                   color = 'no2',
                   color_continuous_scale="Viridis_r",
                   range_color = (0, 100),
                   animation_frame = 'date'
                   )
fig.update_layout(coloraxis_colorbar=dict(
    title= 'media no2, parts per billion',
    ticks="outside", 
    dtick=50))
fig.show()
