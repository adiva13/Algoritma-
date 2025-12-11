#bubble sorting
#daftar merk jam
merk_jam = ["Casio", "Seiko", "Rolex", "Swatch", "G-Shock", "Fossil"]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:   # jika urutannya salah
                arr[j], arr[j+1] = arr[j+1], arr[j]  # tukar elemen

# === PROGRAM UTAMA ===
print("Sebelum Bubble Sort:", merk_jam)
bubble_sort(merk_jam)
print("Setelah Bubble Sort:", merk_jam)


#selection sorting
#daftar merk jam
merk_jam = ["Casio", "Seiko", "Rolex", "Swatch", "G-Shock", "Fossil"]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # tukar

# === PROGRAM UTAMA ===
print("Sebelum Selection Sort:", merk_jam)
selection_sort(merk_jam)
print("Setelah Selection Sort:", merk_jam)


#insertion sorting
#daftar merk jam
merk_jam = ["Casio", "Seiko", "Rolex", "Swatch", "G-Shock", "Fossil"]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# === PROGRAM UTAMA ===
print("Sebelum Insertion Sort:", merk_jam)
insertion_sort(merk_jam)
print("Setelah Insertion Sort:", merk_jam)