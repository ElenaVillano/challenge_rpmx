import yaml
from luigi.contrib.postgres import CopyToTable
import psycopg2 as pg
from src.pipeline.task_4_prediccion import *


class almacenamientoapi(CopyToTable):
    # Parametros
    fecha = luigi.Parameter()

    with open('conf/local/credentials.yaml', 'r') as f:
        config = yaml.safe_load(f)

    credentials = config['db']
    user = credentials['user']
    password = credentials['password']
    database = credentials['dbname']
    host = credentials['host']
    port = credentials['port']
    table = 'predicciones'

    columns = [("y_test", "INTEGER"),
               ("y_pred", "INTEGER"),
               ("id_user", "INTEGER")]

    def requires(self):
        return prediction(self.fecha)

    def rows(self):
        y_test = load_df('tmp/y_test_' + str(self.fecha) + ".pkl")
        y_pred = load_df('tmp/y_pred_' + str(self.fecha) + ".pkl")
        df = load_df('tmp/df_1_limpio_' + str(self.fecha) + ".pkl")

        y_predicciones = pd.DataFrame(y_test)
        y_predicciones.columns = ['y_test']
        y_predicciones['y_pred'] = pd.DataFrame(y_pred)
        y_predicciones['id_user'] = df['id_user']

        records = y_predicciones.to_records(index=False)
        results = list(records)

        for element in results:
            yield element

