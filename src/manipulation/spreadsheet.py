import os
from time import time
from tracemalloc import start
from unicodedata import name
from dotenv import load_dotenv
import os.path

from pip import main
load_dotenv()
import datetime
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd
import requests
import json

global name_dict
name_dict = {"orui": 2, "kusumoto": 3, "saito": 4, "nomura": 5}


def get_sheet(gss_sheet):
    json_path = os.getenv('JSON_KEY')
    gss_key = os.getenv('SPREADSHEET_KEY')
    gss_sheet = gss_sheet
    SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    cred = ServiceAccountCredentials.from_json_keyfile_name(json_path, SCOPES)
    gs_auth = gspread.authorize(cred)
    sh = gs_auth.open_by_key(gss_key)
    ws = sh.worksheet(gss_sheet)
    return ws


def put_data(date, name):
    name_p = name_dict[name]
    date_p = date.day
    month = date.month
    ws = get_sheet(f'{month}月')
    time_v = f'{date.hour}:{date.minute}'
    cell_value = ws.cell(date_p, name_p).value
    if str(cell_value) == "None":
        input_V = f'{time_v}'
    elif '-' in str(cell_value):
        input_V = f'{cell_value[:5]}-{time_v}'
    else:
        start_tim = cell_value
        input_V = f'{start_tim}-{time_v}'
    ws.update_cell(date_p, name_p, input_V)


def send_slack(text):
    # DO
    WEB_HOOK_URL = os.getenv('SLACK_URL')
    requests.post(WEB_HOOK_URL, data=json.dumps({
        'text': text
    }))


def notify_airhead():
    name_dict = {"orui": 2, "kusumoto": 3, "saito": 4, "nomura": 5}
    date = datetime.datetime.today()
    date_p = date.day + 2
    month = date.month
    ws = get_sheet(f'{month}月')

    # 退室時間未記入者の洗い出し
    airhead_list = []
    for k, v in name_dict.items():
        cell_value = ws.cell(date_p, v).value
        if cell_value is None:
            continue
        if cell_value[-1] == '-':  # 退室時間未記入の場合
            airhead_list.append(k)

    df_slack_id = pd.read_csv('data/external/slack_id.csv')
    airhead_id_list = df_slack_id[df_slack_id['name'].isin(airhead_list)]['id'].tolist()
    send_slack(
        f"{''.join([f'<@{m}>' for m in airhead_id_list])} 管理表の記入お願いします"
    )


if __name__ == "main":
    notify_airhead()
