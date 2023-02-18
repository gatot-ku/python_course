# pass statement adalah perintah kosong di dalam Python. Statement ini tidak melakukan apa-apa dan digunakan sebagai placeholder atau penanda tempat yang diperlukan pernyataan di masa depan. Dalam beberapa kasus, ketika kita menulis kode, kita mungkin tidak ingin melakukan apa-apa saat menulis pernyataan tertentu, tetapi kita tidak dapat mengosongkan ruang atau menghapus pernyataan itu, karena itu akan menghasilkan kesalahan sintaksis. Dalam kasus seperti ini, pass digunakan untuk mempertahankan sintaksis yang benar dan memberi tahu interpreter bahwa kode di dalam blok tersebut belum selesai.

# Contoh 1
for i in range(10):
    if i == 5:
        pass
    print(i)

# Contoh 2
def my_function():
    pass

# Contoh 3
class MyClass:
    def __init__(self):
        pass

    def my_method(self):
        pass
    

# Pada contoh pertama, pernyataan pass digunakan di dalam blok if untuk menunjukkan bahwa tidak ada tindakan yang harus dilakukan jika i == 5. Pada contoh kedua, pass digunakan dalam definisi fungsi untuk menunjukkan bahwa fungsi masih kosong dan belum diimplementasikan. Pada contoh ketiga, pass digunakan di dalam definisi kelas untuk menunjukkan bahwa metode kelas masih kosong dan belum diimplementasikan.    
