import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd
import numpy as np
import psycopg2 as pg
import yaml

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

df = pd.read_sql('select * from predicciones;', connection)
print(df)
# df['date'] = pd.to_datetime(df['date'])

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Distribucion y_true"),
    dcc.Graph(id='my-graph', figure=px.histogram(data_frame=df, x='y_test'))])

if __name__ == '__main__':
    app.run_server()