import streamlit as st
import pandas as pd
import numpy as np
st.title("Streamlit Session")
st.divider()
st.text('Hello',help='Text Help')
st.image('../Travel_Project/public/favicon.svg',width=60)
st.logo('../Travel_Project/public/favicon.svg')
st.divider()
st.button('Click here', type='primary')
st.button('Click here', type='secondary')
btn = st.button('Click here', type='tertiary')
if btn:
    st.write('You clicked.')
else:
    st.write('Go on, click.')
st.divider()
st.markdown('*Hello*')
st.markdown('**Hello**')
st.markdown('***Hello***')
st.divider()
st.button('Hit', icon=':material/home:')
st.radio('Select one',[1,2,3])

data  = pd.DataFrame(np.random.randn(15,3), ['A','B','C'])
st.line_chart(data=data)