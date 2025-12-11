# =========================
# Kelas Quick Sort
# =========================
class QuickSort:
    def __init__(self, data):
        self.data = data  # Simpan data yang akan diurutkan

    def sort(self):
        self._quick_sort(0, len(self.data) - 1)  # Jalankan quick sort rekursif
        return self.data

    def _quick_sort(self, low, high):
        if low < high:
            pi = self._partition(low, high)  # Partisi array
            self._quick_sort(low, pi - 1)    # Urutkan subarray kiri
            self._quick_sort(pi + 1, high)   # Urutkan subarray kanan

    def _partition(self, low, high):
        pivot = self.data[high]  # Pilih pivot terakhir
        i = low - 1
        for j in range(low, high):
            if self.data[j] <= pivot:
                i += 1
                self.data[i], self.data[j] = self.data[j], self.data[i]  # Tukar elemen
        self.data[i + 1], self.data[high] = self.data[high], self.data[i + 1]  # Tempatkan pivot
        return i + 1  # Kembalikan indeks pivot