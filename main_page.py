import streamlit as st  
from pytz import timezone
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



st.title("ERD") 
_abspath = os.path.dirname(os.path.abspath(__file__))
image_path1 = _abspath + '/1.png'

image1 = Image.open(image_path1)
st.image(image1)

st.header("Index 활용 실습") 

st.write(
    "ex) 예금 잔액이 1만원이상~5만원 미만이면서 2년이상 거래가 없는 계좌"
)

st.header("partitioning 활용 실습") 

st.write(
    "ex) 예금 잔액이 1만원이상~5만원 미만이면서 2년이상 거래가 없는 계좌"
)
st.header("window function 활용 실습") 

st.write(
    "ex) 예금 잔액이 1만원이상~5만원 미만이면서 2년이상 거래가 없는 계좌"
)