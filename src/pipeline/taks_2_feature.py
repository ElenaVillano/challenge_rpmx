import pandas as pd
import numpy as np
# import time

from src.utils.utils import save_df, load_df
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer


def one_hot_scaler(data):
    load_df('tmp/df_1_limpio.pkl')
    standard_scaler = StandardScaler()

    transformers = [('one_hot',
                     OneHotEncoder(sparse=False,
                                   categories="auto"),
                     ['tipo_tc', 'is_prime', 'genero',
                      'establecimiento', 'ciudad']),
                    ('standar_scaler',
                     standard_scaler,
                     ['monto', 'dcto', 'cashback',
                      'linea_tc', 'interes_tc'
                      ])]

    col_trans = ColumnTransformer(transformers, remainder="drop",
                                  n_jobs=-1, verbose=True)

    df_regressors = col_trans.fit(data)
    df_transformed = df_regressors.transform(data)

    a = [sorted(data.tipo_tc.unique()),
         sorted(data.is_prime.unique()),
         sorted(data.genero.unique()),
         sorted(data.establecimiento.unique()),
         sorted(data.ciudad.unique())]

    colnames = sum(a, [])

    colnames.append('monto')
    colnames.append('dcto')
    colnames.append('cashback')
    colnames.append('linea_tc')
    colnames.append('interes_tc')

    final_df = pd.DataFrame(df_transformed, columns=colnames)

    final_df['fraude'] = data['fraude']
    final_df['fecha'] = data['fecha']
    final_df['hora'] = data['hora']

    return final_df


def horas_dias_ciclo(data):
    data['dia'] = pd.DatetimeIndex(data['fecha']).day

    dias = 30

    data['sin_dia'] = np.sin(2 * np.pi * data['dia'] / dias)
    data['cos_dia'] = np.cos(2 * np.pi * data['dia'] / dias)

    data = data.drop('fecha', 1)
    data = data.drop('dia', 1)

    horas = 24

    data['sin_hora'] = np.sin(2 * np.pi * data['hora'] / horas)
    data['cos_hora'] = np.cos(2 * np.pi * data['hora'] / horas)

    data = data.drop('hora', 1)

    return data


def feature_engineering(data):
    final_df = one_hot_scaler(data)
    final_df = horas_dias_ciclo(final_df)

    save_df(final_df, 'tmp/df_2_feature_engineering.pkl')

    return final_df
