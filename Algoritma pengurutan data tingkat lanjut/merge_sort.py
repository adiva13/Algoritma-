# =========================
# Kelas Merge Sort
# =========================
class MergeSort:
    def __init__(self, data):
        self.data = data  # Simpan data yang akan diurutkan

    def sort(self):
        self.data = self._merge_sort(self.data)  # Jalankan merge sort rekursif
        return self.data

    def _merge_sort(self, array):
        if len(array) <= 1:
            return array  # Basis rekursi: array sudah satu elemen
        mid = len(array) // 2  # Tentukan titik tengah
        left = self._merge_sort(array[:mid])   # Urutkan bagian kiri
        right = self._merge_sort(array[mid:])  # Urutkan bagian kanan
        return self._merge(left, right)        # Gabungkan hasilnya

    def _merge(self, left, right):
        result = []
        i = j = 0
        # Gabungkan dua array terurut
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        # Tambahkan sisa elemen jika ada
        result.extend(left[i:])
        result.extend(right[j:])
        return result