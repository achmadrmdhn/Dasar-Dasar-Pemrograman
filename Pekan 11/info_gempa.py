# Achmad Rifa'i Ramadhan
# 0110223138
# TI04
# Latihan #11


from gempa import *

# 5 Objek Gempa
Banten=gempa("Banten", 1.2)
Palu=gempa("Palu", 6.1)
Cianjur=gempa("Cianjur", 5.6)
Jayapura=gempa("Jayapura", 3.3)
Garut=gempa("Garut", 4.0)

Banten.dampak()
Palu.dampak()
Cianjur.dampak()
Jayapura.dampak()
Garut.dampak()