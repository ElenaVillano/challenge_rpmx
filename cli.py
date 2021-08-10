from src.pipeline.taks_1_preprocesamiento import preprocesamiento_limpieza
from src.pipeline.taks_2_feature import feature_engineering
from src.pipeline.taks_3_modeling import *

import click


@click.command()
@click.option(
    '--modelado',type=click.Choice(["yes", "no"]), help="Restart and retrain model."
)
@click.option('--datos', default=False, is_flag=True, help="Pon los datos")


def main(modelado, datos):

    if str(modelado)=="yes":
        df = pd.read_csv('data/ds_challenge_apr2021.csv')
        df = preprocesamiento_limpieza(df)
        feature_engineering(df)

        df_undersampled = undersampling()
        print(df_undersampled.columns)
        y_pred, y_test = modeling(df_undersampled)

        metricas(y_pred, y_test)

    else:
        pass