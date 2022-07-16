import os
from dotenv import load_dotenv
load_dotenv()
from oauth2client.client import GoogleCredentials
import gspread
import pandas as pd
json_path = "../../secret/micro-handler-356505-03f1e8bae92f.json"
gss_key=os.getenv('SPREADSHEET_KEY')
api = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# request = service.spreadsheets().create(body=spreadsheet_body)
# response = request.execute()