import psycopg2


class DBcreater:

    def createDB(self):
        conn = psycopg2.connect(host="localhost", user="postgres", password="456852")
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM pg_catalog.pg_database WHERE datname = 'hh'")
            result = cur.fetchone()

            if result[0] == 0:
                cur.execute("CREATE DATABASE hh;")
                conn.commit()
            else:
                print("БД с таким названием уже суествует.")

        cur.close()
        conn.close()

    def create_table_hh_companys(self):
        with psycopg2.connect(host="localhost", database="hh", user="postgres", password="456852") as conn:
            with conn.cursor() as cur:
                cur.execute("""CREATE TABLE IF NOT EXISTS hh_companys(
                                company_id int,
                                company_name varchar(50) NOT NULL,
								CONSTRAINT pk_hh_companys_company_id PRIMARY KEY (company_id)
								);""")
        conn.commit()

    def create_table_hh_vacancies(self):
        with psycopg2.connect(host="localhost", database="hh", user="postgres", password="456852") as conn:
            with conn.cursor() as cur:
                cur.execute("""CREATE TABLE IF NOT EXISTS hh_vacancies(
                                vacantci_title varchar(100),
                                url varchar(100),
                                description text,
                                salary_from int,
                                salary_to int,
                                country varchar(30),
                                company_id int,
                                company_name varchar(100) NOT NULL,
                                CONSTRAINT fk_hh_vacancies_hh_companys FOREIGN KEY(company_id) REFERENCES hh_companys(company_id)
                                );""")
        conn.commit()

    def insert_table_hh_company(self, company_list):
        with psycopg2.connect(host="localhost",
                              database="hh",
                              user="postgres",
                              password="456852") as conn:
            with conn.cursor() as cur:
                for item in company_list:
                    cur.executemany("INSERT INTO hh_companys VALUES (%s, %s)",
                                    [(item['employer_id'], item['employer_name'])])


    def insert_table_hh_vacancies(self, vacant_list):
        with psycopg2.connect(host="localhost",
                              database="hh",
                              user="postgres",
                              password="456852") as conn:
            with conn.cursor() as cur:
                for item in vacant_list:
                    cur.executemany("INSERT INTO hh_vacancies VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                    [(item['name'],
                                      item['url'],
                                      item['description'],
                                      item['salary_from'],
                                      item['salary_to'],
                                      item['city'],
                                      item['employer_name'],
                                      item['employer_id'])])

