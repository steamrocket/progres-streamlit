from threading import Condition
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('ICE BOOK')

st.write('Display')
'Start'

latest_inteation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_inteation.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

if st.checkbox('Show Iamge'):
    img = Image.open('samplecat.jpg')
    st.image(img, caption='cat cafe', use_column_width=True)

#option = st.selectbox(
#    'select number',
#    list(range(1,11))
#)

text = st.sidebar.text_input('好みのコーヒーは？')
condition = st.sidebar.slider('コーヒーの量',0, 100, 50)
'好きなコーヒーの種類:',text
'何g:', condition


#df = pd.DataFrame(
#   np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=['lat','lon']
#)
#st.map(df)
