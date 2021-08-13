set timezone = 'America/Mexico_City';

DROP TABLE IF EXISTS predicciones;
DROP TABLE IF EXISTS table_updates;
DROP TABLE IF EXISTS cleandata;

CREATE SCHEMA IF NOT EXISTS api:

CREATE TABLE predicciones(
	id_user varchar null,
	y_test varchar null,
	y_pred varchar null);