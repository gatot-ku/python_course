# Modules dalam Python adalah sebuah file yang berisi kode Python yang dapat diimport ke dalam program Python lainnya. Dengan menggunakan modules, kita dapat mengorganisir kode menjadi kelompok-kelompok terpisah, sehingga memudahkan pengembangan dan pemeliharaan kode.

import math
#math: module ini berisi fungsi-fungsi matematika seperti fungsi trigonometri, eksponensial, logaritma, dan sebagainya
sudut = 30
sin_sudut = math.sin(math.radians(sudut))
print(sin_sudut)


import random
#random: module ini berisi fungsi-fungsi untuk menghasilkan bilangan acak.
bilangan_acak = random.randint(1, 10)
print(bilangan_acak)

import os
#os: module ini berisi fungsi-fungsi untuk berinteraksi dengan sistem operasi. Contohnya, untuk mendapatkan path dari direktori saat ini
path_sekarang = os.getcwd()
print(path_sekarang)


import datetime
#datetime: module ini berisi fungsi-fungsi untuk bekerja dengan tanggal dan waktu. Contohnya,
tanggal_sekarang = datetime.datetime.now()
print(tanggal_sekarang)

import re
#re: module ini berisi fungsi-fungsi untuk bekerja dengan ekspresi reguler (regular expressions)
teks = "Halo, nama saya John"
hasil = re.search(r"\bJ\w+", teks)
print(hasil.group())

import sys
# sys: module ini berisi fungsi-fungsi untuk berinteraksi dengan interpreter Python dan sistem operasi. Contohnya
# if not condition:
#     print("Terjadi kesalahan.")
#     sys.exit(1)


import time
#time: module ini berisi fungsi-fungsi untuk bekerja dengan waktu
mulai = time.time()
# kode program
selesai = time.time()
print("Waktu eksekusi:", selesai - mulai, "detik")


import json
#json: module ini berisi fungsi-fungsi untuk bekerja dengan format data JSON
with open("data.json", "r") as file:
    data = json.load(file)
print(data)


import csv
# csv: module ini berisi fungsi-fungsi untuk bekerja dengan format data CSV (Comma-Separated Values)
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


import argparse
#argparse: module ini berisi fungsi-fungsi untuk memproses argumen baris perintah (command-line arguments)
parser = argparse.ArgumentParser()
parser.add_argument("nama", help="nama pengguna")
parser.add_argument("-a", "--alamat", help="alamat pengguna")
args = parser.parse_args()
print("Nama:", args.nama)
print("Alamat:", args.alamat)

from collections import Counter
#collections: module ini berisi tipe data koleksi seperti list, tuple, dan dictionary. 
teks = "Halo, nama saya John. Saya suka makan nasi goreng."
kata = teks.split()
frekuensi = Counter(kata)
print(frekuensi)#Counter({'saya': 2, 'Halo,': 1, 'nama': 1, 'John.': 1, 'suka': 1, 'makan': 1, 'nasi': 1, 'goreng.': 1})

import pickle
#pickle: module ini berisi fungsi-fungsi untuk mengonversi objek Python ke format byte dan sebaliknya.
data = [1, 2, 3, 4, 5]
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

import hashlib
#hashlib: module ini berisi fungsi-fungsi untuk menghasilkan hash dari sebuah objek.
password = "password123"
hash = hashlib.sha256(password.encode()).hexdigest()
print(hash)




import socket

HOST = ""  # hostname atau IP address dari server
PORT = 1234  # port yang digunakan

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #Membuat objek socket menggunakan protokol TCP/IP dengan menggunakan method socket.AF_INET dan socket.SOCK_STREAM. Objek socket disimpan dalam variabel s.
    s.bind((HOST, PORT))
    # Mengikat socket ke HOST dan PORT yang telah ditentukan sebelumnya.
    s.listen()
    # Mendengarkan koneksi yang masuk dari client.
    conn, addr = s.accept()
    #Menerima koneksi dari client. Objek conn adalah objek socket yang terhubung ke client. Objek addr adalah informasi alamat dari client
    with conn:
        #Membuat blok with statement untuk mengatur objek conn agar dapat di-close dengan benar setelah digunakan.
        print("Terhubung oleh", addr)
        while True:
            #Mencetak pesan untuk memberitahukan bahwa server telah terhubung oleh client dengan alamat IP tertentu.
            data = conn.recv(1024)
            #Menerima data yang dikirimkan oleh client dan mengirimkan data tersebut kembali ke client. Loop while True akan terus berjalan hingga tidak ada data yang diterima.
            if not data:
                break
            conn.sendall(data)


# Dalam Python, kita dapat menjalankan sebuah modul sebagai script. Ini berarti bahwa kita dapat menulis kode Python dalam sebuah file dan menjalankannya langsung dari baris perintah tanpa harus mengimpor file tersebut ke dalam program Python lain.

# Untuk menjalankan sebuah modul sebagai script, kita dapat menambahkan kode yang diinginkan ke dalam blok "if name == 'main':" pada akhir modul. Kode di dalam blok ini akan dieksekusi hanya jika modul dijalankan sebagai script, dan tidak akan dieksekusi jika modul diimpor ke dalam program Python lain.

# my_module.py
def multiply(a, b):
    return a * b

if __name__ == '__main__':
    # contoh penggunaan
    result = multiply(2, 3)
    print(result)
# Dalam contoh di atas, kita mendefinisikan sebuah fungsi multiply yang mengembalikan hasil perkalian dari dua argumen yang diberikan. Kemudian, kita menambahkan kode di dalam blok "if name == 'main':" untuk menjalankan fungsi multiply sebagai contoh penggunaan ketika modul dijalankan sebagai script.

# Jika kita menjalankan modul ini dari baris perintah dengan perintah "python my_module.py", maka output yang dihasilkan adalah:6



import urllib.request
#Modul urllib adalah modul standar Python yang berguna untuk mengambil data dari Internet. Berikut ini adalah contoh kode sederhana yang menggunakan modul urllib untuk mengambil halaman web dari Internet:
url = 'https://www.python.org/'
response = urllib.request.urlopen(url)

print(response.read())

# Penjelasan:

# Pertama, kita mengimpor modul urllib.request untuk mengakses fungsi-fungsi yang digunakan untuk mengambil data dari Internet.
# Kemudian, kita menetapkan variabel url dengan URL yang akan diambil datanya.
# Selanjutnya, kita menggunakan fungsi urllib.request.urlopen() untuk membuka koneksi ke URL tersebut dan mengambil data halaman webnya.
# Hasilnya disimpan dalam variabel response.
# Terakhir, kita menggunakan fungsi response.read() untuk membaca data dari response dan mencetaknya.

# Fungsi dir() di Python adalah sebuah built-in function yang digunakan untuk mengembalikan daftar nama-nama atribut (atau properti) dari sebuah objek.
my_list = [1, 2, 3]
print(dir(my_list))
#output ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# 
