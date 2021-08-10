import pandas as pd

from src.pipeline.t_1_limpieza import limpieza
from src.utils.utils import save_df

df = pd.read_csv('data/ds_challenge_apr2021.csv')
df = limpieza(df)