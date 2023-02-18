# 1. Inheritance
# Inheritance atau pewarisan adalah salah satu konsep utama dalam pemrograman berorientasi objek di Python. Dengan inheritance, sebuah class dapat mewarisi atribut dan method dari class lainnya, sehingga memudahkan dalam pengelolaan kode dan mengurangi pengulangan kode. Contohnya, sebuah class User dapat mewarisi atribut dan method dari class Person, sehingga tidak perlu membuat ulang atribut dan method yang sama pada kedua class tersebut.

# 2. Abstract Class
# Abstract class adalah class yang tidak dapat di-instantiate atau tidak dapat membuat objek langsung, tetapi hanya dapat diwarisi oleh class lainnya. Abstract class biasanya digunakan untuk membuat kerangka atau template yang digunakan oleh class-class turunan. Abstract class dapat diimplementasikan menggunakan modul abc (Abstract Base Class) di Python.

# 3. Property
# Property adalah cara untuk mengakses dan memodifikasi nilai dari atribut class dengan menggunakan method. Property dapat memungkinkan penggunaan method yang tersembunyi untuk memvalidasi, mengubah, atau mengekstrak nilai dari atribut. Contohnya, sebuah class Product memiliki atribut price yang memiliki validasi tertentu sebelum diubah atau diakses.

# 4. Decorators
# Decorators adalah fitur Python yang dapat digunakan untuk menambahkan fungsionalitas tambahan pada method atau function tanpa mengubah kode asli. Decorator dapat digunakan untuk berbagai tujuan seperti memeriksa autentikasi pengguna sebelum memanggil sebuah method, mencatat waktu pemanggilan suatu method, atau membatasi jumlah pemanggilan pada sebuah method.

# 5. Magic Methods
# Magic methods adalah method bawaan di Python yang memiliki nama khusus yang diawali dan diakhiri dengan double underscore (dunder). Magic methods dapat digunakan untuk membuat class lebih dinamis dan fleksibel dengan memungkinkan implementasi operasi matematika, pembandingan, konversi tipe data, dan lain-lain pada objek class. Beberapa contoh magic methods yang sering digunakan pada pengembangan web adalah __str__, __repr__, __eq__, __lt__, __gt__, dan __len__.

# contoh
# __str__ adalah method bawaan di Python yang digunakan untuk mengembalikan string yang merepresentasikan objek class. Method ini dapat digunakan untuk mencetak informasi objek secara lebih mudah dan rapi.
import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

p = Person("John", 30)
print(p)#Person(name=John, age=30)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = datetime.date.today().year - birth_year
        return cls(name, age)

c = Person.from_birth_year("John", 1992)
print(c.name)#jhon
print(c.age)#31 hasil 31 karena ada operator matematika

# __slots__ adalah attribute di Python yang digunakan untuk membatasi atribut yang dapat ditambahkan pada objek class. Attribute ini dapat digunakan untuk meningkatkan kinerja aplikasi dengan mengurangi penggunaan memori. Berikut adalah contoh penggunaan __slots__ attribute:

class Person:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", 30)
print(p.name)
print(p.age)

p.address = "Street 123"  # AttributeError: 'Person' object has no attribute 'address' (karena objek Person tidak memiliki atribut address dan tidak dapat menambahkan atribut tersebut)

# sebenarnya masih banyak lagi odds lainya


