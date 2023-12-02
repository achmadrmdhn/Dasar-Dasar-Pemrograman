# Achmad Rifa'i Ramadhan
# 0110223138
# TI04
# Latihan #8

# Soal Nomor 1
print("--- Nomor 1 ---")
def profil(nama, alamat, gender, umur, hoby):
    print("Profil:")
    print("Nama:", nama)
    print("Alamat:", alamat)
    print("Gender:", gender)
    print("Umur:", umur)
    print("Hoby:", hoby)

# Pemanggilan
nama = ("Achmad Rifa'i Ramadhan")
alamat = ("Bogor")
gender = ("Laki-laki")
umur = ("19 tahun")
hoby = ("Mengedit")

profil(nama, alamat, gender, umur, hoby)
print("")

# Soal Nomor 2
print("--- Nomor 2 ---")
def cek_kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif 60 <= nilai <=70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai Tidak Valid" 

# Pemanggilan
print(cek_kelulusan(60))
print("")

# Soal Nomor 3
print("--- Soal Nomor 3. ---")
def ganjil(n):
    for i in range(1, n+1, 2):
        print(i)

# Pemanggilan
ganjil(100)
print("")