try:
    # Potongan kode yang mungkin menimbulkan pengecualian
    x = int(input("Masukkan sebuah angka: "))
    y = 10 / x
    print("Hasil pembagian: ", y)
except ZeroDivisionError:
    # Menangani pengecualian jika terjadi pembagian dengan nol
    print("Tidak bisa melakukan pembagian dengan nol")
except ValueError:
    # Menangani pengecualian jika pengguna memasukkan nilai yang tidak valid
    print("Harus memasukkan angka")
finally:
    # Menjalankan kode di blok finally terlepas dari apakah pengecualian terjadi atau tidak
    print("Terima kasih sudah menggunakan program ini")



#-----------------------
while True:
    try:
        x = int(input("Masukkan sebuah angka: "))
        if x < 10:
            raise ValueError("Input harus lebih besar dari 10.")
    except ValueError as e:
        print(e)
    else:
        for i in range(x):
            print("Perulangan ke-", i+1)
        break
#-------------
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


#----------
try:
    a = int(input("Masukkan angka pertama: "))
    b = int(input("Masukkan angka kedua: "))
    c = a / b
    print(c)
except ValueError:
    print("Input yang dimasukkan harus berupa bilangan bulat.")
except ZeroDivisionError:
    print("Tidak dapat membagi dengan nol.")
except:
    print("Terjadi kesalahan yang tidak diketahui.")
#Dalam contoh di atas, blok try mencoba menjalankan tiga baris kode dan mengantisipasi kemungkinan exception. Jika terjadi exception, maka blok except yang cocok akan menangani exception tersebut. Blok except terakhir dengan tanda except: digunakan untuk menangani exception yang tidak diketahui.

#-----------
while True:
    try:
        nilai = int(input("Masukkan nilai: "))
        if nilai < 0:
            raise ValueError("Nilai tidak boleh negatif")
        elif nilai == 0:
            print("Nilai nol")
        else:
            print("Nilai positif")
            break
    except ValueError as err:
        err.args += ("Pastikan nilai yang dimasukkan positif",)
        print(err)
# Dalam contoh kode di atas, program akan terus meminta inputan dari pengguna menggunakan loop while hingga nilai yang dimasukkan positif. Jika nilai negatif, program akan membangkitkan sebuah ValueError dan mencetak pesan error yang lebih spesifik. Jika nilai nol, program akan mencetak "Nilai nol". Jika nilai positif, program akan mencetak "Nilai positif" dan keluar dari loop dengan menggunakan break.

# Dalam hal ini, Enriching Exceptions with Notes sangat berguna karena pesan error yang ditambahkan memberikan petunjuk yang jelas untuk pengguna untuk memperbaiki kesalahan dengan lebih mudah, yaitu "Pastikan nilai yang dimasukkan positif". Selain itu, pengguna juga mendapatkan umpan balik yang berguna tentang nilai yang dimasukkan seperti "Nilai nol" atau "Nilai positif" yang ditampilkan di layar.        