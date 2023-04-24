---Получает список всех компаний и количество вакансий у каждой компании.
SELECT DISTINCT(company_name), COUNT(*) FROM hh_vacancies
GROUP BY company_name;

---Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
SELECT company_name, title, salary, url FROM hh_vacancies;

---Получает среднюю зарплату по вакансиям.
SELECT AVG(salary) AS average_salary FROM hh_vacancies;

---Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
SELECT * FROM hh_vacancies
WHERE salary > (SELECT AVG(salary) FROM hh_vacancies);

---Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.
SELECT * FROM hh_vacancies
WHERE vacantci_title LIKE '%Python%';