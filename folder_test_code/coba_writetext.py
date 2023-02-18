# Meminta user untuk memasukkan angka
number = int(input("Masukkan angka: "))

# Menentukan nama file berdasarkan angka
if number % 2 == 0:
    filename = "genap.txt"
else:
    filename = "ganjil.txt"

# Membuka file dalam mode tulis (write mode)
file = open(filename, "w")

# Menulis angka ke file
file.write(str(number))

# Menutup file
file.close()
#----------------
# Mencetak pesan
print("Angka telah ditulis ke file", filename)

# Membuka file dalam mode baca (read mode)
file = open("ganjil.txt", "r")

# Membaca isi file dan menyimpannya dalam variabel text
text = file.read()

# Menutup file
file.close()

# Mencetak isi file
print("Isi file:")
print(text)



# Untuk mengonversi JSON string ke dalam struktur data Python, kita dapat menggunakan method json.loads() dari modul json. Berikut adalah contoh kode untuk mengonversi data dari file data.json yang telah disimpan dalam format JSON kembali ke struktur data Python:

import json

# membaca data dari file
with open("data.json", "r") as file:
    json_data = file.read()

# mengonversi dari JSON string ke dictionary Python
data = json.loads(json_data)

# mencetak struktur data Python
print(data)



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

#--------------
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
