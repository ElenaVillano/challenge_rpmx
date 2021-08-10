import pandas as pd
from src.utils.utils import convierte_a_minusculas
from src.utils.utils import save_df


def limpieza(data):
    """
    Preprocesamiento y limpieza de datos
    :param data: dataframe
    :return: dataframe en minúsculas
    ==========
    Ejemplo:
        >> dataframe = preprocesamiento_limpieza(dataframe)
    """

    data = convierte_a_minusculas(data)
    data = data.rename(columns={'ID_USER': 'id_user'})
    data['fecha'] = pd.to_datetime(data['fecha'])
    data['fraude'] = data['fraude'].apply(lambda x: 1 if x == True else 0)
    data['is_prime'] = data['is_prime'].apply(lambda x: 'si_prime' if x == True else 'no_prime')
    data['tipo_tc'] = data['tipo_tc'].replace(['física'], 'fisica')
    data['genero'] = data['genero'].replace(['--'], 'no_def')
    data['establecimiento'] = data['establecimiento'].fillna('NA_establecimiento')
    data['ciudad'] = data['ciudad'].fillna('NA_ciudad')

    save_df(data, 'tmp/df_limpio.pkl')

    return data
