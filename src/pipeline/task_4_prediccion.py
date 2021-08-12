import luigi

from src.utils.utils import save_df, load_df
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

    def rows(self):
        df = load_df('tmp/df_2_feature_' + str(self.fecha) + ".pkl")
        df = feature_engineering(df)

        modelo = load_df('tmp/selected_model.pkl')

        X_test = df.drop(columns=['fraude'], axis=1).values
        y_test = df['fraude']

        y_pred, score = predicciones(modelo, X_test, y_test)

        precision, recall, accuracy = metricas(y_pred, y_test)

        print('¡hola', precision, recall, accuracy)



