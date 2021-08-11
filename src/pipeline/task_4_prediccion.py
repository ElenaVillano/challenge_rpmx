import luigi

from src.utils.utils import save_df, load_df
from src.pipeline.task_3_modeling import modeling
from src.utils.funcs_task_4_prediccion import *


class prediction(luigi.Task):
    # Parametros
    fecha = luigi.Parameter()

    def requires(self):
        yield fe