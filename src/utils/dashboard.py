import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import joblib
import psycopg2 as pg
import yaml

def load_df(path):
    data = joblib.load(path)
    return data

with open('../../conf/local/credentials.yaml', 'r') as f:
    config = yaml.safe_load(f)

credentials = config['db']
user = credentials['user']
password = credentials['password']
database = credentials['dbname']
host = credentials['host']
port = credentials['port']

connection = pg.connect(database=database,
                        user=user,
                        password=password,
                        host=host,
                        port=port)

df_nueva = pd.read_sql('select * from cleandata;', connection)
df_entrenamiento = pd.read_sql('select * from datosentrenamiento;', connection)

df_nueva['base'] = 'base_nueva'
df_entrenamiento['base'] = 'base_entrenamiento'

df_entrenamiento = df_entrenamiento.sample(frac=0.3)

df = pd.concat([df_entrenamiento,df_nueva], axis=0)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Div([
    html.H2("Conteos de fraude"),
    dcc.Graph(id='my-graph',
              figure=px.histogram(
                  data_frame=df, x='fraude',
                  color='base'
              )),
        ]),
    html.Div([
        html.H2("Cashback (x) vs monto (y)"),
        dcc.Graph(id='my-graph2',
                  figure=px.scatter(
                      data_frame=df, x='cashback', y='monto',
                      color='base'
                  )),
    ]),
    html.Div([
        html.H2("Conteos de establecimiento"),
        dcc.Graph(id='my-graph3',
                  figure=px.histogram(
                      data_frame=df, x='establecimiento',
                      color='base'
                  )),
    ]),
])

if __name__ == '__main__':
    app.run_server()