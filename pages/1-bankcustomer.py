import streamlit as st  

from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os



import pymysql
import pandas as pd


host_name = "woori-fisa.cfnz7hfzq9bn.ap-northeast-2.rds.amazonaws.com"
host_port = 3306
username = "admin"
password = "woorifisa1!"
database_name = 'SQL_IMPROVE'

db = pymysql.connect(
    host=host_name,     # MySQL Server Address
    port=host_port,          # MySQL Server Port
    user=username,      # MySQL username
    passwd=password,    # password for MySQL username
    db=database_name,   # Database name
    charset='utf8'
)



st.title("INDEX") 

import time
start = time.time()
SQL = st.text_input('Enter query')
if not SQL:
    SQL = '''SELECT * FROM salaries WHERE emp_no=20000;'''
cursor = db.cursor()
cursor.execute(SQL)
columns = cursor.description 
result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
df=pd.DataFrame(result)
st.write(
    "sql = ", SQL,
    df,
    "time = ", time.time()-start
)
if btnResult:
    st.sidebar.text('Button pushed')

    # run query
    st.write(queryText)