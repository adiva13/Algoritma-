#Selection Sort bekerja dengan cara mencari elemen terkecil (atau terbesar) dari sisa daftar yang belum terurut, kemudian menukarnya dengan posisi paling depan dari bagian yang belum terurut.

class SelectionSorter:
    def __init__(self, items):
        self.items = items  # Menyimpan data awal ke dalam objek

    def sort(self):
        arr = self.items.copy()  # Salinan data agar asli tetap aman
        n = len(arr)
        for i in range(n):
            min_idx = i  # Anggap elemen pertama sebagai terkecil
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:  # Cari elemen terkecil
                    min_idx = j  # Update indeks terkecil
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Tukar posisi terkecil dengan posisi i
        return arr

    def display(self):
        print("Selection Sorted:", self.sort())  # Menampilkan hasil
