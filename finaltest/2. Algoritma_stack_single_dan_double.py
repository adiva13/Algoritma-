#algoritma stack single
class StackSingle:
    def __init__(self, kapasitas):
        self.stack = [None] * kapasitas
        self.kapasitas = kapasitas
        self.TOP = -1

    def push(self, data):
        if self.TOP == self.kapasitas - 1:
            print("Stack penuh, tidak bisa menambah lagi. ")
        else:
            self.TOP += 1
            self.stack[self.TOP] = data
            print(f"push: {data}")

    def pop(self):
        if self.TOP == -1:
            print("Stack kosong, tidak bisa mengeluarkan data. ")
        else:
            data = self.stack[self.TOP]
            self.TOP -= 1
            print(f"Pop: {data}")
            return data
        
    def show(self):
        print("isi Stack Emas:")
        for i in range(self.TOP, -1, -1):
            print(self.stack[i])

# === PROGRAM UTAMA ===
stack_emas = StackSingle(5)

stack_emas.push("Emas 24K")
stack_emas.push("Emas 22K")
stack_emas.push("Emas Antam")
stack_emas.show()

stack_emas.pop()
stack_emas.show()

#algoritma stack double
# Stack Double dalam satu array dengan objek barang

class StackDouble:
    def __init__(self, kapasitas):
        self.stack = [None] * kapasitas
        self.kapasitas = kapasitas
        self.TOP1 = -1              # Stack kiri
        self.TOP2 = kapasitas       # Stack kanan

    def push1(self, data):
        if self.TOP1 + 1 == self.TOP2:
            print("Stack penuh! Tidak dapat menambah ke Stack 1.")
        else:
            self.TOP1 += 1
            self.stack[self.TOP1] = data
            print(f"Push ke Stack 1 (Elektronik): {data}")

    def push2(self, data):
        if self.TOP2 - 1 == self.TOP1:
            print("Stack penuh! Tidak dapat menambah ke Stack 2.")
        else:
            self.TOP2 -= 1
            self.stack[self.TOP2] = data
            print(f"Push ke Stack 2 (Dapur): {data}")

    def pop1(self):
        if self.TOP1 == -1:
            print("Stack 1 kosong!")
        else:
            data = self.stack[self.TOP1]
            self.TOP1 -= 1
            print(f"Pop dari Stack 1: {data}")
            return data

    def pop2(self):
        if self.TOP2 == self.kapasitas:
            print("Stack 2 kosong!")
        else:
            data = self.stack[self.TOP2]
            self.TOP2 += 1
            print(f"Pop dari Stack 2: {data}")
            return data

    def show(self):
        print("\n=== ISI STACK ===")
        print("Stack 1 (Elektronik):")
        for i in range(self.TOP1, -1, -1):
            print(self.stack[i])

        print("\nStack 2 (Dapur):")
        for i in range(self.TOP2, self.kapasitas):
            print(self.stack[i])


# === PROGRAM UTAMA ===
stack_barang = StackDouble(10)

stack_barang.push1("Laptop")
stack_barang.push1("Smartphone")
stack_barang.push1("Headset")

stack_barang.push2("Panci")
stack_barang.push2("Piring")
stack_barang.push2("Gelas")

stack_barang.show()

stack_barang.pop1()
stack_barang.pop2()
stack_barang.show()
