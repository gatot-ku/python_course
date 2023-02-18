# Keyword-Only Arguments adalah parameter pada fungsi Python yang hanya dapat diisi dengan menggunakan kata kunci atau keyword. Ini berarti bahwa kita tidak dapat memberikan nilai ke parameter tersebut secara posisi seperti pada parameter biasa, melainkan harus menentukan nama parameter saat memanggil fungsi.

# Berikut ini adalah contoh sederhana untuk menggunakan Keyword-Only Arguments di Python:
def display_info(name, *, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

# Memanggil fungsi display_info dengan Keyword-Only Arguments
# display_info("John", age=30)
# Pada contoh di atas, parameter name adalah parameter biasa yang bisa diisi dengan nilai secara posisi saat memanggil fungsi, sedangkan parameter age ditandai dengan tanda bintang tunggal (*) di depannya. Ini menunjukkan bahwa parameter age hanya dapat diisi dengan menggunakan kata kunci saat memanggil fungsi, seperti age=30.