# Membuat list kosong
my_list = []

# Membuat list dengan beberapa elemen
my_list = [1, 2, 3, "hello", "world"]

my_list = [1, 2, 3, "hello", "world"]

# Mengakses elemen pada indeks ke-2 (indeks dimulai dari 0)
print(my_list[2]) # Output: 3

# Mengakses elemen pada indeks terakhir dengan menggunakan indeks negatif
print(my_list[-1]) # Output: world


my_list = [1, 2, 3, "hello", "world"]

# Menambahkan elemen ke akhir list
my_list.append("python")
print(my_list) # Output: [1, 2, 3, "hello", "world", "python"]


my_list = [1, 2, 3, "hello", "world"]

# Menghapus elemen dengan nilai "hello"
my_list.remove("hello")
print(my_list) # Output: [1, 2, 3, "world"]


my_list = [1, 2, 3, "hello", "world"]

# Mengambil elemen pada indeks ke-1 hingga ke-3
print(my_list[1:4]) # Output: [2, 3, "hello"]

# Mengambil elemen dari awal hingga indeks ke-2
print(my_list[:3]) # Output: [1, 2, 3]

# Mengambil elemen dari indeks ke-2 hingga akhir
print(my_list[2:]) # Output: [3, "hello", "world"]


# Di Python, terdapat beberapa metode (method) yang dapat digunakan untuk memanipulasi list. Berikut adalah beberapa contoh metode yang sering digunakan:

#append
my_list = [1, 2, 3]
my_list.append(4)
print(my_list) # output: [1, 2, 3, 4]

#extend
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list) # output: [1, 2, 3, 4, 5]

#insert
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list) # output: [1, 5, 2, 3]

#remove
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list) # output: [1, 3, 2]

#pop
my_list = [1, 2, 3]
last_elem = my_list.pop()
print(last_elem) # output: 3
print(my_list) # output: [1, 2]

second_elem = my_list.pop(1)
print(second_elem) # output: 2
print(my_list) # output: [1]

#index
my_list = [1, 2, 3]
index_of_two = my_list.index(2)
print(index_of_two) # output: 1

#count
my_list = [1, 2, 3, 2]
count_of_two = my_list.count(2)
print(count_of_two) # output: 2

#sort
my_list = [3, 1, 2]
my_list.sort()
print(my_list) # output: [1, 2, 3]

#reverse
my_list = [1, 2, 3]
my_list.reverse()
print(my_list) # output: [3, 2, 1]

# dll

#  data antrian (queue) dengan menggunakan metode yang disebut "FIFO" (first-in, first-out), 
# append() untuk menambahkan elemen baru ke antrian dan
# metode pop() untuk mengambil elemen teratas dari antrian.
# Membuat list sebagai antrian
antrian = []

# Menambahkan elemen ke antrian
antrian.append('apel')
antrian.append('jeruk')
antrian.append('mangga')

print("Antrian saat ini:", antrian)

# Mengambil elemen teratas dari antrian
elemen_teratas = antrian.pop(0)

print("Elemen teratas yang diambil:", elemen_teratas)
print("Antrian saat ini:", antrian)
#output
# Antrian saat ini: ['apel', 'jeruk', 'mangga']
# Elemen teratas yang diambil: apel
# Antrian saat ini: ['jeruk', 'mangga']

# List comprehension adalah sebuah cara untuk membuat list secara lebih singkat dan efisien dalam Python. Dalam list comprehension, sebuah list dapat dibuat dengan cara mengambil nilai dari list yang ada dan melakukan operasi pada nilai tersebut untuk menghasilkan nilai baru.

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9]
kuadrat = [x ** 2 for x in angka]
print(kuadrat)#[1, 4, 9, 16, 25, 36, 49, 64, 81]


# Nested List Comprehensions adalah konstruksi dalam Python yang memungkinkan kita untuk membuat list secara lebih mudah dan efisien. Nested List Comprehensions memungkinkan kita untuk memasukkan satu atau lebih pernyataan for ke dalam list comprehension lain.

a = [[1, 2], [3, 4], [5, 6]]
flattened = [num for sublist in a for num in sublist]
print(flattened)
#[1, 2, 3, 4, 5, 6]

a = [1, 2, 3]
b = [4, 5, 6]
product = [i * j for i in a for j in b]
print(product)
#[4, 5, 6, 8, 10, 12, 12, 15, 18]

# Del statement adalah sebuah perintah dalam Python yang digunakan untuk menghapus variabel, objek, atau elemen dari sebuah list. Del statement bekerja dengan menghapus referensi dari variabel tersebut ke objek yang ditunjuk, sehingga objek tersebut tidak lagi bisa diakses atau digunakan.
x = 5
del x
print(x) # akan muncul NameError karena x sudah dihapus

my_list = [1, 2, 3, 4, 5]
del my_list[2] # menghapus elemen dengan index 2 (nilai 3)
print(my_list) # output: [1, 2, 4, 5]

class MyClass:
    def __init__(self, name):
        self.name = name

obj1 = MyClass("Object 1")
obj2 = MyClass("Object 2")

del obj1 # menghapus objek obj1
print(obj1) # akan muncul NameError karena obj1 sudah dihapus
# Penting untuk diingat bahwa penggunaan del statement harus dilakukan dengan hati-hati karena objek atau variabel yang dihapus tidak dapat dipulihkan. Selain itu, penghapusan objek tidak selalu berarti membebaskan memori secara otomatis, karena Python memiliki garbage collector yang mengatur pengelolaan memori secara otomatis.


