
import os
from PIL import Image

FOLDER = "dataset/images"

jumlah = 0
rusak = []

print("=== PEMERIKSAAN GAMBAR ===")

for nama in os.listdir(FOLDER):

    path = os.path.join(FOLDER, nama)

    if not nama.lower().endswith(
        (".jpg", ".jpeg", ".png", ".webp")
    ):
        continue

    try:
        with Image.open(path) as img:
            img.verify()

        jumlah += 1
        print("OK:", nama)

    except Exception:
        rusak.append(nama)
        print("RUSAK:", nama)

print("\n=== HASIL PEMERIKSAAN ===")
print("Jumlah gambar normal:", jumlah)
print("Jumlah gambar rusak:", len(rusak))

if rusak:
    print("\nDaftar gambar rusak:")
    for nama in rusak:
        print("-", nama)
else:
    print("Semua gambar berhasil diperiksa.")
