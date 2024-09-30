import sqlite3
from sqlite3 import Connection, Cursor
from sqlite3 import Error as DBError


class Database:
    def __init__(self):
        self.dbname: str = "gamedata.db"
        self.conn: Connection = self.connect_to_db()
        
    def connect_to_db(self) -> Connection:
        try:
            while True:
                conn = sqlite3.connect(self.dbname)
                print("verify testing")
                if self.verify_db(conn):
                    return conn
                else:
                    self.create_db(conn)
        except DBError:
            return None
    def disconnect_to_db(self):
        if self.conn:
            self.conn.close()
    
    @staticmethod
    def verify_db(conn: Connection) -> bool:
        tables = {"save", "character", "translation"}
        try:
            cursor: Cursor = conn.cursor()
            for table in tables:
                cursor.execute(
                    "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,)
                )
                result = cursor.fetchone()
                if not result:
                    return False
            return True
        except DBError:
            return False
    
    @staticmethod
    def create_db(conn: Connection):
        cursor: Cursor = conn.cursor()

        save_table_query = '''
        CREATE TABLE IF NOT EXISTS save (
            id INTEGER PRIMARY KEY,
            lang text not null  
        );
        '''
        character_table_query = '''
        CREATE TABLE IF NOT EXISTS character (
            id INTEGER PRIMARY KEY,
            name text not null,
            stats text not null
        );
        '''
        translation_table_query = '''
        CREATE TABLE IF NOT EXISTS translation (
            id INTEGER PRIMARY KEY,
            lang text not null,
            message text not null  
        );
        '''

        cursor.execute(save_table_query)
        cursor.execute(character_table_query)
        cursor.execute(translation_table_query)
        
        conn.commit()


# db = Database()