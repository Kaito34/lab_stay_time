import os
from time import time
from tracemalloc import start
from dotenv import load_dotenv
import os.path
load_dotenv()
import datetime
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd


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


date=datetime.datetime.today()

def put_data(date,name):
    name_dict=name_dict = {"O":2,  "K":3,"S":4,"N":5}
    name_p=name_dict[name]
    date_p=date.day
    month=date.month
    ws=get_sheet( f'{month}月')
    time_v=f'{date.hour}:{date.minute}'
    cell_value = ws.cell(date_p,name_p).value
    if  str(cell_value) == "None":
        input_V=f'{time_v}'
    elif '-' in str(cell_value):
        input_V=f'{cell_value[:5]}-{time_v}'
    else:
        start_tim=cell_value
        input_V=f'{start_tim}-{time_v}'
    ws.update_cell(date_p,name_p, input_V)

put_data(date,name="S")








