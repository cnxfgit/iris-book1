import streamlit as st

col1, col2 = st.columns(2)
col1.write('This is col1')

col1.latex(r'f(x) = ax^2 + bx + c')

col2.write('This is col2')
