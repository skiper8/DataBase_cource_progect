from classes.DBcreater import *
from classes.request_hh import *
from utils.utils import *

i = HH()
company_list = i.get_request_company()
i.insert_company(company_list)
vacancies_list_hh = i.get_request_vacantcies(company_list)
i.insert_vacancies(vacancies_list_hh)
vacant_list = load_json_vacancies('vacantes.json')
g = DBcreater()
g.createDB()
g.create_table_hh_companys()
g.create_table_hh_vacancies()
g.insert_table_hh_company(company_list)
g.insert_table_hh_vacancies(vacant_list)