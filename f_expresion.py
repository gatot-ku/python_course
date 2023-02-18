# new_list = [expression for item in iterable if condition]

# Keterangan:

# expression: merupakan ekspresi Python yang diterapkan pada setiap elemen dari objek iterable.
# item: merupakan variabel sementara yang merepresentasikan setiap elemen dalam objek iterable.
# iterable: merupakan objek yang akan diiterasi (seperti list, tuple, set, atau string).
# if condition: merupakan kondisi opsional yang menentukan apakah suatu elemen harus dimasukkan ke dalam list baru. Jika kondisi tidak terpenuhi, maka elemen tersebut tidak akan dimasukkan ke dalam list.
# Contoh penggunaan fungsi komprehensi:

numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)

# Pada contoh di atas, kita membuat sebuah list baru squares yang berisi hasil kuadrat dari setiap elemen dalam list numbers. Dengan menggunakan fungsi komprehensi, kita dapat membuat list squares dengan lebih efisien daripada menggunakan perulangan for biasa.

# Fungsi komprehensi juga dapat digunakan untuk melakukan operasi seperti filter, map, dan reduce. Misalnya, untuk membuat list baru yang berisi hanya bilangan genap dari list numbers, kita dapat menambahkan kondisi if pada fungsi komprehensi seperti berikut:

even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)