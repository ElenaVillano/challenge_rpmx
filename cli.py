from src.pipeline.taks_1_preprocesamiento import preprocesamiento_limpieza
from src.pipeline.taks_2_feature import feature_engineering
from src.pipeline.taks_3_modeling import *

import click


@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
def main(verbose):
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Hello World")