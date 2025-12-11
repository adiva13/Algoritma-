#Insertion Sort bekerja seperti menyusun kartu di tangan.

class InsertionSorter:
    def __init__(self, items):
        self.items = items  # Menyimpan data awal ke dalam objek

    def sort(self):
        arr = self.items.copy()  # Salinan data
        for i in range(1, len(arr)):
            key = arr[i]  # Ambil elemen yang akan disisipkan
            j = i - 1
            # Geser elemen yang lebih besar ke kanan
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key  # Sisipkan elemen pada posisi yang tepat
        return arr

    def display(self):
        print("Insertion Sorted:", self.sort())  # Menampilkan hasil
