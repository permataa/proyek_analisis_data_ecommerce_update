import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from datetime import datetime
from io import BytesIO

# Fungsi untuk memuat data
@st.cache_data
def load_data():
    # Dapatkan direktori saat ini berdasarkan lokasi script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "all_data.csv")
    # # Pastikan path file terlihat
    # st.write(f"File Path: {file_path}")
    return pd.read_csv(file_path)

# Muat data
data = load_data()

# Sidebar
st.sidebar.title("E-Commerce Dashboard")
selected_analysis = st.sidebar.selectbox(
    "Pilih Analisis", 
    ["Produk Terlaris", "Metode Pembayaran vs Nilai Pesanan", "Lokasi Pelanggan vs Waktu Pengiriman", "RFM Analysis"]
)

# Filter tanggal
st.sidebar.subheader("Filter Tanggal")
start_date = st.sidebar.date_input("Tanggal Mulai", value=datetime(2017, 1, 1))
end_date = st.sidebar.date_input("Tanggal Akhir", value=datetime(2018, 12, 31))

# Filter data berdasarkan tanggal
data['order_purchase_timestamp'] = pd.to_datetime(data['order_purchase_timestamp'])
filtered_data = data[(data['order_purchase_timestamp'] >= pd.to_datetime(start_date)) &
                     (data['order_purchase_timestamp'] <= pd.to_datetime(end_date))]

# Pilihan tema warna
st.sidebar.subheader("Pilih Tema Warna")
palette_choice = st.sidebar.selectbox("Tema Warna", ["viridis", "coolwarm", "Blues_d", "magma"])

# Tombol unduh data
def convert_df_to_csv(df):
    output = BytesIO()
    df.to_csv(output, index=False)
    processed_data = output.getvalue()
    return processed_data

if st.sidebar.button("Unduh Data yang Difilter"):
    csv_data = convert_df_to_csv(filtered_data)
    st.sidebar.download_button("Klik untuk Unduh", data=csv_data, file_name="filtered_data.csv", mime="text/csv")

# Judul Dashboard
st.markdown("""
    <h1 style='text-align: center; color: #4CAF50;'>E-Commerce Data Analysis Dashboard</h1>
    <p style='text-align: center;'>Analisis Data E-Commerce untuk Menggali Insights</p>
    """, unsafe_allow_html=True)

# Analisis Produk Terlaris
if selected_analysis == "Produk Terlaris":
    st.subheader("Produk apa yang memiliki jumlah penjualan tertinggi dalam periode yang tersedia di data penjualan?")
    top_products = filtered_data.groupby('product_category_name')['order_item_id'].count().sort_values(ascending=False).head(10)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_products.values, y=top_products.index, palette=palette_choice)
    plt.title('Top 10 Produk Terlaris', fontsize=14, fontweight='bold')
    plt.xlabel('Jumlah Terjual', fontsize=12)
    plt.ylabel('Kategori Produk', fontsize=12)
    for index, value in enumerate(top_products.values):
        plt.text(value + 5, index, str(value), va='center')
    st.pyplot(plt)

# Analisis Metode Pembayaran vs Nilai Pesanan
elif selected_analysis == "Metode Pembayaran vs Nilai Pesanan":
    st.subheader("Apakah terdapat perbedaan rata-rata nilai pesanan berdasarkan metode pembayaran (misalnya kartu kredit, transfer bank, atau e-wallet) di data yang tersedia?")
    avg_payment = filtered_data.groupby('payment_type')['price'].mean().sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=avg_payment.index, y=avg_payment.values, palette=palette_choice)
    plt.title('Rata-rata Nilai Pesanan per Metode Pembayaran', fontsize=14, fontweight='bold')
    plt.xlabel('Metode Pembayaran', fontsize=12)
    plt.ylabel('Rata-rata Nilai Pesanan (BRL)', fontsize=12)
    for index, value in enumerate(avg_payment.values):
        plt.text(index, value + 1, f'{value:.2f}', ha='center')
    st.pyplot(plt)

# Analisis Lokasi Pelanggan vs Waktu Pengiriman
elif selected_analysis == "Lokasi Pelanggan vs Waktu Pengiriman":
    st.subheader("Bagaimana pengaruh lokasi pelanggan (misalnya kota atau provinsi) terhadap rata-rata waktu pengiriman berdasarkan data yang tersedia?")
    filtered_data['shipping_time'] = pd.to_datetime(filtered_data['order_delivered_customer_date']) - pd.to_datetime(filtered_data['order_purchase_timestamp'])
    avg_shipping_time = filtered_data.groupby('customer_state')['shipping_time'].mean().dt.days

    plt.figure(figsize=(12, 8))
    sns.barplot(x=avg_shipping_time.index, y=avg_shipping_time.values, palette=palette_choice)
    plt.title('Rata-rata Waktu Pengiriman per Lokasi Pelanggan', fontsize=14, fontweight='bold')
    plt.xlabel('Lokasi Pelanggan', fontsize=12)
    plt.ylabel('Rata-rata Waktu Pengiriman (Hari)', fontsize=12)
    for index, value in enumerate(avg_shipping_time.values):
        plt.text(index, value + 0.5, f'{value:.1f}', ha='center')
    plt.xticks(rotation=45)
    st.pyplot(plt)

# Analisis RFM
elif selected_analysis == "RFM Analysis":
    st.subheader("Distribusi RFM Score")
    
    # Hitung RFM
    latest_date = filtered_data['order_purchase_timestamp'].max()
    
    rfm = filtered_data.groupby('customer_id').agg({
        'order_purchase_timestamp': lambda x: (latest_date - x.max()).days,
        'order_id': 'count',
        'payment_value': 'sum'
    })
    
    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    
    # Skor Recency
    rfm['R_Score'] = pd.qcut(rfm['Recency'], 4, labels=[4, 3, 2, 1])
    
    # Skor Frequency
    if rfm['Frequency'].nunique() > 1:
        try:
            rfm['F_Score'] = pd.qcut(rfm['Frequency'], 4, labels=[1, 2, 3, 4], duplicates='drop')
        except ValueError:
            rfm['F_Score'] = pd.cut(rfm['Frequency'], bins=4, labels=[1, 2, 3, 4])
    else:
        rfm['F_Score'] = 1
    
    # Skor Monetary
    if rfm['Monetary'].nunique() > 1:
        try:
            rfm['M_Score'] = pd.qcut(rfm['Monetary'], 4, labels=[1, 2, 3, 4], duplicates='drop')
        except ValueError:
            rfm['M_Score'] = pd.cut(rfm['Monetary'], bins=4, labels=[1, 2, 3, 4])
    else:
        rfm['M_Score'] = 1
    
    # Hitung total RFM Score
    rfm['RFM_Score'] = rfm[['R_Score', 'F_Score', 'M_Score']].sum(axis=1)
    
    # Visualisasi
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(rfm['RFM_Score'], bins=10, kde=True, color=sns.color_palette(palette_choice, 1)[0], ax=ax)
    ax.set_title("Distribusi RFM Score")
    ax.set_xlabel("RFM Score")
    ax.set_ylabel("Jumlah Pelanggan")
    st.pyplot(fig)
