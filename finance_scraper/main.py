import datetime
from os import replace
import requests
import db_interface
from db_interface import table_operations

base_download_url="https://query1.finance.yahoo.com/v7/finance/download/"
full_url=""
companies=("PD","ZUO","PINS","ZM","PVTL","DOCU","CLDR","RUN")
start_period_key="period1"
end_period_key="period2"
data_file_format=".csv"
data_file_format_delimetr=","
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
time_periods_dict={start_period_key:"0",end_period_key:"-1"}
invalidCharacters={ "~", "@", "#", "$", "%", "^", "-", "(", ")", "{", "}", "`", "+", "=", "[", "]", ":",
                                             ",", ";", "/", "?","/","\\",":","*","?","«","»","<",">","|","&","—","\\"," ","'","\n","\t"}
db_name="data.db"

def replace_invalid_charter(key):
    key=key.replace(" ","_")
    for invalid_charter in  invalidCharacters:
        key=key.replace(invalid_charter,"")
    return key

def add_url_param(url,param,val):
    tmps_str=""
    if "?" not in url:
        tmps_str+="?"
    tmps_str+=param+"="+str(val)+"&"
    return tmps_str

def get_unix_timespan():
    return int(datetime.datetime.timestamp(datetime.datetime.today()))
    
if end_period_key not in time_periods_dict.keys():
    time_periods_dict[end_period_key]="-1"
    
#https://query1.finance.yahoo.com/v7/finance/download/PD?period1=0&period2=1630368000
for company_name in companies:
    full_url=base_download_url+company_name
    time_periods_dict[end_period_key]=get_unix_timespan()
    for url_param_key in time_periods_dict:
        full_url+=add_url_param(full_url,url_param_key,time_periods_dict[url_param_key])
    data_response=requests.get(full_url,stream=True, headers=headers)
    full_file_name=company_name+data_file_format
    with open(full_file_name,'wb') as out_file:
        try:
          out_file.write(data_response.content)
          out_file.close()
        except: pass
    db_table_attribs_dict=dict()
    
    with open(full_file_name,'r') as r_file:
       table_attribs=r_file.readline().split(data_file_format_delimetr)
       for key in table_attribs:
           key=replace_invalid_charter(key)
           db_table_attribs_dict[key]="TEXT"
       db_interface.exec_operation(db_name,table_operations.table_create,company_name,db_table_attribs_dict)
       db_table_attribs_dict.clear()
    #add data to db
       for line in r_file.readlines():
                for attrib,key in zip( line.split(data_file_format_delimetr),table_attribs):
                    key=replace_invalid_charter(key)
                    attrib=replace_invalid_charter(attrib)
                    db_table_attribs_dict[key]=attrib
                db_interface.exec_operation(db_name,table_operations.table_insert,company_name,db_table_attribs_dict)
    db_interface.main_db_connaction.commit()
