import pandas as pd

# from sqlalchemy import create_engine
# create_engine('mysql+pymysql://root:root@localhost:3306/bankdetails')
# query = 'SELECT * FROM BANKDETAILS'
# data=pd.read_sql(query,engine)

pd.read_json('new.json')