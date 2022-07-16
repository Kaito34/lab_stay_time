import os
from dotenv import load_dotenv
import os.path
load_dotenv()
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

test=pd.read_csv('test.csv',index_col=0)
# print(test.index.values)
name_dict = {"A":2,  "B":3,"C":4,"D":5,	"かきくけこ":6 }
for name in test.index.values:
    name_p=name_dict[name]
    date_p=test.loc[name,"date"]
    month=test.loc[name,"month"]
    # ws=get_sheet( f'{month}月')
    V=test.loc[name,"time"]
    V_end=test.loc[name,"end_time"]

    # worksheet.update_cell(1, 2, '更新する値')








