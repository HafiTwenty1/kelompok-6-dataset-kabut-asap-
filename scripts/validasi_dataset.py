
import pandas as pd
import os

# Lokasi dataset
CSV_FILE = "dataset/dataset.csv"
IMAGE_FOLDER = "dataset/images"

# Membaca dataset
df = pd.read_csv(CSV_FILE)

# Kolom wajib
kolom_wajib = [
    "id",
    "nama_file",
    "deskripsi",
    "lokasi",
    "tanggal",
    "kategori",
    "sumber",
    "lisensi"
]

print("=== VALIDASI DATASET KABUT ASAP ===")

# Memeriksa kolom
kolom_kurang = [
    kolom for kolom in kolom_wajib
    if kolom not in df.columns
]

if kolom_kurang:
    print("Kolom belum tersedia:", kolom_kurang)
    raise SystemExit

# Memeriksa jumlah gambar
print("Jumlah data:", len(df))

if len(df) >= 100:
    print("Target minimum tercapai!")
else:
    print("Data belum mencapai 100 gambar.")

# Memeriksa data kosong
print("\n=== DATA KOSONG ===")

for kolom in kolom_wajib:
    kosong = df[kolom].isna().sum()
    print(kolom, ":", kosong)

# Memeriksa kategori
kategori_valid = ["tipis", "sedang", "tebal"]

print("\n=== PEMERIKSAAN KATEGORI ===")

for index, baris in df.iterrows():
    if str(baris["kategori"]).strip().lower() not in kategori_valid:
        print("Kategori tidak valid pada ID:", baris["id"])

# Memeriksa keberadaan gambar
print("\n=== PEMERIKSAAN FILE ===")

for nama in df["nama_file"].dropna():
    path = os.path.join(IMAGE_FOLDER, str(nama))

    if not os.path.isfile(path):
        print("Gambar tidak ditemukan:", nama)

# Memeriksa ID duplikat
print("\nID duplikat:", df["id"].duplicated().sum())

# Memeriksa nama file duplikat
print(
    "Nama file duplikat:",
    df["nama_file"].duplicated().sum()
)

print("\n=== VALIDASI SELESAI ===")
