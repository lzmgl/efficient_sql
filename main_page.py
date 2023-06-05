import streamlit as st  
from pytz import timezone
from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os



import pymysql
import pandas as pd


st.title("ERD") 
_abspath = os.path.dirname(os.path.abspath(__file__))

image0 = Image.open(_abspath + '/esset/erd.png')
st.image(image0)



st.header("Index 활용 실습: id로 정보 찾기") 
st.write(
    "ex) id가 20000인 정보"
)

image1 = Image.open(_abspath + '/esset/1.png')
st.image(image1)
st.write(
    "sql"
)
st.header("partitioning 활용 실습 : 거래중지대상 계좌") 
st.write(
    "ex) 예금 잔액이 1만원이상~5만원 미만이면서 2018년 1월 1일 이후 거래가 없는 계좌"
)
image2 = Image.open(_abspath + '/esset/1.png')
st.image(image2)
st.write(
    "sql"
)
st.header("window function 활용 실습 : 전 행과의 차이값 계산") 
st.write(
    "ex) 지난 해와 연봉 차이"
)
image3 = Image.open(_abspath + '/esset/1.png')
st.image(image3)
st.write(
    "sql"
)