#Linear search
# Daftar nama mahasiswa (tidak terurut)
mahasiswa = ["Dipa", "Firda", "Cimmi", "Nayla", "Uci"]

def linear_search(arr, target):
    for i in range(len(arr)):          # cek setiap elemen satu per satu
        if arr[i] == target:           # jika nama ditemukan
            return i                   # kembalikan posisi/indexnya
    return -1                          # jika tidak ditemukan

# Contoh penggunaan
print(linear_search(mahasiswa, "Cimmi"))   # output: 2

#Binary search
# Daftar judul buku yang SUDAH terurut
buku = ["Algoritma", "Basis Data", "Jaringan", "Kalkulus", "Pemrograman"]

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2     # mencari indeks tengah
        
        if arr[mid] == target:        # jika judul buku yang dicari ada di tengah
            return mid

        elif target < arr[mid]:       # jika target lebih kecil (alfabet), cari di kiri
            right = mid - 1

        else:                         # jika lebih besar, cari di kanan
            left = mid + 1

    return -1                         # jika tidak ditemukan

# Contoh penggunaan
print(binary_search(buku, "Jaringan"))   # output: 2
