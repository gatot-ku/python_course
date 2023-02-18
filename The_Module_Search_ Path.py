# Module Search Path di Python adalah daftar direktori yang digunakan oleh Python untuk mencari modul atau file yang akan diimpor ke dalam program. Ketika Python menjalankan statement import, ia akan mencari file modul tersebut di dalam setiap direktori pada Module Search Path, secara berurutan. Jika modul ditemukan dalam direktori tersebut, maka Python akan mengimpor dan memuatnya ke dalam program.

# Berikut adalah contoh dari Module Search Path di Python:

# Direktori tempat script berada
# Misalkan kita memiliki file script bernama test.py yang berada di direktori /home/user/. Jika kita menambahkan perintah import module1 di dalam file tersebut, maka Python akan mencari modul module1.py di dalam direktori /home/user/.

# Direktori bawaan Python
# Python memiliki beberapa direktori bawaan yang selalu disertakan dalam Module Search Path. Direktori ini dapat berbeda-beda tergantung pada platform atau instalasi Python yang digunakan. Sebagai contoh, pada instalasi Python untuk Windows, direktori bawaan Python biasanya berada di C:\PythonXX\Lib, di mana XX adalah versi Python yang digunakan.

# Direktori yang ditentukan oleh pengguna
# Pengguna dapat menambahkan direktori tertentu ke dalam Module Search Path dengan cara menambahkan path tersebut ke dalam variabel lingkungan PYTHONPATH. Misalnya, jika kita ingin menambahkan direktori /home/user/modules/ ke dalam Module Search Path, kita dapat menambahkan perintah export PYTHONPATH="/home/user/modules/" di terminal atau shell yang digunakan.

# Direktori yang ditentukan oleh aplikasi
# Beberapa aplikasi Python dapat menentukan direktori tertentu yang harus dimasukkan ke dalam Module Search Path. Sebagai contoh, jika kita menggunakan aplikasi Jupyter Notebook atau Anaconda, direktori site-packages pada direktori instalasi Anaconda akan dimasukkan ke dalam Module Search Path secara otomatis.

#Pertama-tama, kita buat sebuah modul bernama my_module.py di dalam direktori /home/user/modules/ dengan isi sebagai berikut:

# my_module.py
def say_hello(name):
    print(f"Hello, {name}!")

# Selanjutnya, kita buat sebuah file skrip bernama main.py yang berada di direktori /home/user/. Di dalam file skrip ini, kita akan mengimpor modul my_module dan menggunakan fungsinya.    
# main.py

import sys

# Tambahkan path direktori modules ke dalam module search path
sys.path.append('/home/user/modules')

# Impor modul my_module
import my_module

# Panggil fungsi say_hello() dari modul my_module
my_module.say_hello('John')


# Dalam kode di atas, kita menggunakan modul sys untuk menambahkan direktori /home/user/modules ke dalam Module Search Path. Selanjutnya, kita mengimpor modul my_module dan memanggil fungsi say_hello() dari modul tersebut.

# Ketika kita menjalankan file skrip main.py, Python akan mencari modul my_module di dalam setiap direktori pada Module Search Path, termasuk direktori /home/user/modules yang kita tambahkan ke dalam daftar tersebut. Jika modul ditemukan di dalam direktori tersebut, maka Python akan mengimpor dan memuatnya ke dalam program dan kita dapat menggunakan fungsinya seperti biasa.