# Di Python, ada dua jenis objek yaitu sequence dan non-sequence. Sequence adalah jenis objek yang terdiri dari urutan nilai atau elemen, seperti string, list, tuple, dan range. Sedangkan non-sequence adalah jenis objek yang tidak terdiri dari urutan nilai atau elemen, seperti set, dictionary, dan boolean.

# Ketika membandingkan objek di Python, ada beberapa hal yang perlu diperhatikan tergantung pada jenis objek tersebut. Untuk membandingkan objek sequence, kita dapat menggunakan operator perbandingan seperti ==, !=, <, >, <=, dan >=. Saat menggunakan operator perbandingan ini, urutan elemen dari sequence diperhatikan.


# contoh membandingkan sequence di Python:
# Membandingkan dua string
string1 = 'hello'
string2 = 'world'
print(string1 == string2) # False
print(string1 < string2)  # True

# Membandingkan dua list
list1 = [1, 2, 3]
list2 = [3, 2, 1]
print(list1 == list2)    # False
print(list1 < list2)     # True

# Membandingkan dua tuple
tuple1 = (1, 2, 3)
tuple2 = (3, 2, 1)
print(tuple1 == tuple2)  # False
print(tuple1 < tuple2)   # True

# Membandingkan range dengan tuple
range1 = range(5)
tuple1 = (0, 1, 2, 3, 4)
print(range1 == tuple1)  # True
print(range1 < tuple1)   # False



# Sedangkan untuk membandingkan objek non-sequence, kita harus menggunakan metode khusus yang tersedia untuk jenis objek tersebut. Misalnya, untuk membandingkan dua set, kita dapat menggunakan metode issubset() dan issuperset(). Sedangkan untuk membandingkan dua dictionary, kita dapat membandingkan nilai dari kunci yang sama di antara keduanya.
# contoh membandingkan objek non-sequence di Python:
# Membandingkan dua set
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.issubset(set2))    # False
print(set1.issuperset(set2))  # False

# Membandingkan dua dictionary
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 3, 'c': 2}
print(dict1 == dict2)    # False
print(dict1['a'] == dict2['a'])  # True
