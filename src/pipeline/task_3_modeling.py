import luigi

from src.utils.utils import save_df, load_df
from src.pipeline.task_2_feature import featureengineering
from src.utils.funcs_task_3_modeling import *


class modeling(luigi.Task):
    # Parametros
    fecha = luigi.Parameter()

    def requires(self):
        return featureengineering(self.fecha)

    def run(self):
        df = load_df('tmp/df_2_feature_' + str(self.fecha) + ".pkl")
        # df = undersampling(df)
        model = modeling(df)

        Pkl_Filename = "tmp/selected_model.pkl"

        with open(Pkl_Filename, 'wb') as file:
            pickle.dump(model, file)


        #save_df(y_pred, 'tmp/modelado_y_pred' + str(self.fecha) + ".pkl")
        #save_df(y_test, 'tmp/modelado_y_test' + str(self.fecha) + ".pkl")
        #save_df(y_pred, 'tmp/selected_model.pkl')

    def output(self):
        return luigi.local_target.LocalTarget('tmp/selected_model.pkl')
