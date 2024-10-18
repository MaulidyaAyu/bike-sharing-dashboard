import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load Data
day_file_path = 'data/day.csv'
hour_file_path = 'data/hour.csv'

day_data = pd.read_csv(day_file_path)
hour_data = pd.read_csv(hour_file_path)

# Title
st.title("Dashboard Penyewaan Sepeda")

# Informasi Proyek
st.subheader("Proyek Analisis Data: Bike Sharing Dataset")
st.write("""
- **Nama:** Maulidya Ayu Ardiena
- **Email:** neenaardiena@gmail.com
- **ID Dicoding:** ardiena
""")

st.write("Original file is located at: [Colab Project Link](https://colab.research.google.com/drive/1Svbr1Ydz9_VafSvbuk1nkUfb5ZecV7fv)")

#Tentang Dataset
st.subheader("Dataset")
st.write("""
Dataset yang digunakan dalam proyek ini berasal dari dataset penyewaan sepeda yang berisi data harian dan per jam. Berikut penjelasan singkat dari setiap file dataset:
- **day.csv**: Data penyewaan sepeda harian.
- **hour.csv**: Data penyewaan sepeda per jam.
""")

# Menentukan Pertanyaan Bisnis
st.subheader("Pertanyaan Bisnis")
st.write("""
- Bagaimana pengaruh cuaca terhadap jumlah penyewaan sepeda?
- Apa pola penggunaan sepeda berdasarkan waktu (jam dan hari)?
""")

st.header("Data Wrangling")
st.subheader("Gathering Data")

# Display Day Data
st.write("Day Data")
st.write(day_data.head())

# Display Hour Data
st.write("Hour Data")
st.write(hour_data.head())

# Insights
st.write("Insight")
st.write("""
- Suhu dan Penyewaan: Semakin tinggi suhu, semakin banyak orang yang menyewa sepeda, terutama saat cuaca cerah.
- Waktu Puncak: Penyewaan sepeda paling tinggi terjadi pada pagi (jam 7-9) dan sore (jam 5-7).
""")

# Data Assessment
st.subheader("Assessment Data")

# Tampilkan informasi dan ringkasan statistik untuk day_data
st.write("Day Data Info:")
st.write("Jumlah baris:", day_data.shape[0])
st.write("Jumlah kolom:", day_data.shape[1])
st.write(day_data.describe())  # Menampilkan ringkasan statistik
st.write(day_data.dtypes)       # Menampilkan tipe data setiap kolom

# Tampilkan informasi dan ringkasan statistik untuk hour_data
st.write("Hour Data Info:")
st.write("Jumlah baris:", hour_data.shape[0])
st.write("Jumlah kolom:", hour_data.shape[1])
st.write(hour_data.describe())  # Menampilkan ringkasan statistik
st.write(hour_data.dtypes)       # Menampilkan tipe data setiap kolom

# Insights
st.write("Insight")
st.write("""
- Tidak ada data yang hilang di kedua dataset. Ini memudahkan analisis karena semua informasi tersedia.
- Rata-rata penyewaan sepeda per jam adalah 189, dengan puncak hingga 977 sepeda pada jam tertentu.
""")


# Cleaning Data
st.subheader("Cleaning Data")

# Check duplicates
duplicates_day = day_data.duplicated().sum()
duplicates_hour = hour_data.duplicated().sum()

# Remove duplicates
day_data = day_data.drop_duplicates()
hour_data = hour_data.drop_duplicates()

# Convert date columns
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])

st.write(f"Duplikat pada day_data: {duplicates_day}")
st.write(f"Duplikat pada hour_data: {duplicates_hour}")

# Insights
st.write("Insight")
st.write("""
- Setelah pembersihan, kedua dataset tidak memiliki duplikat, sehingga data siap untuk analisis lebih lanjut.
- Kolom tanggal telah dikonversi menjadi format datetime, yang memudahkan analisis berbasis waktu.
""")

# Exploratory Data Analysis
st.header("Exploratory Data Analysis (EDA)")
st.subheader("Eksplore:")

# Day Data Analysis
season_counts_day = day_data.groupby('season')['cnt'].mean()
weather_counts_day = day_data.groupby('weathersit')['cnt'].mean()
workingday_counts_day = day_data.groupby('workingday')['cnt'].mean()
month_counts_day = day_data.groupby('mnth')['cnt'].mean()

# Hour Data Analysis
hour_counts_hour = hour_data.groupby('hr')['cnt'].mean()
weather_counts_hour = hour_data.groupby('weathersit')['cnt'].mean()
workingday_counts_hour = hour_data.groupby('workingday')['cnt'].mean()
temp_counts_hour = hour_data.groupby('temp')['cnt'].mean()

# Display EDA Results
st.write("Rata-rata penyewaan berdasarkan musim:")
st.write(season_counts_day)

st.write("Rata-rata penyewaan berdasarkan cuaca:")
st.write(weather_counts_day)

st.write("Rata-rata penyewaan berdasarkan hari kerja:")
st.write(workingday_counts_day)

st.write("Rata-rata penyewaan berdasarkan bulan:")
st.write(month_counts_day)

st.write("Rata-rata penyewaan berdasarkan jam:")
st.write(hour_counts_hour)

st.write("Rata-rata penyewaan berdasarkan suhu:")
st.write(temp_counts_hour)

