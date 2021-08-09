# Usefull functions

def convierte_a_minusculas(df):
    """
    Convierte a minúsculas todas las celdas de tipo str en un dataframe
    :param df: dataframe
    :return: dataframe en minúsculas
    ==========
    Ejemplo:
        >> dataframe = convierte_a_minusculas(dataframe)
    """

    df = df.applymap(lambda s: s.lower() if type(s) == str else s)

    return df

