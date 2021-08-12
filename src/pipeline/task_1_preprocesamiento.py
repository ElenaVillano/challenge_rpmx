import luigi
import pandas as pd

from src.utils.funcs_task_1_prepro import preprocesamiento_limpieza
from src.utils.utils import save_df


class preprocesamiento(luigi.Task):
    # Parametros
    fecha = luigi.Parameter()

    def run(self):
        df = pd.read_csv('data/historic_db_' + str(self.fecha) + '.csv')
        df = preprocesamiento_limpieza(df)

        save_df(df, 'tmp/df_1_limpio_' + str(self.fecha) + ".pkl")

    def output(self):
        return luigi.local_target.LocalTarget('tmp/df_1_limpio_' + str(self.fecha) + ".pkl")