st.write("""
Insight:

- Penyewaan sepeda tertinggi terjadi pada musim semi dan musim panas, menunjukkan bahwa orang lebih suka bersepeda saat cuaca lebih hangat.
- Cuaca cerah menghasilkan penyewaan yang jauh lebih tinggi dibandingkan cuaca buruk, mencerminkan pengaruh kondisi cuaca terhadap preferensi pengguna.
- Penyewaan sepeda paling tinggi terjadi pada jam-jam sibuk, seperti pagi dan sore hari, menunjukkan pola penggunaan yang berkaitan dengan kebutuhan transportasi.
- Rata-rata penyewaan meningkat seiring meningkatnya suhu, mengindikasikan bahwa orang lebih cenderung bersepeda saat cuaca hangat.
- Rata-rata penyewaan di hari kerja lebih tinggi dibandingkan hari libur, mencerminkan kebutuhan transportasi untuk bekerja atau aktivitas harian.
""")


st.header("Visualization & Explanatory Analysis")
# Visualization: Pertanyaan 1
st.subheader("Pertanyaan 1: Pengaruh Cuaca Terhadap Penyewaan Sepeda")
fig1, ax1 = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=day_data, ci=None, ax=ax1)
ax1.set_title('Pengaruh Cuaca Terhadap Jumlah Penyewaan Sepeda (Day Data)')
ax1.set_xlabel('Cuaca (0: Clear, 1: Mist + Cloudy, 2: Light Snow/Rain, 3: Heavy Rain/Snow)')
ax1.set_ylabel('Rata-rata Jumlah Penyewaan')
ax1.set_xticklabels(['Clear', 'Mist + Cloudy', 'Light Snow/Rain', 'Heavy Rain/Snow'])
st.pyplot(fig1)

# Visualization: Pertanyaan 2
st.subheader("Pertanyaan 2: Pola Penggunaan Sepeda Berdasarkan Jam")
fig2, ax2 = plt.subplots()
sns.lineplot(x='hr', y='cnt', data=hour_data, ci=None, ax=ax2)
ax2.set_title('Pola Penggunaan Sepeda Berdasarkan Jam (Hour Data)')
ax2.set_xlabel('Jam')
ax2.set_ylabel('Rata-rata Jumlah Penyewaan')
ax2.set_xticks(range(0, 24))
ax2.grid(True)
st.pyplot(fig2)

# Additional Visualization
st.subheader("Pola Penggunaan Sepeda Berdasarkan Hari Kerja")
fig3, ax3 = plt.subplots()
sns.barplot(x='workingday', y='cnt', data=day_data, ci=None, ax=ax3)
ax3.set_title('Pola Penggunaan Sepeda Berdasarkan Hari Kerja (Day Data)')
ax3.set_xlabel('Hari Kerja (0: Tidak, 1: Ya)')
ax3.set_ylabel('Rata-rata Jumlah Penyewaan')
ax3.set_xticklabels(['Tidak', 'Ya'])
st.pyplot(fig3)

st.write("""
Insight:

- Pengaruh Cuaca: Cuaca cerah meningkatkan jumlah penyewaan sepeda, sedangkan cuaca buruk (hujan atau salju) mengurangi penyewaan.
- Pola Waktu Penggunaan: Penyewaan sepeda lebih tinggi pada jam sibuk (pagi dan sore) dan lebih banyak terjadi pada hari kerja dibandingkan hari libur.
""")

# Menghitung Recency (dari hari terakhir dalam dataset)
most_recent_day = day_data['dteday'].max()
day_data['Recency'] = (most_recent_day - day_data['dteday']).dt.days
recency_mean = day_data['Recency'].mean()

# Menghitung Frequency (jumlah penyewaan dalam seluruh dataset)
frequency = day_data['cnt'].count()

# Menghitung Monetary (total jumlah penyewaan)
monetary = day_data['cnt'].sum()

# Membuat DataFrame untuk RFM Analysis
rfm_data = pd.DataFrame({
    'Recency (Avg)': [recency_mean],  # Rata-rata recency
    'Frequency (Total)': [frequency],  # Total frequency
    'Monetary (Total)': [monetary]  # Total monetary
})

# Tampilkan RFM Analysis
st.header("Hasil RFM Analysis")
st.dataframe(rfm_data)
st.write("""
RFM Analysis membantu kita memahami perilaku pengguna berdasarkan:

- Kapan terakhir mereka menyewa (Recency),
- Seberapa sering mereka menyewa (Frequency), dan
- Berapa banyak uang yang dihasilkan (Monetary)
""")

# Conclusions
st.header("Kesimpulan")
st.write("""
**Pertanyaan 1:** Cuaca sangat memengaruhi jumlah penyewaan sepeda. Saat cuaca cerah dan hangat, orang lebih banyak menyewa sepeda. Sebaliknya, saat hujan atau cuaca buruk, jumlah penyewaan menurun. Ini berarti penting bagi pengelola untuk memperhatikan cuaca dalam rencana pemasaran mereka. Misalnya, mereka bisa memberikan promo saat cuaca baik atau menyiapkan alternatif ketika cuaca buruk.

**Pertanyaan 2:** Pola penggunaan sepeda menunjukkan bahwa banyak orang menyewa sepeda pada jam sibuk, seperti pagi dan sore hari. Ini menunjukkan bahwa mereka menggunakan sepeda untuk pergi ke tempat kerja atau sekolah. Selain itu, lebih banyak sepeda disewa di akhir pekan untuk bersenang-senang. Pengelola dapat meningkatkan layanan dan fasilitas pada waktu-waktu ini untuk menarik lebih banyak pengguna.
""")