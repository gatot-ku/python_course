# Di Python, scope merujuk pada wilayah di mana sebuah variabel dapat diakses. Python memiliki beberapa jenis scope, termasuk scope lokal, scope global, dan scope built-in.

# Setiap fungsi, metode, atau kelas di Python memiliki namespace-nya sendiri. Namespace adalah daftar variabel yang terkait dengan objek tertentu, seperti fungsi atau kelas. Ketika Anda memanggil suatu variabel di dalam sebuah fungsi atau kelas, Python akan mencari variabel tersebut terlebih dahulu di dalam namespace lokal, kemudian di dalam namespace global, dan akhirnya di dalam namespace built-in.

# Ketika sebuah variabel didefinisikan di dalam sebuah kelas di Python, variabel tersebut menjadi bagian dari namespace kelas. Ini berarti bahwa variabel tersebut dapat diakses oleh metode yang terkait dengan kelas, tetapi tidak dapat diakses di luar kelas itu sendiri. Namun, jika variabel tersebut didefinisikan sebagai variabel kelas (dengan menambahkan dekorator @classmethod atau @staticmethod), maka variabel tersebut dapat diakses langsung oleh kelas itu sendiri.

class MyClass:
    # Variabel kelas
    class_var = 10

    def __init__(self, arg1):
        # Variabel instance
        self.instance_var = arg1

    def my_method(self):
        # Variabel lokal
        local_var = 5
        print("local_var:", local_var)
        print("instance_var:", self.instance_var)
        print("class_var:", MyClass.class_var)

    @classmethod
    def my_classmethod(cls):
        # Variabel kelas
        print("class_var:", cls.class_var)

# Membuat objek dari kelas MyClass
obj = MyClass(20)

# Memanggil metode my_method() dari objek
obj.my_method()
# Output: local_var: 5
#         instance_var: 20
#         class_var: 10

# Memanggil metode my_classmethod() dari kelas
MyClass.my_classmethod()
# Output: class_var: 10


# Pada contoh di atas, kelas MyClass memiliki tiga jenis variabel: variabel kelas (class_var), variabel instance (instance_var), dan variabel lokal (local_var). Variabel kelas dapat diakses baik oleh metode my_method() maupun my_classmethod(), sedangkan variabel instance hanya dapat diakses oleh metode my_method(). Variabel lokal hanya dapat diakses di dalam fungsi atau metode di mana ia didefinisikan.