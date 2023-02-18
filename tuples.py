# membuat Tuple dengan tanda kurung ()
my_tuple = (1, 2, 3, "empat", "lima")

# membuat Tuple dengan fungsi tuple()
my_tuple2 = tuple(["satu", "dua", "tiga", 4, 5])

# mengakses nilai pada Tuple
print(my_tuple[0]) # output: 1
print(my_tuple[3]) # output: "empat"

# mengubah nilai pada Tuple
# ini akan menghasilkan TypeError karena Tuple tidak dapat diubah
my_tuple[0] = 10

# menghapus Tuple
del my_tuple


# membuat Tuple baru dengan nilai tambahan
my_tuple_new = my_tuple + ("enam", "tujuh")
print(my_tuple_new) # output: (1, 2, 3, "empat", "lima", "enam", "tujuh")

# membuat Tuple sebagai key pada dictionary
my_dict = {('John', 25): 'Male', ('Jane', 30): 'Female'}

# mengakses nilai pada dictionary dengan menggunakan Tuple sebagai key
print(my_dict[('John', 25)]) # output: 'Male'
print(my_dict[('Jane', 30)]) # output: 'Female'

# menambahkan nilai pada dictionary dengan menggunakan Tuple sebagai key
my_dict[('Jack', 35)] = 'Male'
print(my_dict) # output: {('John', 25): 'Male', ('Jane', 30): 'Female', ('Jack', 35): 'Male'}
# Perlu diingat bahwa Tuple sebagai key pada dictionary harus bersifat immutable, karena jika nilai pada key dapat diubah, maka dictionary tidak dapat memastikan konsistensi nilai pada key.

# Kelebihan dan Kekurangan Tuple
# Kelebihan:

# Immutable, sehingga data pada Tuple tidak bisa diubah
# Lebih efisien daripada List untuk data yang besar
# Dapat digunakan sebagai key pada dictionary
# Kekurangan:

# Tidak dapat diubah, sehingga sulit untuk memodifikasi nilai pada Tuple
# Tidak bisa menambahkan nilai pada Tuple


