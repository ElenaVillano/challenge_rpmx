import pandas as pd

from src.pipeline.taks_1_preprocesamiento import preprocesamiento_limpieza
from src.pipeline.taks_2_feature import feature_engineering

df = pd.read_csv('data/ds_challenge_apr2021.csv')
df = preprocesamiento_limpieza(df)
df_nuevo = feature_engineering(df)

