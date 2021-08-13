set timezone = 'America/Mexico_City';

DROP TABLE IF EXISTS predicciones;
DROP TABLE IF EXISTS table_updates;

CREATE SCHEMA IF NOT EXISTS api:

CREATE TABLE predicciones(
	id_user varchar null,
	y_test varchar null,
	y_pred varchar null);