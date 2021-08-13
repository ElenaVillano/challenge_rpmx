PYTHONPATH="." luigi --module src.pipeline.task_2_feature  featureengineering --fecha '2021-03-16'

PYTHONPATH="." luigi --module src.pipeline.task_3_modeling  modeling --fecha '2021-03-16'

PYTHONPATH="." luigi --module src.pipeline.task_4_prediccion  prediction --fecha '2021-01-30'

PYTHONPATH="." luigi --module src.pipeline.task_5_api  almacenamientoapi --fecha '2020-01-30'