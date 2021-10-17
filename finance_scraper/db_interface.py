from os import replace
import sqlite3
import enum
db_file_name=""
default_db_file_name="data.db"
main_db_connaction=None
max_connection_attempts_count=3
standart_delimetr=","
standart_open_bracket="("
standart_closed_bracket=")"

class table_operations(enum.Enum):
    table_insert="INSERT INTO"
    table_create="CREATE TABLE"
    get_tables=""
    table_select="SELECT "

def create_attrib_tuple(open_bracket, close_bracket,attrib_list,delimetr):
    tmp_str=open_bracket
    for attrib in attrib_list:
        tmp_str+=attrib+delimetr
    if tmp_str[len(tmp_str)-1]==delimetr:
       tmp_str= tmp_str[:-1]
    tmp_str+=close_bracket
    return tmp_str

def connect_to_db(db_file_name, max_try_count):
    global main_db_connaction
    if not hasattr(connect_to_db,"try_connect_db_count"):
        connect_to_db.try_connect_db_count=0
    try:
       main_db_connaction= sqlite3.connect(db_file_name)
    except:
        db_file_name=default_db_file_name
        if connect_to_db.try_connect_db_count<max_try_count:
            connect_to_db.try_connect_db_count+=1
            connect_to_db(db_file_name,max_try_count)
        else:
            connect_to_db.try_connect_db_count=0

def get_create_query(operation,table_name, attribs_dict,if_not_exist_flag=True):
    tmp_str=operation.value+" "
    if if_not_exist_flag:
        tmp_str+=" IF NOT EXISTS "
    tmp_str+=table_name+" "
    tmp_str+= create_attrib_tuple(standart_open_bracket, standart_closed_bracket,[key+" "+attribs_dict[key] for key in attribs_dict.keys()],standart_delimetr)
    return tmp_str

def get_insert_query(operation,table_name, attribs_dict):
    tmp_str=operation.value+" "
    tmp_str+=table_name+" "
    tmp_str+= create_attrib_tuple(standart_open_bracket, standart_closed_bracket,attribs_dict.keys(),standart_delimetr)
    tmp_str+=" VALUES "
    tmp_str+= create_attrib_tuple(standart_open_bracket, standart_closed_bracket,attribs_dict.values(),standart_delimetr)
    return tmp_str

def get_select_query(operation,table_name, attribs,additional_clause):
     tmp_str=operation.value+" "
     if type(attribs) is list:
            tmp_str+=create_attrib_tuple(standart_open_bracket, standart_closed_bracket,attribs,standart_delimetr)
            tmp_str.replace(standart_open_bracket,"")
            tmp_str.replace(standart_closed_bracket,"")
     elif type(attribs) is str:
         tmp_str+=attribs
     
     tmp_str+=" FROM "+table_name
     if  additional_clause!=None:
        if "WHERE" not in additional_clause or "where" not in additional_clause:
            additional_clause=" WHERE "+additional_clause
        tmp_str+=" "+additional_clause
     return tmp_str


def exec_operation(db_name,table_operation,table_name=None, attribs_dict=None, additional_clause=None):
    global main_db_connaction
    global db_file_name
    global max_connection_attempts_count
    global db_file_name

    db_file_name=db_name
    if ".db" not in db_name:
        db_file_name+=".db"

    if main_db_connaction is None:
         connect_to_db(db_file_name,max_connection_attempts_count)
    if table_operation is table_operations.table_create and attribs_dict!=None and table_name!=None:
        query_str=get_create_query(table_operation,table_name, attribs_dict)
    if table_operation is table_operations.table_insert and attribs_dict!=None and table_name!=None:
        query_str=get_insert_query(table_operation,table_name, attribs_dict)
    if table_operation is table_operations.get_tables:
        query_str="SELECT name FROM sqlite_master WHERE type='table';"
    if table_operation is table_operations.table_select and attribs_dict!=None and table_name!=None:
        query_str=get_select_query(table_operation,table_name,attribs_dict,additional_clause)
    try:
        if table_operation is table_operations.get_tables or table_operation is table_operations.table_select:
            main_db_connaction.commit()
            result=main_db_connaction.cursor().execute(query_str)
            #rewrite
            if table_operation is table_operations.get_tables:
                result=[  e[0] for e in result.fetchall()]
            else: result=[  e for e in result.fetchall()]
            return result
        else:
            main_db_connaction.execute(query_str)
        
    except Exception as e:
        print(str(e))


    


