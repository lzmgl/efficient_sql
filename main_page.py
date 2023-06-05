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
    "Index 활용 X"
)
st.write(
    "SELECT * FROM sal_ran WHERE emp_no=20000;;"
)
st.write(
    "Index 활용 O"
)
st.write(
    "SELECT * FROM salaries WHERE emp_no=20000;;"
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
    "SELECT id,balance,last_date FROM bct_amt WHERE balance>=10 AND balance<50;"
)
st.write(
    "Partition 활용 O"
)
st.write(
    "SELECT id,balance,last_date FROM bct_amt_part WHERE balance>=10 AND balance<50;"
)
st.header("window function 활용 실습 : 전 행과의 차이값 계산") 
st.write(
    "ex) 지난 해와 연봉 차이"
)
image3 = Image.open(_abspath + '/esset/1.png')
st.image(image3)
st.write(
    'window 활용 O'
)
st.write(
    '''SELECT emp_no, from_date, salary, LAG(salary, 1, 0) OVER (PARTITION BY emp_no ORDER BY emp_no) as last_year_salary, 
salary - LAG(salary, 1, 0) OVER (PARTITION BY emp_no ORDER BY emp_no) as 연봉차이
FROM salaries;'''
)
st.write(
    'window 활용 X'
)
st.write(
    '''SELECT 
    emp_no, 
    from_date, 
    salary, 
    COALESCE((
        SELECT salary 
        FROM salaries s2 
        WHERE s2.emp_no = s1.emp_no 
        AND s2.from_date < s1.from_date 
        ORDER BY s2.from_date DESC 
        LIMIT 1
    ), 0) as last_year_salary,
    salary - COALESCE((
        SELECT salary 
        FROM salaries s2 
        WHERE s2.emp_no = s1.emp_no 
        AND s2.from_date < s1.from_date 
        ORDER BY s2.from_date DESC 
        LIMIT 1
    ), 0) as 연봉차이
FROM salaries s1;'''
)