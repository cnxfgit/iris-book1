import streamlit as st
import seaborn as sns
import plotly.express as px

st.title('Welcome to the world of :red[Streamlit]')

st.header('Pandas DataFrame')

st.markdown('Load :blue[Iris Data Set]')

df = sns.load_dataset('iris')

st.write(df)

st.header('Visualize Using Heatmap')
fig = px.imshow(df.iloc[:, :-1])
st.write(fig)
