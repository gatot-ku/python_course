# Penggunaan fungsi abs() dalam loop dan if statements dapat membantu kita dalam melakukan pengolahan data atau perhitungan
#matematis yang lebih kompleks. Berikut adalah contoh penggunaan fungsi abs() dalam loop dan if statements di Python:


#Contoh 1: Menghitung rata-rata nilai absolut dari suatu list of numbers
# contoh list of numbers
numbers = [-5, 10, -15, 20, -25]

# inisialisasi variabel sum dan count
sum = 0
count = 0

# loop untuk menghitung rata-rata nilai absolut dari setiap angka di dalam list
for num in numbers:
  sum += abs(num)
  count += 1

# mencetak rata-rata nilai absolut
if count > 0:
  avg_abs = sum / count
  print("Rata-rata nilai absolut adalah:", avg_abs)#15.0
else:
  print("List kosong")


# Contoh 2: Mencari nilai terbesar dari dua bilangan berdasarkan nilai absolutnya#
# input dua bilangan
a = -10
b = 20

# mencari nilai terbesar berdasarkan nilai absolutnya
if abs(a) > abs(b):
  print("Nilai absolut a lebih besar dari nilai absolut b")
  print("Nilai terbesar adalah:", a)
else:
  print("Nilai absolut b lebih besar dari nilai absolut a")
  print("Nilai terbesar adalah:", b)#20
  
# Dalam contoh-contoh di atas, fungsi abs() digunakan untuk melakukan pengolahan data yang lebih kompleks, seperti menghitung rata-rata nilai absolut dari sebuah list, atau memilih nilai terbesar dari dua bilangan berdasarkan nilai absolutnya. Kombinasi loop dan if statements dengan fungsi abs() dapat membantu kita dalam menyelesaikan berbagai macam perhitungan matematis dengan lebih mudah dan efisien.

