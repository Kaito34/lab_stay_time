import os
from dotenv import load_dotenv
load_dotenv()
from oauth2client.client import GoogleCredentials
import gspread
import pandas as pd
json_path = os.getenv('JSON_KEY')
gss_key=os.getenv('SPREADSHEET_KEY')
api = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# request = service.spreadsheets().create(body=spreadsheet_body)
# response = request.execute()