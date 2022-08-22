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
    name_p=name_dict[name]
    month=date.month
    date_p=date.day
    ws=get_sheet( f'{month}月')
    score = ws.cell(34,name_p).value
    today_time= ws.cell(date_p+2,name_p).value
    E=datetime.strptime(today_time[6:],'%H:%M')
    L=datetime.strptime(today_time[:5],'%H:%M')
    today_score=(E-L).total_seconds()/3600
    re_score=today_score+float(score)
    ws.update_cell(34,name_p, re_score)
    return re_score




