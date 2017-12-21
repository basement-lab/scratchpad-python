# from psycopg2 import *
# print(dir())
import psycopg2 as pc2

dbname = "lab"
user = "lab"
password = "basementlab"
host = "172.16.42.4"
port = "32770"

conn = pc2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

cur = conn.cursor()

cur.execute("SELECT * FROM linear_regression;")
x = cur.fetchall()

print(x)

cur.close()
conn.close()
