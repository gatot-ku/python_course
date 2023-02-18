# Set dalam Python sangat berguna untuk menyimpan elemen yang unik dan dapat digunakan dalam berbagai macam situasi, seperti untuk menghapus elemen yang duplikat, menghitung elemen yang berbeda dalam suatu kumpulan data, atau untuk mengecek apakah dua kumpulan data memiliki elemen yang sama.

# Set adalah salah satu tipe data bawaan (built-in) dalam Python dan dapat dibuat dengan menggunakan kurung kurawal {} atau fungsi set()

fruits = {'apple', 'banana', 'orange'}
print(fruits)  # Output: {'banana', 'orange', 'apple'}

fruits.add('grape')
print(fruits)  # Output: {'banana', 'orange', 'apple', 'grape'}

#union ets
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.union(set2)
print(set3)  # Output: {1, 2, 3, 4}

#intersection/persimpangan
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.intersection(set2)
print(set3)  # Output: {2, 3}

#difference/perbedaan
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.difference(set2)
print(set3)  # Output: {1}

# set() adalah tipe data koleksi di Python yang digunakan untuk menyimpan kumpulan elemen yang tidak terurut dan unik. Setiap elemen dalam set harus unik, yang berarti tidak dapat ada duplikat. Set juga dapat digunakan untuk melakukan operasi matematika seperti gabungan, irisan, dan selisih.