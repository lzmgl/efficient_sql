import streamlit as st  
from pytz import timezone
from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os



import pymysql
import pandas as pd


st.title("ERD") 
_abspath = os.path.dirname(os.path.abspath(__file__))

image0 = Image.open(_abspath + '/esset/erderd.png')
st.image(image0)



st.header("Index 활용 실습: id로 정보 조회") 
st.write(
    "ex) id가 20000인 정보"
)

image1 = Image.open(_abspath + '/esset/1.png')
st.image(image1)
st.write(
    "Index 활용 X"
)
st.write(
    "SELECT * FROM sal_ran WHERE emp_no=20000;"
)
st.write(
    "Index 활용 O"
)
st.write(
    "SELECT * FROM salaries WHERE emp_no=20000;"
)
st.header("partitioning 활용 실습 : 거래중지대상 계좌") 
st.write(
    "ex) 예금 잔액이 1만원이상~5만원 미만이면서 2018년 1월 1일 이후 거래가 없는 계좌"
)
image2 = Image.open(_abspath + '/esset/1.png')
st.image(image2)
st.write(
    "Partition 활용 X"
)
st.write(
    "SELECT id,balance,last_date FROM bct_amt WHERE balance>=10 AND balance<50 AND last_date>'2018-01-01';"
)
st.write(
    "Partition 활용 O"
)
st.write(
    "SELECT id,balance,last_date FROM bct_amt_part WHERE balance>=10 AND balance<50 AND last_date>'2018-01-01';"
)
st.header("window function 활용 실습 : 전 행과의 차이값 계산") 
st.write(
    "ex) 연 평균 잔고 순위"
)
image3 = Image.open(_abspath + '/esset/1.png')
st.image(image3)
st.write(
    'window 활용 O'
)
st.write(
    '''SELECT id, balance, 
ROW_NUMBER() OVER(ORDER BY balance desc)
FROM bankcus5000;'''
)
st.write(
    'window 활용 X'
)
st.write(
    '''SELECT id, balance,
(SELECT COUNT(*) FROM bankcus5000 a
WHERE a.balance <= b.balance)
FROM bankcus5000 b
ORDER BY balance DESC;'''
)