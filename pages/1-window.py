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
SQL=''

if not SQL:
    SQL = '''SELECT * FROM salaries WHERE emp_no=20000;'''
SQL1 = '''SELECT 
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

SQL2 = '''SELECT emp_no, from_date, salary,
LAG(salary, 1, 0) OVER (PARTITION BY emp_no ORDER BY emp_no) as last_year_salary, 
salary - LAG(salary, 1, 0) OVER (PARTITION BY emp_no ORDER BY emp_no) as 연봉차이
FROM salaries;'''

st.title("WINDOW FUNCTION") 
_abspath = os.path.dirname(os.path.abspath(__file__))
image_path1 = _abspath + '/1.png'

image1 = Image.open(image_path1)
st.image(image1)

cursor = db.cursor()
cursor.execute(SQL1)
columns = cursor.description 
result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
import time
start = time.time()
with st.sidebar.form("Input"):
    queryText = st.text_area("SQL to execute:", height=3, max_chars=None)
    st.sidebar.text(f'없이 하는 쿼리')
    btnResult = st.form_submit_button('Run')
with st.sidebar.form("Input2"):
    queryText = st.text_area("SQL to execute:", height=3, max_chars=None)
    st.sidebar.text(f'있이 하는 쿼리')
    btnResult1 = st.form_submit_button('Run')
SQL1=queryText
SQL2=queryText
if btnResult:
    st.sidebar.text(f'Button pushed')
    start = time.time()

    try:
        cursor.execute(SQL1)
        columns = cursor.description 
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    except:
        df='query 제대로 입력해'
if btnResult1:
    st.sidebar.text(f'Button pushed')
    start = time.time()

    try:
        cursor.execute(SQL2)
        columns = cursor.description 
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    except:
        df='query 제대로 입력해'

df=pd.DataFrame(result)

st.write(
    "ex) 예금 잔액이 1만원이상~5만원 미만이면서 2년이상 거래가 없는 계좌"
)
st.write(
    df,
    "time = ", time.time()-start
)