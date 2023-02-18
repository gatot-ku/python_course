# Menggunakan lambda expression untuk mengalikan setiap elemen dari sebuah list dengan 2:
from functools import reduce #baris ini untuk pemanggilan reduce


my_list = [1, 2, 3, 4, 5]
new_list = list(map(lambda x: x * 2, my_list))
print(new_list) # output: [2, 4, 6, 8, 10]


# Menggunakan lambda expression untuk mengurutkan sebuah list of tuples berdasarkan elemen kedua dari tiap tuple:
my_list = [('apple', 2), ('banana', 1), ('orange', 3)]
new_list = sorted(my_list, key=lambda x: x[1])
print(new_list) # output: [('banana', 1), ('apple', 2), ('orange', 3)]

# Menggunakan lambda expression untuk mencari nilai maksimum dari sebuah list of integers:
my_list = [1, 6, 3, 9, 2]
max_val = reduce(lambda x, y: x if x > y else y, my_list)
print(max_val) # output: 9
