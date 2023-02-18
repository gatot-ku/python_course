# pengguna untuk menambahkan metadata ke dalam definisi fungsi. Metadata tersebut berisi informasi tentang tipe data parameter dan nilai kembalian dari fungsi
def add_numbers(a: int, b: int) -> int:
    """
    Fungsi ini menerima dua parameter bilangan bulat (a dan b) dan mengembalikan hasil penjumlahannya.
    """
    return a + b

def greet(name: str = "World") -> str:
    """
    Fungsi ini menerima satu parameter string (name) dan mengembalikan string sapaan.
    Jika parameter name tidak diberikan, maka nilai defaultnya adalah "World".
    """
    return f"Hello, {name}!"
