
import csv
from pathlib import Path
from datetime import date

# Menentukan lokasi folder proyek
BASE_DIR = Path(__file__).resolve().parent.parent
FOLDER_GAMBAR = BASE_DIR / "dataset" / "images"
FILE_CSV = BASE_DIR / "dataset" / "dataset.csv"

# Format gambar yang didukung
FORMAT_GAMBAR = {
    ".jpg", ".jpeg", ".png", ".avif"
}

# Kategori kondisi kabut asap
KATEGORI = ["tipis", "sedang", "tebal"]

# Lisensi dataset
LISENSI = "CC BY 4.0"


def buat_dataset():
    # Memastikan folder tersedia
    FOLDER_GAMBAR.mkdir(parents=True, exist_ok=True)
    FILE_CSV.parent.mkdir(parents=True, exist_ok=True)

    # Mengambil daftar gambar
    daftar_gambar = sorted([
        file for file in FOLDER_GAMBAR.iterdir()
        if file.is_file() and file.suffix.lower() in FORMAT_GAMBAR
    ])

    if not daftar_gambar:
        print("Tidak ada gambar di folder dataset/images!")
        return

    data = []

    print("=== PEMBUAT DATASET KABUT ASAP ===")
    print(f"Jumlah gambar ditemukan: {len(daftar_gambar)}")
    print(f"Lisensi dataset: {LISENSI}")

    for nomor, gambar in enumerate(daftar_gambar, start=1):
        print(f"\nData gambar ke-{nomor}")
        print(f"Nama file: {gambar.name}")

        deskripsi = input("Deskripsi gambar: ").strip()
        lokasi = input("Lokasi gambar: ").strip()

        tanggal = input(
            f"Tanggal pengambilan [{date.today()}]: "
        ).strip()

        if not tanggal:
            tanggal = str(date.today())

        print("Kategori: tipis / sedang / tebal")
        kategori = input("Masukkan kategori: ").strip().lower()

        while kategori not in KATEGORI:
            print("Kategori tidak valid!")
            kategori = input(
                "Masukkan tipis, sedang, atau tebal: "
            ).strip().lower()

        sumber = input(
            "Sumber gambar (URL/nama pembuat): "
        ).strip()

        # Memasukkan data ke daftar
        data.append({
            "id": nomor,
            "nama_file": gambar.name,
            "deskripsi": deskripsi,
            "lokasi": lokasi,
            "tanggal": tanggal,
            "kategori": kategori,
            "sumber": sumber,
            "lisensi": LISENSI
        })

    # Menyimpan data menjadi CSV
    kolom = [
        "id",
        "nama_file",
        "deskripsi",
        "lokasi",
        "tanggal",
        "kategori",
        "sumber",
        "lisensi"
    ]

    with open(
        FILE_CSV,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:
        writer = csv.DictWriter(file, fieldnames=kolom)
        writer.writeheader()
        writer.writerows(data)

    print("\n================================")
    print("DATASET BERHASIL DIBUAT!")
    print(f"Total data: {len(data)}")
    print(f"Lisensi: {LISENSI}")
    print(f"Lokasi file: {FILE_CSV}")
    print("================================")


if __name__ == "__main__":
    buat_dataset()
