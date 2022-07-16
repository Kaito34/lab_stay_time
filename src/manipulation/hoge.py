import os
from dotenv import load_dotenv
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
load_dotenv()
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.client import GoogleCredentials
import gspread
from googleapiclient.discovery import build
from apiclient import discovery
import pandas as pd


json_path = os.getenv('JSON_KEY')
gss_key=os.getenv('SPREADSHEET_KEY')
gss_sheet='sheet1'
SCOPES = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
cred = ServiceAccountCredentials.from_json_keyfile_name(json_path, SCOPES)
gs_auth = gspread.authorize(cred)
sh=gs_auth.open_by_key(gss_key)
ws=sh.worksheet(gss_sheet)
data=ws.get_all_values()
df=pd.DataFrame(data)


