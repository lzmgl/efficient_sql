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