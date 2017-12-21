CREATE SEQUENCE linear_regression_id_seq;

CREATE TABLE linear_regression (id INTEGER DEFAULT NEXTVAL('linear_regression_id_seq'), x DOUBLE PRECISION, y DOUBLE PRECISION);
