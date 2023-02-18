class Binatang:
    def __init__(self, nama):
        self.nama = nama

    def bergerak(self):
        print(f"{self.nama} sedang bergerak")

class Mamalia:
    def menyusui(self):
        print("Ibu menyusui anaknya")

class Manusia(Binatang, Mamalia):
    def __init__(self, nama, umur):
        Binatang.__init__(self, nama)
        self.umur = umur

    def bicara(self):
        print(f"{self.nama} sedang bicara")

    def tampilkan_info(self):
        print(f"{self.nama} berumur {self.umur} tahun")

h = Manusia("Budi", 25)
h.bergerak() # output: Budi sedang bergerak
h.menyusui() # output: Ibu menyusui anaknya
h.bicara() # output: Budi sedang bicara
h.tampilkan_info() # output: Budi berumur 25 tahun
