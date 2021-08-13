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

#with open('../../conf/local/credentials.yaml', 'r') as f:
#    config = yaml.safe_load(f)

#credentials = config['db']
#user = credentials['user']
#password = credentials['password']
#database = credentials['dbname']
#host = credentials['host']
#port = credentials['port']

#connection = pg.connect(database=database,
#                        user=user,
#                        password=password,
#                        host=host,
#                        port=port)

#df = pd.read_sql('select * from predicciones;', connection)
#print(df)
# df['date'] = pd.to_datetime(df['date'])

df=load_df('tmp/df_1_limpio_' + str(self.fecha) + ".pkl")

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Distribucion y_true"),
    dcc.Graph(id='my-graph', figure=px.scatter(data_frame=df, x='cashback',y='monto'))])

if __name__ == '__main__':
    app.run_server()