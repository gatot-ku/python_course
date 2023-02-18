# Errors dan exceptions adalah masalah atau kesalahan dalam program Python yang dapat menyebabkan program tidak berjalan dengan benar. Namun, ada perbedaan antara error dan exception. Error terjadi ketika ada masalah dengan sintaks program, sedangkan exception terjadi ketika program berjalan dengan benar secara sintaks, tetapi ada masalah selama eksekusi program.


#SyntaxError: terjadi ketika ada kesalahan dalam sintaks program, seperti penulisan kurang tanda kurung atau tanda kutip. Contoh:
print("Hello World)  # Kurang tanda kutip pada akhir string

# NameError: terjadi ketika ada variabel atau fungsi yang tidak didefinisikan. Contoh:
print(x)  # Variabel 'x' tidak didefinisikan

# TypeError: terjadi ketika terjadi kesalahan dalam penggunaan tipe data, seperti mencoba menggabungkan tipe data yang tidak cocok. Contoh:
print("Age: " + 20)  # Tidak bisa menggabungkan string dan integer

# ValueError: terjadi ketika nilai yang diberikan pada fungsi tidak valid, seperti memberikan bilangan negatif pada fungsi yang hanya menerima bilangan positif. Contoh:
import math
math.sqrt(-1)  # Tidak bisa menghitung akar bilangan negatif

# ZeroDivisionError: terjadi ketika mencoba membagi bilangan dengan nol. Contoh:
x = 5
y = 0
z = x/y  # Tidak bisa membagi bilangan dengan nol

# FileNotFoundError: terjadi ketika mencoba membuka file yang tidak ditemukan. Contoh:
file = open("file.txt", "r")  # File.txt tidak ditemukan

#IndexError: terjadi ketika mencoba mengakses indeks yang tidak ada dalam list atau tuple. Contoh:
my_list = [1, 2, 3]
print(my_list[3])  # Indeks 3 tidak ada dalam list

#KeyError: terjadi ketika mencoba mengakses key yang tidak ada dalam dictionary. Contoh:
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])  # Key 'c' tidak ada dalam dictionary

#AttributeError: terjadi ketika mencoba mengakses atribut yang tidak ada dalam objek. Contoh:
my_list = [1, 2, 3]
print(my_list.size)  # Objek list tidak memiliki atribut 'size'

#AssertionError: terjadi ketika sebuah assertion gagal. Assertion adalah cara untuk memeriksa kondisi tertentu dalam program, dan jika kondisinya salah, assertion akan memberikan pesan error. Contoh:
x = 5
assert x == 10, "x harus sama dengan 10"  # Assertion akan gagal karena x tidak sama dengan 10

#ImportError: terjadi ketika mencoba mengimpor modul yang tidak ditemukan. Contoh:
import non_existent_module  # Modul tidak ditemukan

#IndentationError: terjadi ketika ada masalah dalam indentasi program, seperti indentasi yang tidak konsisten. Contoh:
def my_function():
print("Hello World")  # Indentasi pada baris kedua harus diperbaiki

#IOError: terjadi ketika ada masalah dengan input/output, seperti mencoba membaca file yang tidak dapat dibaca. Contoh:
file = open("non_existent_file.txt", "r")  # File tidak ditemukan atau tidak dapat dibuka

#KeyboardInterrupt: terjadi ketika pengguna menghentikan program dengan menekan tombol CTRL-C. Contoh:
while True:
    # Program akan terus berjalan sampai pengguna menekan CTRL-C

#MemoryError: terjadi ketika tidak cukup memori untuk menjalankan program. Contoh:
my_list = [1] * 1000000000  # List terlalu besar untuk dimuat ke dalam memori

#OverflowError: terjadi ketika hasil operasi aritmatika terlalu besar untuk dimuat dalam tipe data yang diberikan. Contoh:
import math
print(math.exp(1000))  # Hasil dari operasi ini terlalu besar untuk dimuat dalam tipe data float

#RecursionError: terjadi ketika terjadi rekursi yang terlalu dalam, sehingga memakan terlalu banyak memori. Contoh:
def my_function(x):
    if x == 0:
        return 0
    else:
        return my_function(x-1) + 1

my_function(100000)  # Terjadi rekursi terlalu dalam


#TypeError: terjadi ketika tipe data yang tidak cocok digunakan pada operasi tertentu, seperti menggabungkan list dengan tuple. Contoh:
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
print(my_list + my_tuple)  # Tidak bisa menggabungkan list dan tuple

#UnboundLocalError: terjadi ketika mencoba menggunakan variabel lokal sebelum diberi nilai. Contoh:
def my_function():
    print(x)
    x = 5

my_function()  # Variabel 'x' belum diberi nilai sebelum digunakan

