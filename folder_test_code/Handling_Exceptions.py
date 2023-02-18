# try:
#     # Potongan kode yang mungkin menimbulkan pengecualian
#     x = int(input("Masukkan sebuah angka: "))
#     y = 10 / x
#     print("Hasil pembagian: ", y)
# except ZeroDivisionError:
#     # Menangani pengecualian jika terjadi pembagian dengan nol
#     print("Tidak bisa melakukan pembagian dengan nol")
# except ValueError:
#     # Menangani pengecualian jika pengguna memasukkan nilai yang tidak valid
#     print("Harus memasukkan angka")
# finally:
#     # Menjalankan kode di blok finally terlepas dari apakah pengecualian terjadi atau tidak
    
#     print("Terima kasih sudah menggunakan program ini")
# #--------------

# while True:
#     try:
#         x = int(input("Masukkan sebuah angka: "))
#         if x < 10:
#             raise ValueError("Input harus lebih besar dari 10.")
#     except ValueError as e:
#         print(e)
#     else:
#         for i in range(x):
#             print("Perulangan ke-", i+1)
#         break

class DivideByZeroError(Exception):
    pass

class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            raise DivideByZeroError("Cannot divide by zero")
        return result

calc = Calculator()

try:
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    print(calc.add(x, y))
    print(calc.subtract(x, y))
    print(calc.multiply(x, y))
    print(calc.divide(x, y))
except ValueError:
    print("Invalid input")
except DivideByZeroError as e:
    print(e)
