#dictionary dengan detail sendal
sendal = {
    "Sandal Gunung": {"Merk": "Eiger", "Harga": 250000, "Ukuran": 42},
    "Sandal Jepit": {"Merk": "Nike", "Harga": 150000, "Ukuran": 40},
    "Sandal Kulit": {"Merk": "Geox", "Harga": 400000, "Ukuran": 41},
    "Sandal Sport": {"Merk": "Adidas", "Harga": 350000, "Ukuran": 43}
}

#menampilkan semua informasi
print("Informasi lengkap sendal:")
for jenis, info in sendal.items():
    print(f"{jenis}: Merk={info['Merk']}, Harga={info['Harga']}, Ukuran={info['Ukuran']}")
