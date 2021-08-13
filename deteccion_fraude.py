
from src.pipeline.task_2_feature import feature_engineering
from src.pipeline.task_3_modeling import *

df_nuevo = feature_engineering(df)

df_undersampled = undersampling()

print(df_undersampled.columns)

y_pred, y_test = modeling(df_undersampled)

metricas(y_pred, y_test)