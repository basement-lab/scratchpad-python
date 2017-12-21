"""
Module: provides a Class that proviedes a Connection to the Basement-Lab PostgreSQL database,
and manages the Connection & Cursors to that database and provides convenient methods for
making queries against that database.
"""

import os
import psycopg2


DB_NAME = os.environ['POSTGRES_DB']
USER = os.environ['POSTGRES_USER']
PASSWORD = os.environ['POSTGRES_PASSWORD']
HOST = os.environ['POSTGRES_HOST']
PORT = os.environ['POSTGRES_PORT']


class Postgres:
    """
    Class: provides a connection and a NEW cursor with each query made
    """

    def __init__(self):
        self._connection = self._connect()

    def _connect(self):
        """
        Method (private): returns a connection to the PostgreSQL database
        """
        return psycopg2.connect(dbname=DB_NAME,
                                user=USER,
                                password=PASSWORD,
                                host=HOST,
                                port=PORT)

    def _cursor(self):
        """
        Method (private): returns a Cursor from the connected PostgreSQL database
        """
        return self._connection.cursor()

    def close(self):
        """
        Method: closes the Connection to the PostgreSQL Database
        """
        self._connection.close()

    def query(self, statement, values=False):
        """
        Method: creates a Cursor, executes the SQL Query, closing the Cursor,
        and returning ALL of the results from the query
        """
        cur = self._cursor()

        if values is False:
            cur.execute(statement, values)
        else:
            cur.execute(statement)

        res = cur.fetchall()
        cur.close()
        return res

