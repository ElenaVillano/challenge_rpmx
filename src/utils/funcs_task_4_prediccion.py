import pandas as pd
from sklearn.metrics import precision_score, accuracy_score, recall_score


def predicciones(modelo, X_test, y_test):

    y_pred = modelo.predict(X_test)

    score = modelo.score(X_test, y_test)

    print('Score:', score)

    return y_pred, score


def metricas(y_pred, y_test):
    data_precision_score = precision_score(y_test, y_pred, average='micro')

    data_accuracy_score = accuracy_score(y_test, y_pred)

    data_recall_score = recall_score(y_test, y_pred)

    metricas_all = pd.DataFrame([(data_precision_score,
                              data_recall_score,
                              data_accuracy_score)],
                 columns=['precision', 'recall', 'accuracy'])

    print('metricas:', metricas_all)

    return metricas_all