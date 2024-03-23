import streamlit as st

tab_A, tab_B = st.tabs(["Tab A", "Tab B"])

with tab_A:
    st.header('Tab A Title')
    st.write('This is Tab A.')

with tab_B:
    st.header('Tab B Title')
    st.write('This is Tab B.')