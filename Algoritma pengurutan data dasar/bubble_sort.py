#Bubble sort bekerja dengan membandingkan dua elemen yang berdekatan dan menukarnya jika urutannya salah.

class BubbleSorter:
    def __init__(self, items):
        self.items = items  # Menyimpan data awal ke dalam objek

    def sort(self):
        arr = self.items.copy()  # Membuat salinan agar data asli tidak berubah
        n = len(arr)  # Panjang list
        for i in range(n):
            # Loop untuk setiap elemen
            for j in range(n - i - 1):
                # Bandingkan elemen berdekatan
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Tukar jika salah urut
        return arr  # Kembalikan list yang sudah diurutkan

    def display(self):
        print("Bubble Sorted:", self.sort())  # Menampilkan hasil
