# Stack untuk menyimpan riwayat halaman web
browser_history = []

# Fungsi membuka halaman baru
def open_page(page):
    browser_history.append(page)   # menambahkan halaman ke bagian atas stack
    print(f"Membuka: {page}")

# Fungsi kembali ke halaman sebelumnya
def go_back():
    if len(browser_history) == 0:   # jika tidak ada riwayat
        return "Tidak ada halaman sebelumnya!"
    return browser_history.pop()    # menghapus halaman terakhir yang dikunjungi

# Fungsi melihat halaman yang sedang dibuka
def current_page():
    if len(browser_history) == 0:   # jika stack kosong
        return "Tidak ada halaman!"
    return browser_history[-1]      # halaman paling atas adalah yang sedang dibuka

# --- Contoh penggunaan ---
open_page("Google")        # membuka Google
open_page("Wikipedia")     # membuka Wikipedia
open_page("YouTube")       # membuka YouTube

print("Kembali dari:", go_back())   # keluar dari YouTube
print("Halaman saat ini:", current_page())  # sekarang di Wikipedia
