#1 *args: digunakan untuk menangani sejumlah argumen tanpa batas yang diteruskan ke sebuah fungsi. Args akan mewakili tuple dari semua argumen yang diteruskan ke fungsi tersebut.
#biasanya juga di sebut Arbitrary Argument Lists
# Berikut contoh penggunaannya:

def print_args(*args):
    for arg in args:
        print(arg)
        
print_args(1, 2, 3, 4)
# output: 
# 1
# 2
# 3
# 4

#2 **kwargs: digunakan untuk menangani sejumlah keyword arguments (argumen yang diberi nama) tanpa batas yang diteruskan ke sebuah fungsi. Kwargs akan mewakili dictionary dari semua keyword arguments yang diteruskan ke fungsi tersebut. 
#biasa juga di sebut Unpacking Argument Lists
# Berikut contoh penggunaannya:

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_kwargs(name="John", age=30, city="New York")
# output:
# name: John
# age: 30
# city: New York


#3 *args dan **kwargs: digunakan untuk menangani sejumlah argumen tanpa batas dan keyword arguments tanpa batas yang diteruskan ke sebuah fungsi secara bersamaan. Berikut contoh penggunaannya:

def print_args_kwargs(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_args_kwargs(1, 2, 3, name="John", age=30, city="New York")
# output:
# 1
# 2
# 3
# name: John
# age: 30
# city: New York
