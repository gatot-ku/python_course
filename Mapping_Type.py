# Dictionary (dict): Tipe data ini digunakan untuk merepresentasikan pasangan kunci-nilai yang tidak terurut dan unik. Kunci (key) digunakan untuk mengakses nilai (value) yang terkait. Contohnya:

person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"]) # Output: "John"

from collections import defaultdict
person = defaultdict(str)
person["name"] = "John"
person["age"] = 30
person["city"] = "New York"
print(person["hobby"]) # Output: ""


from collections import OrderedDict
person = OrderedDict()
person["name"] = "John"
person["age"] = 30
person["city"] = "New York"
for key, value in person.items():
    print(key, value)
# Output: name John
#         age 30
#         city New York

from collections import Counter
text = "hello world"
count = Counter(text)
print(count)
# Output: Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
