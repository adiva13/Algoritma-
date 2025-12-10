#Union adalah tipe data khusus yang bisa menyimpan berbagai jenis data, tetapi hanya satu yang aktif pada satu waktu. Artinya, union menggunakan satu tempat memori untuk beberapa tipe data, sehingga lebih hemat memori dibandingkan struktur.

union_data = {}

# menyimpan nilai integer
union_data["value"] = 10
print("Isi union (integer):", union_data["value"])

# menimpa dengan nilai string
union_data["value"] = "Halo"
print("Isi union (string):", union_data["value"])
