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