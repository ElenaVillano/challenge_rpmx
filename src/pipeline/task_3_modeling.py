import luigi

from src.utils.utils import save_df, load_df
from src.pipeline.task_2_feature import featureengineering
from src.utils.funcs_task_3_modeling import modelado


class modeling(luigi.Task):
    # Parametros
    fecha = luigi.Parameter()

    def requires(self):
        return featureengineering(self.fecha)

    def run(self):
        df = load_df('tmp/df_2_feature_' + str(self.fecha) + ".pkl")

        model = modelado(df)

        save_df(model, 'model/selected_model.pkl')

    def output(self):
        return luigi.local_target.LocalTarget('model/selected_model.pkl')
