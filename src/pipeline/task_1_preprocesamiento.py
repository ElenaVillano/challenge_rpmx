import luigi
import pandas as pd

from src.pipeline.task_1_preprocesamiento import preprocesamiento_limpieza
from src.utils.utils import save_df


class preprocesamiento(luigi.Task):

    def run(self):
        df = pd.read_csv('data/ds_challenge_apr2021.csv')
        df = preprocesamiento_limpieza(df)

        save_df(df, 'tmp/df_1_limpio' + str(self.fecha) + ".pkl")

    def output(self):
        return luigi.local_target.LocalTarget('tmp/df_1_limpio' + str(self.fecha) + ".pkl")