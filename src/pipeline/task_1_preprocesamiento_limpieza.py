import pandas as pd
import luigi


from src.utils.t_1_preprocesamiento_limpieza import limpieza
from src.utils.utils import save_df


class preprocesamiento_limpieza(luigi.Task):
    def run(self):
        # Carga de datos
        df = pd.read_csv("data/ds_challenge_apr2021.csv")

        # Limpieza de base
        df = limpieza(df)

        ## Saving File
        save_df(df, '../tmp/df_limpio.pkl')

    def output(self):
        return luigi.local_target.LocalTarget("tmp/df_limpio.pkl")
