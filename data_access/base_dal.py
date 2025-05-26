from datetime import date, datetime
import sqlite3
import os

import shutil
source = "database/hotel_reservation_db.db"
db_file = "database/working_db.db"
os.environ["DB_FILE"] = db_file

shutil.copyfile(source, db_file) #Copy original DB first to always start fresh.

def date_to_db(d: date) -> str:
    return d.isoformat()

def db_to_date(s: str) -> date:
    return datetime.strptime(s.decode(), "%Y-%m-%d").date()

## Adapter: Wandelt `date`-Objekt in `TEXT` um
sqlite3.register_adapter(date, date_to_db)

## Konverter: Wandelt gespeicherte `TEXT`-Werte wieder in `date`
sqlite3.register_converter("DATE", db_to_date)



class BaseDAL:
    def __init__(self, connection_str: str = None):
        if connection_str:
            self.__connection_str = connection_str
        else:
            self.__connection_str = os.environ.get("DB_FILE")
            if self.__connection_str is None:
                raise Exception("DB_FILE environment variable or parameter connection_str has to be set.")
    
    def _connect(self):
        conn = sqlite3.connect(self.__connection_str, detect_types=sqlite3.PARSE_DECLTYPES)
        conn.row_factory = sqlite3.Row
        return conn

    def fetchone(self, sql: str, params: tuple = None):
        if params is None:
            # leeres tuple für sql parameter wenn params None ist
            params = ()
        with self._connect() as conn:
            try:
                cursor = conn.execute(sql, params)
                result = cursor.fetchone()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
        return result

    def fetchall(self, sql: str, params: tuple = None):
        if params is None:
            # leeres tuple für sql parameter wenn params None ist
            params = ()
        with self._connect() as conn:
            try:
                cursor = conn.execute(sql, params)
                results = cursor.fetchall()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
        return results

    def execute(self, sql: str, params: tuple = None):
        if params is None:
            # leeres tuple für sql parameter wenn params None ist
            params = ()
        with self._connect() as conn:
            try:
                cursor = conn.execute(sql, params)
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            else:
                conn.commit()
        return cursor.lastrowid, cursor.rowcount
    
    @property
    def conn(self):
        return self._connect()