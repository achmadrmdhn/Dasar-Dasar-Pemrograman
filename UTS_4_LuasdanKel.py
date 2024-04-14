# Achmad Rifa'i Ramadhan
# 0110223138
# TI04
# Soal UTS_Nomor 4
# Menghitung Luas dan Keliling_Trapesium

print("4. Menghitung Luas dan Keliling Trapesium", "\n")
# Menginput sisi
sisi_a = float(input("Masukkan sisi A trapesium: "))
sisi_b = float(input("Masukkan sisi B trapesium: "))
sisi_c = float(input("Masukkan sisi C trapesium: "))
sisi_d = float(input("Masukkan sisi D trapesium: "))
tinggi = float(input("Masukkan tinggi trapesium: "))

# Menghitung luas trapesium
luas_trapesium = (sisi_a + sisi_b) * tinggi / 2

# Menghitung keliling trapesium
keliling_trapesium = sisi_a + sisi_b + sisi_c + sisi_d

# Menampilkan output hasil keduanya
print(f"Luas trapesium adalah: {luas_trapesium}")
print(f"Keliling trapesium adalah: {keliling_trapesium}")
print("== Operator Selesai ==")