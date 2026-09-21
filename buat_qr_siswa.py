import qrcode
from qrcode.image.pil import PilImage
import os
from typing import List, Dict

# Konfigurasi
BASE_URL = "https://gasmi.id/cari-murid.html"
OUTPUT_FOLDER = "qr-codes"

# Data siswa (sesuai format)
SISWA_DATA: List[Dict[str, str]] = [
    {
        "nomor_induk": "03352-19-09",
        "nama": "DEWI NOVITAYENI",
        "ttl": "Trenggalek, 23 Agustus 2005",
        "jenis_kelamin": "Perempuan",
        "sekolah": "SMK FATHUL MUNA",
        "orangtua": "Mesnan / Dati",
        "alamat": "Botoputih, Bendungan, Trenggalek"
    },
    {
        "nomor_induk": "03353-19-09",
        "nama": "AFNAN GHOZI MAYRIA ASEGAF",
        "ttl": "Ponorogo, 20 Mei 2008",
        "jenis_kelamin": "Laki-Laki",
        "sekolah": "MTS.AL-JAWARIYAH",
        "orangtua": "Agus Riyadi / Siti Maysaroh",
        "alamat": "Grogol, Sawoo Ponorogo"
    },
    # Tambahkan data siswa lainnya di sini dengan format yang sama
]

def generate_qr_code(student: Dict[str, str]) -> str:
    """Buat QR Code untuk satu siswa & simpan sebagai PNG"""
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # URL yang akan tertanam di QR -> sesuai sistem pencarian Gasmi
    qr_url = f"{BASE_URL}?nomor_induk={student['nomor_induk']}"
    
    # Konfigurasi tampilan QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_url)
    qr.make(fit=True)
    
    img = qr.make_image(
        image_factory=PilImage,
        fill_color="black",
        back_color="white"
    ).resize((300, 300))
    
    # Simpan file
    filename = f"{OUTPUT_FOLDER}/{student['nomor_induk']}.png"
    img.save(filename)
    print(f"✅ Dibuat: {filename} → {qr_url}")
    return filename

def generate_all() -> None:
    """Buat QR untuk semua siswa"""
    print(f"Memproses {len(SISWA_DATA)} QR Code...")
    for siswa in SISWA_DATA:
        generate_qr_code(siswa)
    print("Selesai! Semua QR tersimpan di folder:", OUTPUT_FOLDER)

if __name__ == "__main__":
    generate_all()

