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

sql_list={
          'window 없이' : '''SELECT 
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
FROM salaries s1;''',
'window 활용':
'''SELECT emp_no, from_date, salary, LAG(salary, 1, 0) OVER (PARTITION BY emp_no ORDER BY emp_no) as last_year_salary, 
salary - LAG(salary, 1, 0) OVER (PARTITION BY emp_no ORDER BY emp_no) as 연봉차이
FROM salaries;''',
'partitioning 없이':
'''SELECT id,balance,last_date FROM bct_amp WHERE balance>=10 AND balance<50 AND last_date>'2018-01-01';''', 

'partitioning 활용':
'''SELECT id,balance,last_date FROM bct_amp_part WHERE balance>=10 AND balance<50 AND last_date>'2018-01-01';''',
'index 없이':
'''SELECT * FROM sal_ran WHERE emp_no=20000;''',
'index 활용':
'''SELECT * FROM salaries WHERE emp_no=20000;'''
}
db = pymysql.connect(
    host=host_name,     # MySQL Server Address
    port=host_port,          # MySQL Server Port
    user=username,      # MySQL username
    passwd=password,    # password for MySQL username
    db=database_name,   # Database name
    charset='utf8'
)



st.title("EFFICIENT SQL") 

import time
start = time.time()
with st.sidebar.form("Input"):
    queryText = st.text_area("SQL to execute:", height=3, max_chars=None)
    # queryText=st.radio('Select one:', sql_list)
    btnResult = st.form_submit_button('Run')
if btnResult:
    st.sidebar.text(f'Button pushed')
    start = time.time()
SQL = queryText
try:
    if not SQL:
        SQL = ''''''
    cursor = db.cursor()
    cursor.execute(SQL)
    columns = cursor.description 
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    dur_time=time.time()-start
    df=pd.DataFrame(result)
except:
    df='query 입력해주세요'

st.write(
    SQL,
    "   \n",
    df,
    "   \n",
    "time = ", dur_time
)

