#nama : Siti adiva kirani
#Nim : D0425302
#Kelas : B_SistemInformasi

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

        self.buat_widget()

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
            text=f"Giliran: {self.pemain_sekarang}",
            font=("Arial", 16),
            bg="#34495e",
            fg="white",
            pady=10
        )
        self.label_pemain.grid(row=1, column=0, columnspan=3, sticky="ew")

        for i in range(9):
            tmbl = tk.Button(
                self.root,
                text="",
                font=("Arial", 32, "bold"),
                width=5,
                height=2,
                bg="#ecf0f1",
                activebackground="#bdc3c7",
                command=lambda indeks=i: self.lakukan_langkah(indeks)
            )
            baris = (i // 3) + 2
            kolom = i % 3
            tmbl.grid(row=baris, column=kolom, padx=5, pady=5)
            self.tombol.append(tmbl)

        self.label_skor = tk.Label(
            self.root,
            text=f"Skor - x: {self.skor_x} | o: {self.skor_o}",
            font=("Arial", 14),
            bg="#34495e",
            fg="white",
            pady=10
        )
        self.label_skor.grid(row=5, column=0, columnspan=3, sticky="ew")

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
        tombol_reset.grid(row=6, column=0, columnspan=3, sticky="ew", padx=5, pady=5)

        self.root.configure(bg="#34495e")

    def lakukan_langkah(self, indeks):
        if self.papan[indeks] == "" and not self.cek_pemenang():
            self.papan[indeks] = self.pemain_sekarang
            self.tombol[indeks].config(
                text=self.pemain_sekarang,
                fg="#e74c3c" if self.pemain_sekarang == "x" else "#3498db",
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

            elif "" not in self.papan:
                messagebox.showinfo("Permainan Selesai", "Seri!")

            else:
                self.pemain_sekarang = "o" if self.pemain_sekarang == "x" else "x"
                self.label_pemain.config(text=f"Giliran: {self.pemain_sekarang}")

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
                bg="#ecf0f1"
            )

    def perbarui_skor(self):
        self.label_skor.config(text=f"Skor - x: {self.skor_x} | o: {self.skor_o}")


if __name__ == "__main__":
    root = tk.Tk()
    permainan = TicTacToe(root)
    root.mainloop()
