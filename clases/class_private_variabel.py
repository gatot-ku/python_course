
# Dalam Python, sebuah variabel yang didefinisikan di dalam kelas dan diberi awalan dengan dua garis bawah (dunder) dianggap sebagai variabel privat (private variable). Variabel privat hanya dapat diakses di dalam kelas dan tidak dapat diakses di luar kelas.

class Mobil:
    def __init__(self, merk, model, tahun):
        self.__merk = merk
        self.__model = model
        self.__tahun = tahun

    def print_info(self):
        print("Mobil ini adalah", self.__merk, self.__model, "tahun", self.__tahun)

    def get_merk(self):
       return self.__merk

    def set_merk(self, merk):
        self.__merk = merk
        print("Mobil ini adalah", self.__merk)
# Membuat objek dari kelas Mobil
mobil1 = Mobil("Toyota", "Avanza", 2020)

# Memanggil metode print_info
mobil1.print_info()#Mobil ini adalah Toyota Avanza tahun 2020

# Memanggil metode get_merk
print(mobil1.get_merk())#Toyota

# Memanggil metode set_merk/atau merubah dari set_merk
mobil1.set_merk("Honda")#Mobil ini adalah Honda

# Memanggil metode print_info lagi setelah mengubah merk
mobil1.print_info()#Mobil ini adalah Honda Avanza tahun 2020