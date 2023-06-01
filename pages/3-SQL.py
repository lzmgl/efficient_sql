import streamlit as st  

from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os
path_now = os.path.dirname(os.path.abspath(__file__))
dog_image_paths=os.path.join(path_now, '..', 'esset', 'dog')
dog_image_files=os.listdir(dog_image_paths)

# select = st.sidebar.selectbox('사진 3개중에 골라', dog_image_files)
with st.sidebar:
    add_radio = st.radio(
        "개 사진 골라",
        (dog_image_files)
    )
st.image(Image.open(os.path.join(dog_image_paths, add_radio)))


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
sql = '''SELECT * FROM salaries WHERE emp_no=20000;'''
cursor = db.cursor()
cursor.execute(SQL)
result = cursor.fetchall()  
st.write(
    "sql = ", sql,
    "result = ", result
)