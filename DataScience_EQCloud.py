import requests
import pandas as pd
from pandas.io.json import json_normalize                      
import getpass
from tqdm import tqdm

import warnings; warnings.filterwarnings('ignore')

#request_config = []

def initiate_config():
    global creds
    creds = set_user_creds()
    reqConf = set_request_config()
    columnList = set_request_columns()
    print('')
    print('Next, call a request function and assign a variable (example: df = request_processvalues())')
    global request_config
    request_config = [list(reqConf), columnList]
    #return request_config

def set_user_creds():
    print('Please fill in:')
    print('Equipment Cloud username:')
    user = input()
    print('')
    print('Password:')
    pwd = getpass.getpass()
    print('')
    return user, pwd

def set_request_config():
    print('Define equipment to fetch data from:')
    equipment = input()
    print('')
    print('Define start time (example: 2019-03-10T00:00:00):')
    start_time = input()
    print('')
    print('Define end time (example: 2019-03-25T00:00:00):')
    end_time = input()
    print('')
    return equipment, start_time, end_time

def set_request_columns():
    ###### Hier noch Abfrage zu vorhandenen Datenspalten für das jeweilige Equipment ######
    print('Define columns to be fetched (use comma to seperate):')
    columnList = input()
    columnList = columnList.split(',')
    return columnList

def change_user():
    print('Set new username:')
    creds[0][0] = input()
    #return request_config

def change_password():
    print('Set new password:')
    creds[0][1] = getpass.getpass()
    #return request_config

def change_equipment():
    print('Define new equipment to fetch data from:')
    request_config[0][0] = input()
    #return request_config

def change_startTime():
    print('Define new start time (example: 2019-03-10T00:00:00):')
    request_config[0][1] = input()
    #return request_config

def change_endTime():
    print('Define new end time (example: 2019-03-25T00:00:00):')
    request_config[0][2] = input()
    #return request_config

def set_startTime(time):    
    request_config[0][1] = time
    
def set_endTime(time):    
    request_config[0][2] = time
    
def change_request_columns():
    ###### Hier noch Abfrage zu vorhandenen Datenspalten für das jeweilige Equipment ######
    request_config[1].clear()
    print('Set new columns to be fetched (use comma to seperate):')
    request_config[1] = input()
    request_config[1] = [request_config[1]]
    #return request_config

def request_processvalues():
    temp_df = pd.DataFrame()
    user = creds[0]
    pwd = creds[1]
    equipment = request_config[0][0]
    start_time = request_config[0][1]
    end_time = request_config[0][2]
    columnList = request_config[1]
    code = {
        'qp':"{"+'"'+"ts_start"+'":'+'"'+start_time+"+01:00"+'"'+","+'"'+"ts_end"+'"'+':'+'"'+end_time+"+01:00"+'"'+"}",
        'step':'1'
            }
    for i in tqdm(range(len(columnList))):
            response = requests.get("https://vm1477.de-ais.r-r.local/ords/dev/cloudconnect/api/monitoring/v2/history/things/" + equipment + "/processvalues/" + columnList[i].strip().replace("'","") + "",
                                     auth=requests.auth.HTTPBasicAuth(user, pwd),
                                     params=code,
                                     verify=False)
            json = response.json()
            df = pd.DataFrame.from_dict(json['items'])
            #dd = pd.DataFrame.from_dict(json['controls'])
            #print(dd)
            df['ChannelID'] = columnList[i].strip().replace("'","")
            if "value_string" in df.columns:
                df.rename(columns={'value_string': 'value'}, inplace=True)
            else: pass
            frames = [temp_df,df]
            temp_df = pd.concat(frames,sort=True)
    EQ_Cloud_DataFrame = pd.DataFrame()
    EQ_Cloud_DataFrame = temp_df.pivot_table(values='value', index=['timestamp','material_id'], columns=['ChannelID'], aggfunc=lambda x: ' '.join(str(v) for v in x))
    fkt_columns_to_numbers(EQ_Cloud_DataFrame)
    return EQ_Cloud_DataFrame
    
## umwandeln aller columns in numbers
def fkt_columns_to_numbers(df_input): 
    for i_col in tqdm(df_input.columns):
        # converting to numeric
        try:
            #df_input[i_col] = df_input[i_col].astype('float64')
            df_input[i_col] = pd.to_numeric(df_input[i_col],downcast='signed')
        #except ValueError:
        except:
            print('not converted to numeric:', i_col)    
    
def functions():
    pd.set_option('display.max_colwidth', -1)
    data = {
            'function': ['initiate_config()', #1
                         'set_user_creds()', #2
                         'set_request_config()', #3 
                         'change_user()', #4
                         'change_password()', #5
                         'change_equipment()', #6
                         'change_startTime()', #7
                         'change_endTime()', #8
                         'set_startTime(time)', #9
                         'set_endTime(time)',#10
                         'set_request_columns()', #11
                         'request_processvalues()', #12
                        ],
            'description': ['combines function calls "type_user_creds()" and "define_request_config()" for initial parameter input', #1
                            'define or change user credentials', #2
                            'define or change all request params', #3
                            'change user name', #4
                            'change password', #5
                            'change equipment', #6
                            'change first date for data to be fetched', #7
                            'change last date for data to be fetched ', #8
                            'set start time with a function call parameter', #9
                            'set end time with a function call parameter', #10
                            'set the column names from which the data will be fetched', #11
                            'fetch equipment specific process values from the EQ-Cloud', #12
                           ]
    }
    function_help = pd.DataFrame(data)
    return function_help