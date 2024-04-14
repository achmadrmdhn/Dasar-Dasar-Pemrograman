# Achmad Rifa'i Ramadhan
# 0110223138
# TI04
# Soal UTS_Nomor 5
# Kalkulator Sederhana

print("5. Kalkulator Sederhana", "\n")
angka1 = int(input("Masukan Angka 1 :"))
angka2 = int(input("Masukan Angka 2 :"))
operator = input("Pilihan Operator :")
print(operator)

if operator == "Tambah":
    print("Hasil Operator : ", angka1+angka2)
elif operator == "Kurang":
    print("Hasil Operator : ", angka1-angka2)
elif operator == "Bagi":
    print("Hasil Operator : ", angka1/angka2)
elif operator == "Kali":
    print("Hasil Operator : ", angka1*angka2)
elif operator == "Pangkat":
    print("Hasil Operator : ", angka1**angka2)    
else :
    print("Tidak ada proses yang sesuai!")
print("== Operator Selesai ==")