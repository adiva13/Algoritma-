import tkinter as tk
from tkinter import messagebox
import time
import threading
import winsound  # Untuk suara di Windows

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("TicTacToe")
        self.root.resizable(False, False)

        self.pemain_sekarang = "x"
        self.papan = [""] * 9
        self.tombol = []

        self.skor_x = 0
        self.skor_o = 0

        self.timer = 10  # detik
        self.timer_label = None
        self.timer_thread = None
        self.timer_running = False

        self.buat_widget()
        self.mulai_timer()

    def buat_widget(self):
        # Pita pink
        pita = tk.Frame(self.root, bg="#ff69b4", height=10)
        pita.grid(row=0, column=0, columnspan=3, sticky="ew")

        label_judul = tk.Label(
            self.root,
            text="TIC-TAC-TOE DIVA",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="#ff69b4",     # 🔥 warna pink
            pady=10
        )
        label_judul.grid(row=1, column=0, columnspan=3, sticky="ew")

        self.label_pemain = tk.Label(
            self.root,
            text=f"Giliran: {self.pemain_sekarang}",
            font=("Arial", 16),
            bg="#34495e",
            fg="white",
            pady=10
        )
        self.label_pemain.grid(row=2, column=0, columnspan=3, sticky="ew")

        self.timer_label = tk.Label(
            self.root,
            text=f"Waktu: {self.timer} detik",
            font=("Arial", 14),
            bg="#34495e",
            fg="white",
            pady=5
        )
        self.timer_label.grid(row=3, column=0, columnspan=3, sticky="ew")

        for i in range(9):
            tmbl = tk.Button(
                self.root,
                text="",
                font=("Arial", 32, "bold"),
                width=5,
                height=2,
                bg="black",
                fg="white",
                activebackground="#555555",
                command=lambda indeks=i: self.lakukan_langkah(indeks)
            )
            baris = (i // 3) + 4
            kolom = i % 3
            tmbl.grid(row=baris, column=kolom, padx=5, pady=5)
            self.tombol.append(tmbl)

        self.label_skor = tk.Label(
            self.root,
            text=f"Skor - x: {self.skor_x} | o: {self.skor_o}",
            font=("Arial", 14),
            bg="#34495e",
            fg="blue",
            pady=10
        )
        self.label_skor.grid(row=7, column=0, columnspan=3, sticky="ew")

        tombol_reset = tk.Button(
            self.root,
            text="Atur Ulang Permainan",
            font=("Arial", 12, "bold"),
            bg="#e74c3c",
            fg="white",
            activebackground="#c0392b",
            command=self.atur_ulang_permainan,
            pady=10
        )
        tombol_reset.grid(row=8, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

        self.root.configure(bg="#34495e")

    def mainkan_suara(self):
        winsound.Beep(1000, 100)  # 1000 Hz selama 100 ms

    def lakukan_langkah(self, indeks):
        self.mainkan_suara()

        if self.papan[indeks] == "" and not self.cek_pemenang():
            self.papan[indeks] = self.pemain_sekarang
            warna = "#e74c3c" if self.pemain_sekarang == "x" else "#ffa500"
            self.tombol[indeks].config(
                text=self.pemain_sekarang,
                fg=warna,
                state="disabled"
            )

            if self.cek_pemenang():
                pemenang = self.pemain_sekarang
                if pemenang == "x":
                    self.skor_x += 1
                else:
                    self.skor_o += 1
                self.perbarui_skor()
                messagebox.showinfo("Permainan Selesai", f"Pemain {pemenang} Menang!")
                self.nonaktifkan_semua_tombol()
                self.timer_running = False

            elif "" not in self.papan:
                messagebox.showinfo("Permainan Selesai", "Seri!")
                self.timer_running = False

            else:
                self.pemain_sekarang = "o" if self.pemain_sekarang == "x" else "x"
                self.label_pemain.config(text=f"Giliran: {self.pemain_sekarang}")
                self.timer = 10

    def cek_pemenang(self):
        menang = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for kombinasi in menang:
            if (
                self.papan[kombinasi[0]] == self.papan[kombinasi[1]] ==
                self.papan[kombinasi[2]] != ""
            ):
                for idx in kombinasi:
                    self.tombol[idx].config(bg="#2ecc71")
                return True

        return False

    def nonaktifkan_semua_tombol(self):
        for tmbl in self.tombol:
            tmbl.config(state="disabled")

    def atur_ulang_permainan(self):
        self.pemain_sekarang = "x"
        self.papan = [""] * 9
        self.label_pemain.config(text=f"Giliran: {self.pemain_sekarang}")

        for tmbl in self.tombol:
            tmbl.config(
                text="",
                state="normal",
                bg="black",
                fg="white"
            )
        self.timer = 10
        self.timer_running = True
        self.mulai_timer()

    def perbarui_skor(self):
        self.label_skor.config(text=f"Skor - x: {self.skor_x} | o: {self.skor_o}")

    def mulai_timer(self):
        self.timer_running = True
        if self.timer_thread is None or not self.timer_thread.is_alive():
            self.timer_thread = threading.Thread(target=self.update_timer)
            self.timer_thread.daemon = True
            self.timer_thread.start()

    def update_timer(self):
        while self.timer_running:
            self.timer_label.config(text=f"Waktu: {self.timer} detik")
            if self.timer <= 0:
                self.pemain_sekarang = "o" if self.pemain_sekarang == "x" else "x"
                self.label_pemain.config(text=f"Giliran: {self.pemain_sekarang}")
                self.timer = 10
            time.sleep(1)
            self.timer -= 1


if __name__ == "__main__":
    root = tk.Tk()
    permainan = TicTacToe(root)
    root.mainloop()
