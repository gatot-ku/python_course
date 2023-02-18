# Logging adalah proses mencatat kejadian atau peristiwa tertentu yang terjadi saat program berjalan, baik itu kesalahan (error), informasi, atau kejadian penting lainnya. Logging sangat berguna dalam proses debugging atau pemecahan masalah, karena dapat membantu kita memahami apa yang terjadi saat program berjalan dan menemukan sumber masalah yang mungkin terjadi.

#contoh
import logging

# Konfigurasi logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# Contoh penggunaan logging
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        logging.error("Tidak bisa melakukan pembagian dengan 0: %s", e)
    else:
        logging.info("Pembagian berhasil dilakukan: %s / %s = %s", x, y, result)

# Memanggil fungsi divide
divide(10, 2)
divide(10, 0)
# output -> INFO:root:Pembagian berhasil dilakukan: 10 / 2 = 5.0
# ERROR:root:Tidak bisa melakukan pembagian dengan 0: division by zero
#Hasil logging pada contoh di atas akan disimpan dalam file bernama example.log 


# Pada contoh di atas, kita mengimport modul logging dan melakukan konfigurasi logging dengan menentukan nama file log dan level logging yang diinginkan (dalam hal ini, level logging adalah DEBUG). Kemudian, kita mendefinisikan sebuah fungsi divide yang mencoba membagi dua bilangan. Jika pembagian berhasil dilakukan, kita menggunakan logging.info untuk mencatat kejadian tersebut. Namun jika pembagian gagal karena pembaginya adalah 0, kita menggunakan logging.error untuk mencatat kesalahan tersebut. Setelah itu, kita memanggil fungsi divide dua kali dengan parameter yang berbeda untuk menguji logging.

# Hasil logging pada contoh di atas akan disimpan dalam file bernama example.log dengan format seperti berikut: