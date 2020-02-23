import mysql.connector
from bikeApi.config import db_config
from mysql.connector.cursor import MySQLCursorDict
from typing import List, Dict, Iterator, Union


class StoreException(Exception):
    def __init__(self, message, *errors):
        Exception.__init__(self, message)
        self.errors = errors


class Store():
    def __init__(self, dbconfig=None):
        try:
            config = dbconfig or db_config
            self.conn = mysql.connector.connect(**config)
        except Exception as e:
            raise StoreException(*e.args)
        self._complete = False

    def __enter__(self):
        return self

    def __exit__(self, type_, value, traceback):
        self.close()

    def complete(self) -> None:
        self._complete = True

    def random(self) -> Union[Dict, None]:
        c = self.conn.cursor(dictionary=True)
        c.execute('SELECT * FROM {} ORDER BY RAND() LIMIT 1;'.format(self.table))
        return c.fetchone()

    def find_by_id(self, ID: int) -> Union[Dict, None]:
        c = self.conn.cursor(dictionary=True)
        statement = 'SELECT * FROM {} where ID = %s ;'.format(self.table)
        c.execute(statement, (ID,))
        return c.fetchone()

    def where(self, condition) -> Union[Dict, None]:
        c = self.conn.cursor(dictionary=True)
        statement = 'SELECT * FROM {table} where {condition}'.format(table=self.table, condition=' AND '.join(
            ['{} = %s'.format(x) for x in condition.keys()]))
        c.execute(statement, tuple(condition.values()))
        return c.fetchone()

    def iter_row(cursor: MySQLCursorDict, size: int = 1000) -> Iterator[Dict]:
        while True:
            rows: List[Dict] = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    def close(self):
        if self.conn:
            try:
                if self._complete:
                    self.conn.commit()
                else:
                    self.conn.rollback()
            except Exception as e:
                raise StoreException(*e.args)
            finally:
                try:
                    self.conn.close()
                except Exception as e:
                    raise StoreException(*e.args)
