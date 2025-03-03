# E-Commerce Data Analysis Dashboard ✨

Dashboard ini dibuat untuk membantu menganalisis data e-commerce, menggali insight dari data, dan memberikan visualisasi interaktif untuk mendukung pengambilan keputusan bisnis. Selain analisis dasar seperti produk terlaris, metode pembayaran, dan waktu pengiriman, dashboard ini juga menyertakan **Analisis Lanjutan (RFM Analysis)** untuk segmentasi pelanggan.

---

## Fitur

- **Analisis Produk Terlaris**  
  Visualisasi produk-produk dengan penjualan tertinggi berdasarkan data yang tersedia.

- **Filter Berdasarkan Tanggal**  
  Memungkinkan pengguna memfilter data berdasarkan rentang waktu tertentu.

- **Tema Warna Interaktif**  
  Pilihan untuk mengubah tema warna visualisasi sesuai preferensi pengguna.

- **Unduh Data yang Difilter**  
  Data yang telah difilter dapat diunduh dalam format CSV untuk analisis lebih lanjut.

- **Analisis Lanjutan (RFM Analysis)**  
  Mengelompokkan pelanggan berdasarkan:
  - **Recency:** Jarak waktu sejak transaksi terakhir.
  - **Frequency:** Frekuensi pembelian.
  - **Monetary:** Total pengeluaran pelanggan.
  
  **Insight dari RFM Analysis:**  
  - Pelanggan dengan **RFM Score** tinggi merupakan pelanggan yang sangat berharga.
  - Pelanggan dengan skor rendah perlu strategi re-engagement atau promosi khusus.

---

## Setup Environment

### Menggunakan Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
### Menggunakan Shell/Terminal dengan Pipenv
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Cara Menjalankan
1. Clone Repository
Clone repository ini menggunakan perintah berikut:
git clone https://github.com/permataa/proyek_analisis_data_ecommerce_update.git
2. Masuk ke Direktori Repository
Pindah ke direktori project yang telah di-clone:
cd dashboard
3. Install Dependencies
Pastikan sudah menginstall Python (versi 3.8 atau lebih baru) dan pip di sistem. Lalu, install pustaka Python yang diperlukan dengan perintah:
pip install -r requirements.txt
4. Jalankan Aplikasi
Jalankan aplikasi Streamlit menggunakan perintah berikut:
streamlit run dashboard.py
5. Akses Aplikasi
Setelah perintah di nomor 4 dijalankan, aplikasi akan terbuka di browser pada alamat:
http://localhost:8501
Jika dijalankan di server, gunakan IP atau domain server.

## Analisis Lanjutan: RFM Analysis

### Dashboard ini juga menyertakan Analisis RFM untuk mengelompokkan pelanggan berdasarkan:
- **Recency: Jarak waktu sejak transaksi terakhir pelanggan.**
- **Frequency: Frekuensi pembelian pelanggan.**
- **Monetary: Total pengeluaran pelanggan.**

### Insight dari RFM Analysis:
- **Recency: Banyak pelanggan memiliki pembelian terakhir yang lama sehingga perlu strategi re-engagement.**
- **Frequency: Sebagian besar pelanggan hanya berbelanja sekali, namun ada segmen yang sering membeli.**
- **Monetary: Sebagian besar pelanggan menghabiskan jumlah kecil, tetapi terdapat segmen high-value.**
### Strategi Bisnis:
  1. 🎯 Promosi eksklusif bagi pelanggan dengan nilai tinggi.
  2. 🔄 Program loyalitas untuk meningkatkan retensi pelanggan.
  3. 📢 Reaktivasi pelanggan lama dengan diskon atau penawaran menarik.

## Cara Mengakses Versi Online
Aplikasi ini juga tersedia secara online dan dapat diakses melalui link berikut:
https://strmlit-proyek2.streamlit.app/

## Catatan
- **Pastikan file all_data.csv dan file pendukung lainnya sudah ter-push ke repository.**
- **Periksa file .gitignore untuk memastikan file CSV tidak diabaikan.**
- **Jika ada pertanyaan atau saran, silakan buat issue di repository ini.**




