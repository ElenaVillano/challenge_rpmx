from sklearn.metrics import precision_score, accuracy_score, recall_score


def predicciones(modelo, X_test, y_test):

    y_pred = modelo.predict(X_test)

    score = modelo.score(X_test, y_test)

    print('Score:', score)

    return y_pred


def metricas(y_pred, y_test):
    data_precision_score = precision_score(y_test, y_pred)

    data_accuracy_score = accuracy_score(y_test, y_pred)

    data_recall_score = recall_score(y_test, y_pred)

    print('precision score:', data_precision_score)
    print('recall score:', data_recall_score)
    print('accuracy score:', data_accuracy_score)

    return data_precision_score, data_recall_score, data_accuracy_score