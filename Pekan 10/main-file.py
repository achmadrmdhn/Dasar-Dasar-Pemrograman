# Achmad Rifa'i Ramadhan
# 0110223138
# TI04
# Latihan #10


from bangun_datar import *
from perhitungan import *

# Bangun Datar Segitiga
alas_segitiga = 5
tinggi_segitiga = 8
sisi_a = 3
sisi_b = 4
sisi_c = 5

print("Luas Segitiga:", luas_segitiga(alas_segitiga, tinggi_segitiga))
print("Keliling Segitiga:", keliling_segitiga(sisi_a, sisi_b, sisi_c))

# Bangun Datar Persegi
sisi_persegi = 4
print("Luas Persegi:", luas_persegi(sisi_persegi))
print("Keliling Persegi:", keliling_persegi(sisi_persegi))

# Bangun Datar Persegi Panjang
panjang_persegi_panjang = 5
lebar_persegi_panjang = 12
print("Luas Persegi Panjang:", luas_persegi_panjang(panjang_persegi_panjang, lebar_persegi_panjang))
print("Keliling Persegi Panjang:", keliling_persegi_panjang(panjang_persegi_panjang, lebar_persegi_panjang))

# Bangun Datar Jajar Genjang
A = 12
B = 7
print("Luas Jajar Genjang:", luas_jajar_genjang(A, B))
print("Keliling Jajar Genjang:", keliling_jajar_genjang(A, B))

# Bangun Datar Belah Ketupat
diagonal_1 = 3
diagonal_2 = 8
sisi = 5
print("Luas Belah Ketupat:", luas_belah_ketupat(diagonal_1, diagonal_2))
print("Keliling Belah Ketupat:", keliling_belah_ketupat(sisi))


# Perhitungan
angka1 = 10
angka2 = 5
print("Tambah:", tambah(angka1, angka2))
print("Kurang:", kurang(angka1, angka2))
print("Pangkat:", pangkat(angka1, angka2))
print("Kali:", kali(angka1, angka2))
print("Bagi:", bagi(angka1, angka2))
print("Sin:", sin(30))
print("Cos:", cos(60))
print("Log:", log(angka1))
print("Akar:", akar(angka1))
print("Tan:", tan(45))