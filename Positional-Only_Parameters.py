# Positional-Only Parameters adalah jenis parameter di Python 3.8 atau yang lebih baru, yang memungkinkan kita untuk membatasi parameter yang dapat diteruskan sebagai posisi tanpa harus menempatkannya sebagai argumen kata kunci.

# Secara umum, pada fungsi Python, kita dapat memasukkan argumen sebagai posisi atau sebagai argumen kata kunci. Namun, dengan Positional-Only Parameters, parameter-parameter tersebut hanya dapat diteruskan sebagai posisi saja dan tidak dapat diisi dengan argumen kata kunci.

#def function_name(positional_only_parameter, /, positional_or_keyword_parameter, *, keyword_only_parameter):
    # code

# Perhatikan bahwa garis miring tunggal (/) digunakan untuk memisahkan parameter-posisi yang hanya dapat diteruskan sebagai posisi dari parameter-posisi atau parameter-kata kunci lainnya. Sedangkan tanda bintang (*) digunakan untuk memisahkan parameter kata kunci saja dari parameter-posisi atau parameter kata kunci yang lain.

def greet(name, /, greeting, *, punct='.'):
    return f"{greeting} {name}{punct}"

print(greet("John", "Hello")) # Output: Hello John.
print(greet("John", "Hello", punct='!')) # Output: Hello John!
print(greet(name="John", greeting="Hello")) # TypeError: greet() got some positional-only arguments passed as keyword arguments: 'name'

# Dalam contoh di atas, kita memiliki fungsi greet() yang memiliki 3 parameter, yaitu name, greeting, dan punct. Namun, kita menggunakan garis miring tunggal (/) untuk membatasi name agar hanya dapat diteruskan sebagai posisi saja. Artinya, kita hanya bisa memanggil fungsi dengan cara greet("John", "Hello"), bukan dengan greet(name="John", greeting="Hello"). Ini akan menghasilkan TypeError, karena name adalah Parameter-Only yang hanya dapat diteruskan sebagai posisi saja.