import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, accuracy_score, recall_score
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


def train_test(data):
    df = data

    print(df.columns)

    X = df.drop(columns=['fraude'], axis=1).values
    y = df['fraude']

    print(X.shape, y.shape)

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        stratify=y,
                                                        random_state=12)

    #print(X.shape, X_train.shape, X_test.shape)

    model = LogisticRegression()

    model.fit(X_train, y_train)

    return model

    #with open()


    #filename = 'tmp/selected_model.sav'
    #pickle.dump(model, open(filename, 'wb'))
    #selected_model = model_selection(models, X_test, y_test, self.fecha)

    #y_pred = model.predict(X_test)

    # score = model.score(X_test, y_test)

    # print('Score modelo:', score)

    #return y_pred, y_test, model
    #return y_pred


def metricas(y_pred, y_test):
    data_precision_score = precision_score(y_test, y_pred)

    data_accuracy_score = accuracy_score(y_test, y_pred)

    data_recall_score = recall_score(y_test, y_pred)

    print('precision score:', data_precision_score)
    print('recall score:', data_recall_score)
    print('accuracy score:', data_accuracy_score)
