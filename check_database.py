from DBtools import DataBaseConnection

data_base = DataBaseConnection('dev') # 保険のデータベース
data_base.show_all()
data_base = DataBaseConnection('main') # 本番のデータベース