#Di Python, kelas (class) adalah struktur dasar yang digunakan untuk mengelompokkan kode dan data terkait menjadi satu unit
class Mobil:
    def __init__(self, merk, warna, tahun):
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info(self):
        print(f"Ini adalah mobil {self.merk} warna {self.warna} tahun {self.tahun}")
# Penjelasan:

# class Mobil:: Kata kunci class digunakan untuk membuat kelas baru dengan nama Mobil.
# def __init__(self, merk, warna, tahun):: Ini adalah metode khusus dalam Python yang digunakan untuk menginisialisasi objek kelas. Metode ini disebut konstruktor dan akan dipanggil setiap kali objek baru dibuat dari kelas. Dalam contoh ini, konstruktor mengambil tiga parameter: merk, warna, dan tahun.
# self.merk = merk, self.warna = warna, self.tahun = tahun: Ini adalah atribut objek. Atribut ini digunakan untuk menyimpan data yang berhubungan dengan objek. Dalam contoh ini, setiap objek mobil memiliki tiga atribut: merk, warna, dan tahun.
# def info(self):: Ini adalah metode yang didefinisikan di dalam kelas. Metode ini akan menampilkan informasi tentang mobil. Metode ini mengambil satu parameter yaitu self yang merujuk pada objek yang memanggil metode.
# print(f"Ini adalah mobil {self.merk} warna {self.warna} tahun {self.tahun}"): Ini adalah kode yang digunakan untuk mencetak informasi tentang mobil ke konsol. Kode ini menggunakan format string (f-string) untuk menggabungkan nilai atribut objek dengan teks statis.

#Dengan menggunakan kelas Mobil di atas, kita dapat membuat objek baru yang mewakili mobil dengan menggunakan sintaks berikut:
mobil_pertama = Mobil("Toyota", "merah", 2010)
mobil_kedua = Mobil("Honda", "biru", 2015)

#Setelah objek dibuat, kita dapat mengakses atribut objek dan memanggil metode dari objek tersebut:
print(mobil_pertama.merk)  # output: "Toyota"
print(mobil_kedua.warna)   # output: "biru"

mobil_pertama.info()       # output: "Ini adalah mobil Toyota warna merah tahun 2010"
mobil_kedua.info()         # output: "Ini adalah mobil Honda warna biru tahun 2015"
