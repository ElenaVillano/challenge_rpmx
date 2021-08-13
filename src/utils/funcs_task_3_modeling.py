import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def undersampling(data):
    df = data.drop(['no_prime', 'si_prime'], 1)

    df_no_fraude = df[df['fraude'] == 0]
    df_si_fraude = df[df['fraude'] == 1]

    muestra_no_fraude = df_no_fraude.sample(n=810, random_state=12)
    muestra_si_fraude = df_si_fraude

    df_undersampled = pd.concat([muestra_si_fraude, muestra_no_fraude], axis=0)

    print(df_undersampled['fraude'].value_counts())

    return df_undersampled


def modelado(data):
    df = data

    print(df.columns)

    X = df.drop(columns=['fraude'], axis=1).values
    y = df['fraude']

    print(X.shape, y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        stratify=y,
                                                        random_state=12)

    model = LogisticRegression()

    print(model)

    model.fit(X_train, y_train)

    return model






