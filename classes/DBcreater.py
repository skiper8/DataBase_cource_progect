import psycopg2
from config import config


class DBcreater:
    params = config()
    def createDB(self):
        conn = psycopg2.connect(dbname='hh', **self.params)
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM pg_catalog.pg_database WHERE datname = 'hh'")
            result = cur.fetchone()

            if result[0] == 0:
                cur.execute("CREATE DATABASE hh;")
                conn.commit()
            else:
                print("БД с таким названием уже существует.")
        cur.close()
        conn.close()

    def create_table_hh_companys(self):
        """
        Создание таблицы с компаниями
        """
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT * FROM hh_companys;""")
                rows = cur.fetchall()
                if rows is not None:
                    cur.execute("""DROP TABLE hh_vacancies;
                                    DROP TABLE hh_companys;""")

                cur.execute("""CREATE TABLE IF NOT EXISTS hh_companys(
                                company_id int,
                                company_name varchar(50) NOT NULL,
								CONSTRAINT pk_hh_companys_company_id PRIMARY KEY (company_id)
								);""")
        conn.commit()

    def create_table_hh_vacancies(self):
        """
        Создание таблицы с вакансиями
        """
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("""CREATE TABLE IF NOT EXISTS hh_vacancies(
                                vacanci_id int UNIQUE,
                                title varchar(100),
                                url varchar(200),
                                description text,
                                salary int,
                                city varchar(50),
                                company_id int,
                                company_name varchar(100) NOT NULL,
                                CONSTRAINT fk_hh_vacancies_hh_companys FOREIGN KEY(company_id) REFERENCES hh_companys(company_id)
                                );""")
        conn.commit()

    def insert_table_hh_company(self, data):
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                for item in data:
                    cur.executemany("INSERT INTO hh_companys VALUES (%s, %s) "
                                    "ON CONFLICT (company_id) DO NOTHING",
                                    [(item['employer_id'], item['employer_name'])])
    def insert_table_hh_vacancies(self, data):
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                for item in data:
                    cur.executemany("INSERT INTO hh_vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                                    "ON CONFLICT(vacanci_id) DO NOTHING",
                                    [(item['vacanci_id'],
                                      item['name'],
                                      item['url'],
                                      item['description'],
                                      item['salary_to'],
                                      item['city'],
                                      item['employer_id'],
                                      item['employer_name'])])
