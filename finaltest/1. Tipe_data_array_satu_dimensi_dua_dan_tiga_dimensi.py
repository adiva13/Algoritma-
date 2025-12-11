#nama: Siti Adiva Kirani
#nim: D0425302
#kelas: B_Sistem informasi

#tipe data array satu dimensi

tanaman = ["Mawar", "Melati", "Anggrek", "Kaktus", "Lavender"]

print("Daftar tanaman awal:")
print(tanaman)

# Akses elemen
print("Tanaman pertama:", tanaman[0])

# Tambah elemen
tanaman.append("Kenanga")
print("Setelah menambah Kenanga:", tanaman)

# Ubah elemen
tanaman[1] = "Kemuning"
print("Setelah mengubah elemen kedua:", tanaman)

# Hapus elemen
tanaman.remove("Kaktus")
print("Setelah menghapus Kaktus:", tanaman)


#tipe data array dua dimensi
# Array 2 Dimensi berisi brand skincare dari berbagai negara
skincare = [
    ["SK-II", "Shiseido", "Hada Labo"],          # Jepang
    ["Innisfree", "Laneige", "Etude House"],     # Korea
    ["The Ordinary", "CeraVe", "Cetaphil"]       # Barat
]

print("=== DAFTAR BRAND SKINCARE ===")
for baris in skincare:
    print(baris)

# Mengakses elemen tertentu
print("\n=== AKSES ELEMEN ===")
print("Brand dari Jepang indeks [0][1]:", skincare[0][1])  # Shiseido
print("Brand dari Korea indeks [1][0]:", skincare[1][0])    # Innisfree
print("Brand dari Barat indeks [2][2]:", skincare[2][2])    # Cetaphil

# Menambah brand baru pada kategori Korea
print("\n=== MENAMBAH BRAND ===")
skincare[1].append("Cosrx")
print("Setelah menambah 'Cosrx' pada kategori Korea:")
print(skincare[1])

# Mengubah brand tertentu
print("\n=== MENGUBAH BRAND ===")
skincare[0][2] = "SK-II Treatment"
print("Mengubah Hada Labo menjadi SK-II Treatment pada kategori Jepang:")
print(skincare[0])

# Menghapus brand tertentu
print("\n=== MENGHAPUS BRAND ===")
skincare[2].remove("CeraVe")
print("Menghapus 'CeraVe' dari kategori Barat:")
print(skincare[2])

# Menampilkan semua brand setelah perubahan
print("\n=== DATA TERBARU ===")
for baris in skincare:
    print(baris)


#tipe data array tiga dimensi
nama = [
    [   # Kelompok 1
        ["Nayla", "Firda"],        # Subkelompok 1
        ["Cimmi", "Lulu"]          # Subkelompok 2
    ],
    [   # Kelompok 2
        ["Ucay", "Dean"],          # Subkelompok 1
        ["Diki", "Diva"]           # Subkelompok 2
    ]
]

print("=== DATA AWAL ARRAY 3 DIMENSI ===")
for kelompok in nama:
    print(kelompok)

# Mengakses elemen tertentu
print("\n=== AKSES ELEMEN ===")
print("nama[0][0][1] =", nama[0][0][1])  # Firda
print("nama[1][1][0] =", nama[1][1][0])  # Diki
print("nama[1][0][1] =", nama[1][0][1])  # Dean

# Mengubah elemen
print("\n=== MENGUBAH ELEMEN ===")
nama[0][1][0] = "Cimmi cantik"
print("Mengubah 'Cimmi' menjadi 'Cimmi cantik':")
print(nama[0][1])

# Menampilkan semua elemen setelah perubahan
print("\n=== DATA TERBARU ===")
for kelompok in nama:
    for sub in kelompok:
        for orang in sub:
            print(orang)

