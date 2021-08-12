import luigi
import yaml
from luigi.contrib.postgres import CopyToTable
from src.utils.utils import save_df, load_df
from src.pipeline.task_3_modeling import modeling
from src.pipeline.task_2_feature import featureengineering
from src.utils.funcs_task_4_prediccion import *
from src.utils.funcs_task_2_feature import *

class prediction(luigi.Task):
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
    table = ''

    def requires(self):
        yield featureengineering(self.fecha)

        yield modeling(self.fecha)