import pandas as pd
import numpy as np


from src.utils.utils import save_df, load_df
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, accuracy_score, recall_score
from sklearn.linear_model import LogisticRegression


def undersampling():
    df = load_df('tmp/df_2_feature_engineering.pkl')
    df = df.drop(['no_prime', 'si_prime'], 1)

    df_no_fraude = df[df['fraude'] == 0]
    df_si_fraude = df[df['fraude'] == 1]

    muestra_no_fraude = df_no_fraude.sample(n=810, random_state=12)
    muestra_si_fraude = df_si_fraude

    df_undersampled = pd.concat([muestra_si_fraude, muestra_no_fraude], axis=0)

    print(df_undersampled['fraude'].value_counts())

    return df_undersampled


def modeling(data):
    X = data.drop(columns=['fraude'], axis=1).values
    y = data['fraude']

    print(X.shape, y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        stratify=y,
                                                        random_state=12)

    print(X.shape, X_train.shape, X_test.shape)

    model = LogisticRegression().fit(X_train, y_train)

    y_pred = model.predict(X_test)

    score = model.score(X_test, y_test)

    print('Score modelo:', score)

    return y_pred, y_test


def metricas(y_pred,y_test):

    data_precision_score = precision_score(y_test, y_pred)

    data_accuracy_score = accuracy_score(y_test, y_pred)

    data_recall_score = recall_score(y_test, y_pred)

    print('precision score:', data_precision_score)
    print('recall score:', data_recall_score)
    print('accuracy score:', data_accuracy_score)










