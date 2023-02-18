# Membaca file teks
# Untuk membaca file teks, Anda dapat menggunakan fungsi built-in "open" pada Python. Fungsi ini membuka file dan mengembalikan objek file yang dapat digunakan untuk membaca isi file. Berikut adalah contoh membaca file teks:

# membuka file
file = open("nama_file.txt", "r")

# membaca isi file
data = file.read()

# menutup file
file.close()

# mencetak isi file
print(data)


# Menulis file teks
# Untuk menulis file teks, Anda dapat menggunakan fungsi built-in "open" pada Python. Fungsi ini membuka file dan mengembalikan objek file yang dapat digunakan untuk menulis ke file. Berikut adalah contoh menulis ke file teks:
# membuka file
file = open("nama_file.txt", "w")

# menulis ke file
file.write("Ini adalah contoh penulisan ke file")

# menutup file
file.close()


# Membaca file biner
# Untuk membaca file biner, Anda dapat menggunakan fungsi built-in "open" pada Python. Fungsi ini membuka file dan mengembalikan objek file yang dapat digunakan untuk membaca isi file. Berikut adalah contoh membaca file biner:
# membuka file
file = open("nama_file.jpg", "rb")

# membaca isi file
data = file.read()

# menutup file
file.close()
# melakukan sesuatu dengan data


# Menulis file biner
# Untuk menulis file biner, Anda dapat menggunakan fungsi built-in "open" pada Python. Fungsi ini membuka file dan mengembalikan objek file yang dapat digunakan untuk menulis ke file. Berikut adalah contoh menulis ke file biner:
# membuka file
file = open("nama_file.jpg", "wb")

# menulis ke file
file.write(b"some binary data")

# menutup file
file.close()

# untuk mengonversi JSON string ke dalam struktur data Python.
import json

# contoh data dictionary
data = {
    "nama": "John Doe",
    "umur": 30,
    "alamat": {
        "jalan": "Jl. Merdeka",
        "kota": "Jakarta"
    },
    "hobi": ["berenang", "membaca", "travelling"]
}

# konversi ke JSON string
json_data = json.dumps(data)

# simpan ke dalam file
with open("data.json", "w") as file:
    file.write(json_data) #file  sudah terbuat "{} data,json


# Untuk mengonversi JSON string ke dalam struktur data Python, kita dapat menggunakan method json.loads() dari modul json. Berikut adalah contoh kode untuk mengonversi data dari file data.json yang telah disimpan dalam format JSON kembali ke struktur data Python:

import json

# membaca data dari file
with open("data.json", "r") as file:
    json_data = file.read()

# mengonversi dari JSON string ke dictionary Python
data = json.loads(json_data)

# mencetak struktur data Python
print(data)

#---------------
try:
    f = open('file.txt', 'r')
    # melakukan operasi membaca file kalau ada
    
    # tambahkan pernyataan if di sini
    if f.mode == 'r':
        contents = f.read()
        print(contents)
        
except:
    print('Error occurred while reading the file.')
    #kalau tidak di temukan akan menampilkan error ini dan menutup "f.close()"
finally:
    f.close()

