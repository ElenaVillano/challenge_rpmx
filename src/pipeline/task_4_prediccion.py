import luigi

from src.pipeline.task_3_modeling import modeling
from src.pipeline.task_2_feature import featureengineering
from src.utils.funcs_task_4_prediccion import *
from src.utils.funcs_task_2_feature import *

class prediction(luigi.Task):
    # Parametros
    fecha = luigi.Parameter()

    def requires(self):
        yield featureengineering(self.fecha)

        yield modeling(self.fecha)

    def run(self):
        df = load_df('tmp/df_2_feature_' + str(self.fecha) + ".pkl")

        modelo = load_df('model/selected_model.pkl')

        X_test = df.drop(columns=['fraude'], axis=1).values
        y_test = df['fraude']

        y_pred, y_proba, score = predicciones(modelo, X_test, y_test)

        metricas_all = metricas(y_pred, y_test)

        save_df(X_test, 'tmp/X_test_' + str(self.fecha) + ".pkl")
        save_df(y_test, 'tmp/y_test_' + str(self.fecha) + ".pkl")
        save_df(y_proba, 'tmp/y_proba_' + str(self.fecha) + ".pkl")
        save_df(y_pred, 'tmp/y_pred_' + str(self.fecha) + ".pkl")
        save_df(metricas_all, 'tmp/metricas_all_' + str(self.fecha) + ".pkl")

    def output(self):
        return luigi.local_target.LocalTarget('tmp/y_test_' + str(self.fecha) + ".pkl")







