# Generator adalah fungsi khusus di Python yang menghasilkan serangkaian nilai saat diiterasi. Generator memungkinkan Anda menghasilkan nilai secara bertahap, satu per satu, dan menyimpan kondisi antara setiap pemanggilan fungsi.

# Saat generator digunakan dalam kelas, generator biasanya didefinisikan sebagai metode kelas, dan menggunakan sintaks yield untuk menghasilkan nilai.

class MyGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def generate_numbers(self):
        for i in range(self.start, self.end):
            yield i

# menggunakan generator yang didefinisikan dalam kelas
generator = MyGenerator(1, 6)
for number in generator.generate_numbers():
    print(number)#1,2,3,4,5

# Perlu diingat bahwa generator memungkinkan kita untuk menghasilkan serangkaian nilai secara bertahap dan menangani setiap nilai satu per satu, yang membuatnya sangat berguna dalam situasi di mana kita hanya ingin menghasilkan nilai pada saat dibutuhkan, daripada menghasilkan semua nilai sekaligus.

#-------------------------------------------------
class MySequence:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return (x for x in range(self.start, self.end))

seq = MySequence(0, 5)
for num in seq:
    print(num)#0,1,2,3,4,

# Generator expression adalah cara yang efisien dan ringkas untuk membuat generator, yaitu objek yang menghasilkan serangkaian nilai pada saat diperlukan. Generator expression dapat digunakan di dalam kelas Python untuk menghasilkan serangkaian nilai yang dihasilkan secara dinamis, dengan memanfaatkan sintaksis yang mudah digunakan dan fleksibel.


