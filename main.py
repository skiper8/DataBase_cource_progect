from classes.DBcreater import *
from classes.DBmanager import *
from classes.request_hh import *
from utils.utils import *


#i = HH()
#company_list, company_id = i.get_request_company()
#i.insert_company(company_list)
#vacancies_list_hh = i.get_request_vacantcies(company_id)
#i.insert_vacancies(vacancies_list_hh)

vacant_list = load_json_file('vacantes.json')
company_list = load_json_file('companys.json')

g = DBcreater()
g.createDB()
g.create_table_hh_companys()
g.create_table_hh_vacancies()
g.insert_table_hh_company(company_list)
g.insert_table_hh_vacancies(vacant_list)

m = DBmanager()
m.get_all_vacancies()
