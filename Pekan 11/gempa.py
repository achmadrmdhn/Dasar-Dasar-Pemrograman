class gempa:
    def __init__(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala
        
    def dampak(self):
        print("- Gempa", self.lokasi)
        if self.skala < 2:
            print("     Dampak Gempa : Tidak berasa")
        elif 2 <= self.skala < 4:
            print("     Dampak Gempa : Bangunan retak-retak")
        elif 4 <= self.skala < 6:
            print("     Dampak Gempa : Bangunan roboh")
        else :
            print("     Dampak Gempa : Bangunan roboh dan berpotensi tsunami")