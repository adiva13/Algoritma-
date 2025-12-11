#binary search
#Daftar nama bulan (teurut secara alfabet)
bulan = ["April", "Agustus", "Desember", "Februari", "Januari", "Juli", "Juni", "Maret", "Mei", "November", "Oktober", "September"]

#Urutkan terlebih dahulu
bulan.sort()

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid - 1
        else:
            high = mid - 1
    return -1 

# === PROGRAM UTAMA ===
cari_bulan = "Mei"
index = binary_search(bulan, cari_bulan)

if index != -1:
    print(f"Bulan {cari_bulan} ditemukan di indeks {index}")
else:
    print(f"Bulan {cari_bulan} tidak ditemukan")


#interpolation search
#daftar nama negara (terurut secara alfabet)
negara = ["Argentina", "Australia", "Brasil", "Canada", "Denmark", 
          "Filipina", "Indonesia", "Jepang", "Malaysia", "Singapura", "Thailand"]

#fungsi bantu: konversi string ke nilai numerik sederhana
def nilai_ascii(s):
    return sum([ord(c) for c in s])

#interpolation search
def interpolation_search(arr, target):
    arr_values = [nilai_ascii(x) for x in arr]
    target_value = nilai_ascii(target)

    low = 0
    high = len(arr_values) - 1

    while low <= high and target_value >= arr_values[low] and target_value <= arr_values[high]:
        if arr_values[high] == arr_values[low]:
            if arr_values[low] == target_value:
                return low
            else:
                return -1
            
            #hitung posisi estimasi
            pos = low + ((target_value - arr_values[low]) * (high - low)) // (arr_values[high] - arr_values[low])

            if arr_values[pos] == target_value:
                return pos
        elif arr_values[pos] < target_value:
            low = pos + 1
        else:
            high = pos - 1
    return -1

# === PROGRAM UTAMA ===
cari_negara = "Indonesia"
index = interpolation_search(negara, cari_negara)

if index != -1:
    print(f"Negara {cari_negara} ditemukan di indeks {index}")
else:
    print(f"Negara {cari_negara} tidak ditemukan")