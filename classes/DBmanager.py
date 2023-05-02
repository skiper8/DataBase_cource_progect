import psycopg2
from config import config


class DBmanager:
    params = config()

    def get_companies_and_vacancies_count(self):
        """
        Получает список всех компаний и количество вакансий у каждой компании.
        """
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT DISTINCT(company_name), COUNT(*) FROM hh_vacancies
                                GROUP BY company_name;""")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_all_vacancies(self):
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
        """
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT company_name, title, salary, url FROM hh_vacancies;""")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_avg_salary(self):
        """
        Получает среднюю зарплату по вакансиям.
        """
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT AVG(salary) AS average_salary FROM hh_vacancies;""")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_vacancies_with_higher_salary(self):
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
        """
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("""SELECT * FROM hh_vacancies
                                WHERE salary > (SELECT AVG(salary) FROM hh_vacancies);""")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_vacancies_with_keyword(self):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.
        """
        keyword = input("Введите слово для поиска - ")
        with psycopg2.connect(dbname='hh', **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM hh_vacancies WHERE title ILIKE '%{keyword}%';")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
