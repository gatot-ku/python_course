# Inheritance atau pewarisan adalah konsep penting dalam pemrograman berorientasi objek di Python. Dalam inheritance, kita dapat membuat sebuah kelas baru yang mengambil sifat atau method dari kelas yang telah ada sebelumnya. Kelas yang ada sebelumnya disebut kelas induk atau superclass, sedangkan kelas baru yang kita buat disebut kelas turunan atau subclass.

# Untuk membuat kelas turunan, kita cukup menuliskan nama kelas induk dalam tanda kurung setelah nama kelas turunan. Selanjutnya, kita dapat menambahkan sifat atau method baru ke dalam kelas turunan, atau meng-overwrite sifat atau method yang sudah ada dalam kelas induk.

class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bicara(self):
        print("Halo, nama saya", self.nama, "dan saya berumur", self.umur)

class Mahasiswa(Manusia):
    def __init__(self, nama, umur, npm):
        super().__init__(nama, umur)
        self.npm = npm

    def belajar(self):
        print("Saya",self.nama, "sedang belajar di kampus.",  "dan saya berumur", self.umur, "dengan NPM", self.npm)

# membuat objek dari kelas Manusia
orang = Manusia("Budi", 20)
orang.bicara()#Halo, nama saya Budi dan saya berumur 20

# membuat objek dari kelas Mahasiswa
mhs = Mahasiswa("Agus", 21, "123456789")
mhs.bicara()#Halo, nama saya Agus dan saya berumur 21
mhs.belajar()#Saya Agus sedang belajar di kampus. dan saya berumur 21 dengan NPM 123456789




# Pada contoh di atas, kita memiliki dua kelas: Manusia dan Mahasiswa. Kelas Mahasiswa merupakan kelas turunan dari kelas Manusia. Kelas Manusia memiliki sifat nama dan umur, serta method bicara(). Kelas Mahasiswa menambahkan sifat npm, dan method belajar(). Method __init__() pada kelas Mahasiswa menggunakan method super() untuk memanggil constructor kelas induk Manusia.

# Dalam contoh di atas, kita membuat dua objek: orang dan mhs. Objek orang adalah objek dari kelas Manusia, sedangkan objek mhs adalah objek dari kelas Mahasiswa. Objek orang hanya bisa memanggil method bicara(), sedangkan objek mhs dapat memanggil method bicara() dan belajar(), karena kelas Mahasiswa mewarisi sifat dan method dari kelas Manusia.