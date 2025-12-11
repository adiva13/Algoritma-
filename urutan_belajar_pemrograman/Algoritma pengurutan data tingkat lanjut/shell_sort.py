# =========================
# Kelas Shell Sort
# =========================
class ShellSort:
    def __init__(self, data):
        self.data = data  # Simpan data yang akan diurutkan

    def sort(self):
        n = len(self.data)
        gap = n // 2  # Tentukan jarak awal (gap)
        while gap > 0:
            # Lakukan insertion sort untuk setiap elemen yang berjarak gap
            for i in range(gap, n):
                temp = self.data[i]  # Simpan nilai sementara
                j = i
                while j >= gap and self.data[j - gap] > temp:
                    self.data[j] = self.data[j - gap]  # Geser elemen
                    j -= gap
                self.data[j] = temp  # Tempatkan nilai sementara di posisi yang tepat
            gap //= 2  # Kurangi gap
        return self.data  # Kembalikan data yang sudah terurut

