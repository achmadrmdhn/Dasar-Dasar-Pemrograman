# Achmad Rifa'i Ramadhan
# 0110223138
# TI04
# Latihan #9

# Nomor 1
print("--- 1. Nama Siswa Yang Lulus---")
lulus_saja = []
hasil_akhir =[
    {'nama':'Reza', 'nilai':70},
    {'nama':'Ciut', 'nilai':63},
    {'nama':'Dian', 'nilai':80},
    {'nama':'Badu', 'nilai':40}
]
for mahasiswa in hasil_akhir:
    if mahasiswa['nilai'] > 65 :
        lulus_saja.append(mahasiswa['nama'])
print(lulus_saja)
print("")

# Nomor 2
print("---2. Membalik Nama Buah---")
def membalik(buah):
    reversed_fruitslist = []
    for i in range(len(buah) - 1, -1, -1):
        reversed_fruitslist.append(buah[i])
    return reversed_fruitslist

hasil = membalik(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])
print("Hasil Membalik :", hasil)
print("")

# Nomor 3
print("---3. Duplikasi Nama Buah---")
def duplikasi(fruits):
    duplicated_fruitslist = []
    for fruit in fruits:
        duplicated_fruitslist.extend([fruit, fruit])
    return duplicated_fruitslist

hasil = duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu'])
print("Hasil Duplikasi :", hasil)
print("")

# Nomor 4
print("---4. Filter Konsonan---")
def filter_konsonan(string):
    konsonan = ''
    for char in string:
        if char.isalpha() and char.lower() not in 'aeiou':
            konsonan += char
    return konsonan

hasil = filter_konsonan("Nurul Fikri")
print("Hasil Filter Konsonan :", hasil)