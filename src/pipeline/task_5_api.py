import yaml
from luigi.contrib.postgres import CopyToTable
import psycopg2
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

    columns = [("col_1", "VARCHAR"),
               ("col_2", "VARCHAR")]

    def requires(self):
        return prediction(self.fecha)

    def rows(self):

        z = str(2+ 3)
        #print("########### ", z)
        r = [("test 1", z), ("test 2","45")]
        for element in r:
            yield element

    #def rows(self):
        #y_test = load_df('tmp/y_test_' + str(self.fecha) + ".pkl")
        #y_pred = load_df('tmp/y_pred_' + str(self.fecha) + ".pkl")

        #y_predicciones = pd.DataFrame(y_test)
        #y_predicciones.columns = ['y_test']
        #y_predicciones['y_pred'] = pd.DataFrame(y_pred)

        #records = y_predicciones.to_records(index=False)
        #results = list(records)

       # results = [('hola',
       #            'funciona')]

       # for element in results:
        #    yield element

