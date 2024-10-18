Tugas akhir untuk sertifikasi Dicoding
=======
# Bike Sharing Data Analysis Dashboard
Dataset
Dataset yang digunakan dalam proyek ini berasal dari dataset penyewaan sepeda yang berisi data harian dan per jam. Berikut penjelasan singkat dari setiap file dataset:

**day.csv**: Data penyewaan sepeda harian.

**hour.csv**: Data penyewaan sepeda per jam.

## Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dataset penyewaan sepeda harian dan per jam, dengan fokus pada pola penggunaan sepeda dan pengaruh cuaca. Analisis dilakukan menggunakan Jupyter Notebook, sedangkan hasil akhirnya divisualisasikan dalam bentuk dashboard interaktif menggunakan Streamlit.

## Struktur Proyek
Berikut adalah struktur proyek ini:

submission/

├───dashboard

│ └───app.py

├───data

│ ├───day.csv

│ └───hour.csv

├───notebook.ipynb

├───Readme.md

└───requirements.txt

└───url.txt


- **dashboard/**: Folder yang berisi file Python untuk menjalankan aplikasi Streamlit.
- **data/**: Folder yang berisi dataset yang digunakan dalam analisis.
- **notebook.ipynb**: Jupyter Notebook yang berisi proses analisis data.
- **Readme.md**: Berkas ini, berisi panduan penggunaan proyek.
- **requirements.txt**: Berisi daftar library yang diperlukan untuk menjalankan proyek.
- **url.txt**: Berkas berisi tautan ke dashboard Streamlit.

## Cara Menjalankan Dashboard
1. **Clone repository** atau unduh folder proyek ini.
2. Install library yang diperlukan dengan menjalankan perintah:
   pip install -r requirements.txt
3. Jalankan aplikasi Streamlit dengan perintah berikut di terminal:
	streamlit run dashboard/app.py
4. Buka browser dan arahkan ke alamat yang ditampilkan untuk melihat dashboard.
>>>>>>> cfefe39 (Initial commit)
