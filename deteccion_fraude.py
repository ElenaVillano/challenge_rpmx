import pandas as pd

from src.pipeline.taks_1_preprocesamiento import preprocesamiento_limpieza


df = pd.read_csv('data/ds_challenge_apr2021.csv')
df = preprocesamiento_limpieza(df)