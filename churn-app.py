import streamlit as st
import pandas as pd
import plotly.express as px

# Judul aplikasi
st.title('Analisis Churn Pelanggan')

# Memuat dataset
try:
    df = pd.read_csv('customer_churn.csv')
except FileNotFoundError:
    st.error("File 'customer_churn.csv' tidak ditemukan. Pastikan file tersebut berada di direktori yang sama dengan script Streamlit Anda.")
    st.stop()

# Menampilkan dataset (opsional)
if st.checkbox('Tampilkan Dataset'):
    st.dataframe(df)

# Visualisasi Data

st.header('Visualisasi Data')

# Distribusi Churn
st.subheader('Distribusi Churn Pelanggan')
churn_counts = df['Exited'].value_counts()
fig_churn = px.pie(churn_counts, 
                   values=churn_counts.values, 
                   names=['Tidak Churn (0)', 'Churn (1)'], 
                   title='Persentase Pelanggan yang Churn vs Tidak Churn')
st.plotly_chart(fig_churn)

# Distribusi Usia berdasarkan Churn
st.subheader('Distribusi Usia berdasarkan Churn')
fig_age_churn = px.histogram(df, x='Age', color='Exited', 
                             title='Distribusi Usia Pelanggan berdasarkan Status Churn',
                             labels={'Exited': 'Status Churn (0: Tidak, 1: Churn)'})
st.plotly_chart(fig_age_churn)

# Distribusi Gaji berdasarkan Churn
st.subheader('Distribusi Estimasi Gaji berdasarkan Churn')
fig_salary_churn = px.histogram(df, x='EstimatedSalary', color='Exited', 
                                title='Distribusi Estimasi Gaji Pelanggan berdasarkan Status Churn',
                                labels={'Exited': 'Status Churn (0: Tidak, 1: Churn)'})
st.plotly_chart(fig_salary_churn)

# Korelasi antar Fitur Numerik
st.subheader('Korelasi antar Fitur Numerik')
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = df[numeric_cols].corr()
fig_corr = px.imshow(correlation_matrix, text_auto=True, aspect="auto",
                     title='Heatmap Korelasi Fitur Numerik')
st.plotly_chart(fig_corr)

# Scatter plot: Usia vs Estimasi Gaji, diwarnai berdasarkan Churn
st.subheader('Hubungan Usia dan Estimasi Gaji berdasarkan Churn')
fig_scatter = px.scatter(df, x='Age', y='EstimatedSalary', color='Exited',
                         title='Hubungan Usia dan Estimasi Gaji berdasarkan Status Churn',
                         labels={'Exited': 'Status Churn (0: Tidak, 1: Churn)'})
st.plotly_chart(fig_scatter)

# Anda bisa menambahkan visualisasi lain di sini sesuai kebutuhan
# Contoh: Bar chart jumlah kartu kredit berdasarkan churn
st.subheader('Jumlah Kartu Kredit berdasarkan Churn')
fig_card_churn = px.histogram(df, x='HasCrCard', color='Exited',
                              title='Jumlah Kartu Kredit berdasarkan Status Churn',
                              labels={'HasCrCard': 'Memiliki Kartu Kredit (0: Tidak, 1: Ya)',
                                      'Exited': 'Status Churn (0: Tidak, 1: Churn)'})
st.plotly_chart(fig_card_churn)

st.header('Ringkasan Statistik')
st.write(df.describe())
