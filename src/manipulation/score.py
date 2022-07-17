import os
import numpy as np
from dotenv import load_dotenv
import os.path
load_dotenv()
import datetime
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import matplotlib.pyplot as plt
def get_sheet(gss_sheet):
    json_path = os.getenv('JSON_KEY')
    gss_key=os.getenv('SPREADSHEET_KEY')
    gss_sheet=gss_sheet
    SCOPES = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    cred = ServiceAccountCredentials.from_json_keyfile_name(json_path, SCOPES)
    gs_auth = gspread.authorize(cred)
    sh=gs_auth.open_by_key(gss_key)
    ws=sh.worksheet(gss_sheet)
    return ws

date=datetime.today()

def gragh(data,name,month):
    plt.figure(figsize=(6,4))
    plt.plot(np.arange(len(data)),data)
    plt.xlabel('date')
    plt.ylabel(' score')
    plt.xlim(0, 32)
    plt.ylim(0, 140)
    
    plt.savefig(f'../../data/score_data/{name}_{month}.png')
    plt.show()

def get_data(date,name):
    name_dict=name_dict = {"orui":2, "kusumoto":3,"saito":4,"nomura":5}
    if date.day== 1:
        record=0
    else:
        record=np.load(f'../../data/score_data/{name}_score.npy')
    name_p=name_dict[name]
    month=date.month
    date_p=date.day
    if len(record)<date_p:
        record=np.append(record,np.array([record[-1]]*(date_p-len(record)-1)))
        print(len(record))
    if len(record)>date_p:
        print("error")
    ws=get_sheet( f'{month}月')
    score = ws.cell(34,name_p).value
    today_time= ws.cell(date_p+2,name_p).value
    E=datetime.strptime(today_time[6:],'%H:%M')
    L=datetime.strptime(today_time[:5],'%H:%M')
    today_score=(E-L).total_seconds()/3600
    re_score=today_score+float(score)
    record=np.append(record,re_score)
    gragh(record,name,date.month)
    np.save(f'../../data/score_data/{name}_score',record)
    re_score='{:.2f}'.format(re_score)
    ws.update_cell(34,name_p, re_score)
    return 


get_data(date,"orui")

