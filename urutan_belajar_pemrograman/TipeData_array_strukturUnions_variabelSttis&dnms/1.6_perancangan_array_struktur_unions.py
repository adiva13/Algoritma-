# ============================================
#   perancangan array
# ============================================
#Array nilai dirancang untuk menyimpan banyak angka dengan tipe sama (integer). Indeks digunakan untuk mengambil data tertentu.
nilai = [80, 85, 90, 75]

print("Nilai pertama:", nilai[0])
print("Seluruh nilai:", nilai)

# ============================================
#   perancangan struktur
# ============================================

mahasiswa = {
    "nama": "Dina",
    "umur": 18,
    "ipk": 3.75
}

print("Nama:", mahasiswa["nama"])
print("Umur:", mahasiswa["umur"])
print("IPK:", mahasiswa["ipk"])

#truktur mahasiswa menyatukan data nama (string), umur (int), dan IPK (float). Perancangannya bertujuan untuk membuat data terkait menjadi satu paket yang rapi.

# ============================================
#   perancangan unions
# ============================================

union_data = {}

union_data["value"] = 100
print("Isi union (integer):", union_data["value"])

union_data["value"] = "Teks"
print("Isi union (string):", union_data["value"])
