# Tipe Data int Biner
# Tipe data int biner digunakan untuk merepresentasikan bilangan bulat dalam format biner (basis 2). Untuk mendefinisikan bilangan bulat biner, kita perlu menambahkan awalan 0b atau 0B sebelum angka binernya. Contoh:

x = 0b1010  # bilangan biner 1010 dalam desimal adalah 10
y = 0b1111  # bilangan biner 1111 dalam desimal adalah 15

x = int('1010', 2)  # konversi bilangan biner 1010 ke desimal, hasilnya 10
y = int('1111', 2)  # konversi bilangan biner 1111 ke desimal, hasilnya 15



# Tipe Data bool Biner
# Tipe data bool biner hanya memiliki dua nilai: True dan False, yang masing-masing merepresentasikan 1 dan 0 dalam format biner. Contoh:

x = True  # 1 dalam format biner
y = False  # 0 dalam format biner


x = True
y = False
z = x and y  # hasilnya False (0 dalam format biner)
w = x or y  # hasilnya True (1 dalam format biner)
