# Definisi string
string1 = 'Hello, World!'
string2 = "Ini juga string"

# Menggabungkan dua string
string3 = string1 + ' ' + string2
print(string3) # Output: Hello, World! Ini juga string

# Menampilkan karakter pada indeks tertentu
print(string1[1]) # Output: e

# Slicing string
print(string1[0:5]) # Output: Hello

# Menentukan panjang string
print(len(string2)) # Output: 13

# Mengubah huruf besar-kecil pada string
string4 = 'CONTOH string KAPITAL'
print(string4.lower()) # Output: contoh string kapital
print(string4.upper()) # Output: CONTOH STRING KAPITAL

# Mencari karakter tertentu pada string
print(string1.find('W')) # Output: 7

# Mengganti karakter pada string
string5 = 'Ini kalimat lama'
string6 = string5.replace('lama', 'baru')
print(string6) # Output: Ini kalimat baru

# Contoh penggunaan character escape sequence
print('Ini adalah tanda kutip tunggal: \'')
print('Ini adalah tanda kutip ganda: \"')
print('Ini adalah backslash: \\')
print('Ini adalah tab: \t')

#split join strip
# Contoh penggunaan built-in methods pada string
string7 = 'Ini adalah contoh string untuk split'
list_string = string7.split(' ')
print(list_string) # Output: ['Ini', 'adalah', 'contoh', 'string', 'untuk', 'split']

string8 = '-'.join(list_string)
print(string8) # Output: Ini-adalah-contoh-string-untuk-split

string9 = '   ini string dengan spasi di awal dan akhir   '
string10 = string9.strip()
print(string10) # Output: ini string dengan spasi di awal dan akhir

#fancy output formatting

name = "John"
age = 25
print("My name is {0} and I'm {1} years old.".format(name, age))
#My name is John and I'm 25 years old.

name = "John"
age = 25
print(f"My name is {name} and I'm {age} years old.")
#My name is John and I'm 25 years old.

name = "John"
age = 25
print(f"{name=} {age=}")
#name='John' age=25

# Python juga memiliki beberapa built-in function yang dapat digunakan untuk memformat tampilan output. Misalnya, str.ljust(), str.rjust(), dan str.center() untuk meletakkan teks pada posisi tertentu, str.upper() dan str.lower() untuk mengubah teks menjadi huruf kapital atau huruf kecil, str.capitalize() untuk membuat huruf pertama dalam kalimat menjadi kapital, dan lain-lain.