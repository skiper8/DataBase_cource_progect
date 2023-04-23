import psycopg2
from config import config


class DBmanager:
    params = config()

    def get_companies_and_vacancies_count(self):

        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT DISTINCT(company_name), COUNT(*) FROM hh_vacancies
                                GROUP BY company_name;""")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_all_vacancies(self):
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT company_name, title, salary, url FROM hh_vacancies;""")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_avg_salary(self):
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT AVG(salary) AS average_salary FROM hh_vacancies;""")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_vacancies_with_higher_salary(self):
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT * FROM hh_vacancies
                                WHERE salary > (SELECT AVG(salary) FROM hh_vacancies);""")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_vacancies_with_keyword(self):
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT * FROM hh_vacancies
                                WHERE vacantci_title LIKE '%Python%';""")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
