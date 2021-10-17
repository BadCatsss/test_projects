from aiogram.types.base import String
import json
import os


file_read_res=None

def create_default_conf(configs:dict()):
    for cnf in configs:
        with open(cnf,'w') as f:
            f.write(configs[cnf])
            f.close()


def read_conf_file(file_name:String,file_default_value):
    global file_read_res
    file_read_res=None
    if os.path.exists(file_name):
        with open(file_name,'r') as file:
            try:
                file_read_res=json.load(file)
            except Exception as e:
                print(e)
            finally:
                file.close()
                return file_read_res
    else:
        create_default_conf({file_name:file_default_value})
        read_conf_file(file_name,file_default_value)

def read_tken_file(bot_token_file_path):
     with open(bot_token_file_path,'r') as f:
        client_bot_token=f.readline()
        f.close()
        return client_bot_token