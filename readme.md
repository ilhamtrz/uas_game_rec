# **Sistem Rekomendasi Video Game menggunakan Algoritma TF-IDF dan Cosine Similarity**

# Sistem Temu Kembali Informasi

# Ilham Triza Kurniawan (A11.2022.14193)

---

## Dataset

Dataset diambil dari kaggle → [![Kaggle Badge](https://img.shields.io/badge/Kaggle-blue?style=flat&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/nikatomashvili/steam-games-dataset/data)
Pada dataset terdapat 16 Kolom:

- Title
- Original Price
- Discounted Price
- Release Date
- Link
- Game Description
- Recent Reviews Summary
- All Reviews Summary
- Recent Reviews Number
- All Reviews Number
- Developer
- Publisher
- Supported Languages
- Popular Tags
- Game Features
- Minimum Requirements

Dari Semua 16 kolom tersebut tidak semua kolom diperlukan untuk membuat sistem Rekomendasi ini. Beberapa kolom yang diperlukan diantaranya adalah kolom Title, Game Description, dan All Reviews Number

## Tujuan

Sistem rekomendasi berdasarkan deskripsi game dapat menjadi solusi yang berguna bagi pengguna yang ingin menemukan game baru yang sesuai dengan selera mereka. Dengan menggunakan dataset yang telah disebutkan, penulis dapat mengembangkangkan sebuah sistem rekomendasi dengan pendekatan content-based.

## Metode dan Tahapan

- Preprocessing :
  - Kolom All Number Reviews dilakukan ekstraksi nilai angka, karena menunjukkan jumlah review pada tiap judul game hasilnya akan diletakkan pada kolom "Number of Reviews"
  - Drop kolom yang tidak dibutuhkan
  - Sorting secara descending berdasarkan kolom "Number of Reviews"
  - Drop baris yang memiliki jumlah review 0
  - Normalisasi pada kolom "Game Description" (menyeragamkan menjadi lower, tokenisasi)
- Method :
  - SKLearn digunakan untuk melakukan vektorisasi TF-IDF
  - SKLearn digunakan untuk menghitung similaritas berdasarkan matrix TF-IDF dari vektorisasi
  - Outputnya adalah 5 judul game yang memiliki deskripsi yang serupa dari input judul game yang dimasukkan pengguna

## Performa Uji

Performa Uji dilakukan menggunakan K-Fold Cross-Validation yang sebelumnya penulis perlu membuat beberapa sampel rekomendasi pada judul game tertentu untuk mendapatkan hasil dari pengujian ini.
Setelah dilakukan pengujian hasil Average Hit Ratio yang didapat: 0.224

## Deployment

- Sistem Rekomendasi Video Game dapat dicoba di → [![Streamlit Badge](https://img.shields.io/badge/Streamlit-red?style=flat&logo=streamlit&logoColor=white)](https://ilhamtriza-game-rec.streamlit.app/)
