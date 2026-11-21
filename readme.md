
# Kelompok 6 - Dataset Multimodal Teks dan Citra Kabut Asap

## Identitas Kelompok

- Kode Kelompok: 06
- Nama Kelompok: Kelompok 6
- Topik: Dataset Multimodal Teks dan Citra Kabut Asap

### Anggota Kelompok

1. Adet
2. Adha
3. Hafi
4. Alza

## Deskripsi Proyek

Proyek ini bertujuan membangun dataset multimodal
yang menggabungkan data citra dan teks mengenai
fenomena kabut asap.

Dataset berisi kumpulan gambar kabut asap yang
dilengkapi dengan deskripsi, lokasi, tanggal,
kategori, sumber gambar, dan informasi lisensi.

Dataset ini dapat digunakan sebagai bahan penelitian
dan pembelajaran dalam bidang pengolahan citra,
analisis teks, dan kecerdasan buatan (AI).

## Target Dataset

- Target minimum: 100 citra.
- Format data: CSV.
- Jenis data: Citra dan teks deskriptif.
- Kategori: Tipis, sedang, dan tebal.

## Struktur Repository

kelompok-6-dataset-kabut-asap/
- README.md
- LICENSE
- .gitignore
- dataset/
  - images/
  - dataset.csv
- scripts/
  - validasi_dataset.py
  - cek_gambar.py
- docs/
  - dokumentasi.md

## Cara Mengunduh Dataset

1. Buka repository GitHub ini.
2. Klik tombol Code.
3. Pilih Download ZIP.
4. Ekstrak file ZIP.
5. Dataset tersedia pada folder dataset.

## Cara Menggunakan Dataset

Install library:

pip install pandas pillow

Baca dataset menggunakan Python:

import pandas as pd

df = pd.read_csv("dataset/dataset.csv")

print(df.head())

## Cara Menjalankan Validasi

python scripts/validasi_dataset.py

## Cara Memeriksa Gambar Rusak

python scripts/cek_gambar.py

## Pembagian Tugas Kelompok

| Nama | Tugas |
|---|---|---|
| Adet | Pengumpulan citra | 
| Adha | Pembuatan deskripsi teks | 
| Hafi | Pembuatan dataset dan kode Python | 
| Alza | Validasi dan dokumentasi | 

## Sumber Dataset

Seluruh sumber gambar dan informasi lisensi
dicantumkan pada dataset.csv.

## Lisensi

Dataset menggunakan lisensi CC BY 4.0
sepanjang seluruh materi di dalamnya
memiliki izin untuk didistribusikan dengan lisensi tersebut.

## Penutup

Dataset ini dibuat sebagai proyek tugas Kelompok 6
dengan tujuan mengembangkan kumpulan data multimodal
teks dan citra mengenai fenomena kabut asap.
