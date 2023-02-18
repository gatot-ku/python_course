# Dalam Python, Magic Method (atau disebut juga Special Method) adalah metode khusus di dalam sebuah class yang diawali dan diakhiri dengan dua underscore (__). Magic methods memungkinkan programmer untuk mendefinisikan perilaku khusus dari sebuah class dan objek yang terkait dengan berbagai operasi seperti pemanggilan fungsi, operator aritmatika, pemanggilan fungsi built-in, akses ke atribut, dan sebagainya.

# Berikut ini adalah beberapa contoh dari magic methods yang sering digunakan di dalam Python:

# init(): Magic method yang digunakan untuk menginisialisasi objek. Method ini dipanggil saat objek dibuat dan dapat digunakan untuk menentukan nilai awal dari atribut objek.

# str(): Magic method yang digunakan untuk mengonversi objek ke dalam string. Method ini dipanggil ketika objek diwakili sebagai string, seperti ketika objek dicetak ke konsol.

# repr(): Magic method yang digunakan untuk mengonversi objek ke dalam string representasi formal. Method ini dipanggil ketika objek diwakili sebagai string oleh fungsi built-in repr().

# len(): Magic method yang digunakan untuk mengembalikan panjang objek. Method ini dipanggil saat len() dipanggil pada objek.

# add(): Magic method yang digunakan untuk menentukan perilaku saat operator + digunakan pada objek.

# sub(): Magic method yang digunakan untuk menentukan perilaku saat operator - digunakan pada objek.

# eq(): Magic method yang digunakan untuk menentukan perilaku saat operator == digunakan pada objek.

# lt(): Magic method yang digunakan untuk menentukan perilaku saat operator < digunakan pada objek.

# gt(): Magic method yang digunakan untuk menentukan perilaku saat operator > digunakan pada objek.

# getattr(): Magic method yang digunakan untuk menangani akses ke atribut yang tidak didefinisikan pada objek.

# Itu adalah beberapa contoh dari magic methods yang sering digunakan di dalam Python. Dengan menggunakan magic methods, programmer dapat menentukan perilaku yang khusus dan kompleks dari sebuah class dan objek di dalam Python.