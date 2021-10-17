from enum import Enum
from flask import Flask, jsonify,abort
from flask.wrappers import Response
import db_interface

db_name="data.db"
flask_host="localhost"
flask_port="5000"
class RestOperation(Enum):
    get_api_description="/"
    get_companies_list="/finance_scrapper/companies"
    get_all_companies_data=get_companies_list+"/all"
    get_specific_company_data=str(get_companies_list+"/")
    


#base_api_path="http://"+flask_host+"/"
rest_api = Flask(__name__)

@rest_api.route(RestOperation.get_api_description.value)
def index():
    desc_str=""
    for item in list(RestOperation):
       desc_str+="operation: "+item.name+" - uri: "+item.value+"\n\b"
    return desc_str

@rest_api.route(RestOperation.get_companies_list.value)
def get_companies_list():
    return jsonify( db_interface.exec_operation(db_name,db_interface.table_operations.get_tables))

@rest_api.route(RestOperation.get_all_companies_data.value)
def get_all_companies_data():
    ret_data=list()
    table_names=db_interface.exec_operation(db_name,db_interface.table_operations.get_tables)
    for table_n in table_names:
        ret_data.append(list(db_interface.exec_operation(db_name,db_interface.table_operations.table_select,table_n,"*")))
    return jsonify(ret_data)
    
@rest_api.route(RestOperation.get_specific_company_data.value+"<string:company_name>")
def get_specific_company_data(company_name):
        if company_name in db_interface.exec_operation(db_name,db_interface.table_operations.get_tables):
            return jsonify(db_interface.exec_operation(db_name,db_interface.table_operations.table_select,company_name,"*"))
        else:
            abort(Response("Cannot find company:"+str(company_name)))


    

if __name__=='__main__':
    rest_api.run(host=flask_host,port=flask_port, debug=True)