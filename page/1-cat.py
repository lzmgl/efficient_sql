import streamlit as st  

from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os

cat_image_paths=os.path.join(path_now, '..', 'esset', 'cat')
cat_image_files=os.listdir(cat_image_paths)
select = st.sidebar.selectbox('사진 3개중에 골라', cat_image_files)
st.image(Image.open(os.path.join(cat_image_paths, select)))
