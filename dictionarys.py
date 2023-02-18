# Membuat dictionary kosong
my_dict = {}

# Membuat dictionary dengan beberapa pasangan key-value
my_dict = {'nama': 'Andi', 'usia': 25, 'alamat': 'Jakarta'}

# Mengakses nilai dengan key 'nama'
print(my_dict['nama'])  # Output: Andi

# Mengakses nilai dengan key 'usia'
print(my_dict['usia'])  # Output: 25

# Menambahkan pasangan key-value baru
my_dict['pekerjaan'] = 'Programmer'

# Mengubah nilai yang terkait dengan key 'usia'
my_dict['usia'] = 26

# Melihat isi dictionary setelah ditambahkan dan diubah
print(my_dict)  # Output: {'nama': 'Andi', 'usia': 26, 'alamat': 'Jakarta', 'pekerjaan': 'Programmer'}

# Menghapus pasangan key-value dengan key 'alamat'
del my_dict['alamat']

# Melihat isi dictionary setelah dihapus
print(my_dict)  # Output: {'nama': 'Andi', 'usia': 26, 'pekerjaan': 'Programmer'}

# Mengembalikan daftar key dalam dictionary
print(my_dict.keys())  # Output: ['nama', 'usia', 'pekerjaan']

# Mengembalikan daftar value dalam dictionary
print(my_dict.values())  # Output: ['Andi', 26, 'Programmer']

# Mengembalikan daftar pasangan key-value dalam dictionary
print(my_dict.items())  # Output: [('nama', 'Andi'), ('usia', 26), ('pekerjaan', 'Programmer')]
#catatan method di dictionary keys values item