def add_numbers(x, y):
    return x + y

result = add_numbers(x=5, y=7)
print(result)


# Default argument values adalah fitur dalam bahasa pemrograman Python yang memungkinkan pengguna untuk menentukan nilai default untuk parameter yang tidak perlu diisi saat pemanggilan fungsi
def greeting(name, message="Hello"):
    print(message, name)

greeting("Alice") # Output: Hello Alice
greeting("Bob", "Hi") # Output: Hi Bob

# Keyword Arguments
def print_user_data(name, age, city):
    print(f"Nama: {name}")
    print(f"Umur: {age}")
    print(f"Kota: {city}")

# Cara penggunaan dengan keyword arguments
print_user_data(name="John", age=25, city="Jakarta")

# Output:
# Nama: John
# Umur: 25
# Kota: Jakarta
