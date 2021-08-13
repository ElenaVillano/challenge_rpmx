import yaml
from luigi.contrib.postgres import CopyToTable
import psycopg2 as pg
from src.pipeline.task_1_preprocesamiento import *
from src.utils.utils import load_df

class dbcleanrds(CopyToTable):
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
    table = 'cleandata'

    columns = [("order_txn", "INTEGER"),
               ("id_user", "INTEGER"),
               ("genero", "VARCHAR"),
               ("monto", "FLOAT"),
               ("fecha", "DATE"),
               ("hora", "INTEGER"),
               ("establecimiento", "VARCHAR"),
               ("tipo_tc", "VARCHAR"),
               ("dcto", "FLOAT"),
               ("cashback", "FLOAT"),
               ("fraude", "VARCHAR")
               ]

    def requires(self):
        return preprocesamiento(self.fecha)

    def rows(self):
        df = load_df('tmp/df_1_limpio_' + str(self.fecha) + ".pkl")
        records = df.to_records(index=False)
        results = list(records)

        for element in results:
            yield element

