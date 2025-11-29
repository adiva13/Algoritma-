import tkinter as tk
from tkinter import messagebox

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

        self.waktu = 10  # timer per giliran
        self.timer_id = None

        self.buat_widget()
        self.mulai_timer()

    def buat_widget(self):
        label_judul = tk.Label(
            self.root,
            text="TIC-TAC-TOE DIVA",
            font=("Arial", 24, "bold"),
            bg="#2c3e50",
            fg="white",
            pady=10
        )
        label_judul.grid(row=0, column=0, columnspan=3, sticky="ew")

        self.label_pemain = tk.Label(
            self.root,
            text=f"Giliran: {self.pemain_sekarang.upper()}",
            font=("Arial", 16),
            bg="#34495e",
            fg="white",
            pady=10
        )
        self.label_pemain.grid(row=1, column=0, columnspan=3, sticky="ew")

        self.label_timer = tk.Label(
            self.root,
            text=f"Timer: {self.waktu} detik",
            font=("Arial", 16, "bold"),
            bg="#34495e",
            fg="yellow",
            pady=10
        )
        self.label_timer.grid(row=2, column=0, columnspan=3, sticky="ew")

        for i in range(9):
            tmbl = tk.Button(
                self.root,
                text="",
                font=("Arial", 32, "bold"),
                width=5,
                height=2,
                bg="black",
                fg="white",
                activebackground="#333333",
                command=lambda indeks=i: self.lakukan_langkah(indeks)
            )
            baris = (i // 3) + 3
            kolom = i % 3
            tmbl.grid(row=baris, column=kolom, padx=5, pady=5)
            self.tombol.append(tmbl)

        self.label_skor = tk.Label(
            self.root,
            text=f"Skor - X: {self.skor_x} | O: {self.skor_o}",
            font=("Arial", 16, "bold"),
            bg="#34495e",
            fg="blue",  # warna skor biru
            pady=10
        )
        self.label_skor.grid(row=6, column=0, columnspan=3, sticky="ew")

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
        tombol_reset.grid(row=7, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

        self.root.configure(bg="#34495e")

    def mulai_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.waktu = 10
        self.update_timer()

    def update_timer(self):
        self.label_timer.config(text=f"Timer: {self.waktu} detik")

        if self.waktu <= 0:
            messagebox.showinfo("Waktu Habis", f"Pemain {self.pemain_sekarang.upper()} kehabisan waktu!")
            self.pemain_sekarang = "o" if self.pemain_sekarang == "x" else "x"
            self.label_pemain.config(text=f"Giliran: {self.pemain_sekarang.upper()}")
            self.mulai_timer()
            return

        self.waktu -= 1
        self.timer_id = self.root.after(1000, self.update_timer)

    def lakukan_langkah(self, indeks):
        if self.papan[indeks] == "" and not self.cek_pemenang():
            self.papan[indeks] = self.pemain_sekarang

            warna = "red" if self.pemain_sekarang == "x" else "green"

            self.tombol[indeks].config(
                text=self.pemain_sekarang.upper(),
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
                messagebox.showinfo("Permainan Selesai", f"Pemain {pemenang.upper()} Menang!")
                self.nonaktifkan_semua_tombol()
                return

            elif "" not in self.papan:
                messagebox.showinfo("Permainan Selesai", "Seri!")
                return

            # ganti pemain
            self.pemain_sekarang = "o" if self.pemain_sekarang == "x" else "x"
            self.label_pemain.config(text=f"Giliran: {self.pemain_sekarang.upper()}")

            # restart timer
            self.mulai_timer()

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
        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.pemain_sekarang = "x"
        self.papan = [""] * 9
        self.label_pemain.config(text=f"Giliran: {self.pemain_sekarang.upper()}")

        for tmbl in self.tombol:
            tmbl.config(
                text="",
                state="normal",
                bg="black",
                fg="white"
            )

        self.mulai_timer()

    def perbarui_skor(self):
        self.label_skor.config(text=f"Skor - X: {self.skor_x} | O: {self.skor_o}")


if __name__ == "__main__":
    root = tk.Tk()
    permainan = TicTacToe(root)
    root.mainloop()
