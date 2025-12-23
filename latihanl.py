import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit application.")

st.write('ini contoh *huruf miring*')
st.write('ini contoh **huruf tebal**')
st.write('ini contoh ***huruf tebal miring***')

penjualan_oktober = 900
penjualan_november = 850
penjualan_desember = 1000

selisih1 = penjualan_desember - penjualan_november
selisih2 = penjualan_november - penjualan_oktober

st.metric(label='Penjualan Sekarang', value = penjualan_desember, delta = selisih1)
st.metric(label='Penjualan Sebelumnya', value = penjualan_november, delta = selisih2)

df = pd.read_csv('healthcare-dataset-stroke-data.csv')
st.dataframe(df)

st.line_chart(df['age'].value_counts().sort_index())

category_df = df['gender'].value_counts(dropna=False).reset_index()
category_df.columns = ['gender', 'count']
fig = px.pie(category_df, names='gender', values='count')
st.plotly_chart(fig, use_container_width=True)

st.bar_chart(df['work_type'].value_counts().sort_index())

st.write('**5. Button**')
st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else: 
    st.write("Goodbye")
if st.button("Aloha", type="tertiary"):
    st.write("Ciao")

st.write('**6. Checkbox**')
agree = st.checkbox("I agree")
if agree:
    st.write("Great!")

st.write('**7. Multiselect**')
options = st.multiselect(
    "What are your favorite colors",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"],
)
st.write("You Selected:", options)

col1, col2 = st.columns(2)
with col1:
    st.bar_chart(df['work_type'].value_counts().sort_index())
with col2:
    st.line_chart(df['age'].value_counts().sort_index())

col1, col2, col3, = st.columns(3)
with col1:
    st.write('ini contoh *huruf miring*')
    st.write('ini contoh **huruf tebal**')
    st.write('ini contoh ***huruf tebal miring***')
with col2:
    st.metric(label='Penjualan Sekarang', value = penjualan_desember, delta = selisih1)
with col3:
    st.metric(label='Penjualan Sebelumnya', value = penjualan_november, delta = selisih2)

tab1, tab2 = st.tabs(['Line', 'Bar'])
with tab1:
    st.line_chart(df['age'].value_counts().sort_index())
with tab2:
    st.bar_chart(df['work_type'].value_counts().sort_index())

st