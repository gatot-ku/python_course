# Dalam Python, klausa "else" pada loop memberikan aksi yang akan dilakukan setelah loop selesai dijalankan. Klausa "else" akan dijalankan jika dan hanya jika loop tidak dihentikan menggunakan pernyataan "break".

# Berikut adalah contoh penggunaan klausa "else" pada loop:
# Looping untuk mencari bilangan prima
for num in range(2, 10):
    for i in range(2, num):
        if num % i == 0:
            print(num, 'bukan bilangan prima')
            break
    else:
        print(num, 'adalah bilangan prima')
#2 adalah bilangan prima
# 3 adalah bilangan prima
# 4 bukan bilangan prima
# 5 adalah bilangan prima
# 6 bukan bilangan prima
# 7 adalah bilangan prima
# 8 bukan bilangan prima
# 9 bukan bilangan prima

# Sedangkan, klausa "else" pada loop while digunakan untuk mengeksekusi blok kode ketika kondisi while menjadi False.

# Berikut adalah contoh penggunaan klausa "else" pada loop while:
# Looping untuk mencari nilai x yang memenuhi persamaan 2x = 64
x = 1
while 2*x != 64:
    x += 1
else:
    print("Nilai x yang memenuhi persamaan adalah", x)
 #Nilai x yang memenuhi persamaan adalah 32
   
