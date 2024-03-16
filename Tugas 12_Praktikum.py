# Achmad Rifa'i Ramadhan
# 0110223138
# TI04
# Latihan #12


class animal:
    def __init__(self,nama,makanan,hidup,berkembangBiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangBiak = berkembangBiak

    def cetak(self):
        print("Nama Hewan                   :",self.nama)
        print("Makanannya                   :",self.makanan)
        print("Hidup Di                     :",self.hidup)
        print("Berkembang Biak Dengan Cara  :",self.berkembangBiak)

class sapi(animal):
    def __init__(self,nama,makanan,hidup,berkembangBiak,bergerak,bernapas):
        super().__init__(nama,makanan,hidup,berkembangBiak)
        self.bergerak = bergerak
        self.bernapas = bernapas

    def cetak(self):
        super().cetak()
        print("Bergerak Menggunakan         :",self.bergerak)
        print("Bernafas Menggunakan         :",self.bernapas)

class harimau(animal):
    def __init__(self,nama,makanan,hidup,berkembangBiak,bergerak,bernapas):
        super().__init__(nama,makanan,hidup,berkembangBiak)
        self.bergerak = bergerak
        self.bernapas = bernapas

    def tampil(self):
        super().cetak()
        print("Bergerak Menggunakan         :",self.bergerak)
        print("Bernafas Menggunakan         :",self.bernapas)

class ular(animal):
    def __init__(self, nama,makanan,hidup,berkembangBiak,bergerak,bernapas):
        super().__init__(nama,makanan,hidup,berkembangBiak)
        self.bergerak = bergerak
        self.bernapas = bernapas

    def hasil(self):
        super().cetak()
        print("Bergerak Menggunakan         :",self.bergerak)
        print("Bernafas Menggunakan         :",self.bernapas)
        

x = sapi("Sapi","Rumput","Darat","Melahirkan","Kaki","Paru-Paru")
x.cetak()

print("------------------------------------------")

y = harimau("Harimau","Daging","Darat//Hutan","Melahirkan","Kaki","Paru-Paru")
y.tampil()

print("------------------------------------------")

z = ular("Ayam","Biji-Bijian","Darat","Bertelur","Kaki","Paru-Paru dan Kantong Udara")
z.hasil()