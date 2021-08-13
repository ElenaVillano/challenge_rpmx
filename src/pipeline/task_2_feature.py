import luigi

from src.pipeline.task_1_preprocesamiento_rds import dbcleanrds
from src.utils.funcs_task_2_feature import *


class featureengineering(luigi.Task):
    # Parametros
    fecha = luigi.Parameter()

    def requires(self):
        return dbcleanrds(self.fecha)

    def run(self):

        df = load_df('tmp/df_1_limpio_' + str(self.fecha) + ".pkl")
        df = feature_engineering(df)

        save_df(df, 'tmp/df_2_feature_' + str(self.fecha) + ".pkl")

    def output(self):
        return luigi.local_target.LocalTarget('tmp/df_2_feature_' + str(self.fecha) + ".pkl")
