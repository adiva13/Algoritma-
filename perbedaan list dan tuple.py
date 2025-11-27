#Nama : Siti Adiva Kirani 
#Nim : D0425302
#Program_studi : Sistem_informasi
#Mata_kuliah : Pemrograman Dasar

#perbedaan antara list dan tuple
#list adalah struktur data yang dapat diubah (mutable) dan menggunakan tanda kurung siku [], sedangkan tuple tidak bisa diubah (immutable) dan menggunakan tanda kurung biasa () 

#contoh list
kelas = [["diva", 85], ["danu", 90], ["caca", 88]]
kelas[0][1] = 95   #masih bisa diubah 
print(kelas)

#contoh tuple
hari = ("senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu")
print(hari)
