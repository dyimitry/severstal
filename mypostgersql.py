import os
from dotenv import load_dotenv
import psycopg2
load_dotenv()


class Postgres:
    def __init__(self, name_table):
        self.name_table = name_table
        self.con = psycopg2.connect(dbname=os.getenv('DB_NAME'), user=os.getenv('POSTGRES_USER'),
                                    password=os.getenv('POSTGRES_PASSWORD'))
        self.cur = self.con.cursor()

    def close_database(self):
        self.con.commit()
        self.con.close()

    def create_table(self):
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {self.name_table}(
                            id SERIAL PRIMARY KEY,
                            ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            size TEXT);
                        """)

    def insert(self, size):
        self.cur.execute(f"""INSERT INTO {self.name_table}(size) VALUES ({size});""")

    def select(self):
        self.cur.execute(f'''
        SELECT *
        FROM {self.name_table};
        ''')

        for result in self.cur:
            print(result)
        # self.con.close()

# q = Postgres('pictures')
# q.create_table()
# q.insert(5, '1')
# c  =q.select()
# q.close_database()