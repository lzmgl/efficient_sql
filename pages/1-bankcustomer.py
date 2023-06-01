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
with st.sidebar.form("Input"):
    queryText = st.text_area("SQL to execute:", height=3, max_chars=None)
    btnResult = st.form_submit_button('Run')
if btnResult:
    tm = time.localtime(time.time())
    st.sidebar.text(f'Button pushed {tm}')
    start = time.time()
SQL = queryText
try:
    if not SQL:
        SQL = '''SELECT * FROM salaries WHERE emp_no=20000;'''
    cursor = db.cursor()
    cursor.execute(SQL)
    columns = cursor.description 
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    df=pd.DataFrame(result)
except:
    df='query 제대로 입력해'
st.write(
    SQL,
    "   \n",
    df,
    "   \n",
    "time = ", time.time()-start
)