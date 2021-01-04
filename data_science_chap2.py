import re
from collections import Counter
from collections import defaultdict
string_with_special_chars = r"\t"
print(string_with_special_chars)

multiline = """pierwsza linia
druga linia
trzecia linia"""
print(multiline)


def var_lambda_function(a): return a * 2


def just_print(me):
    return me


def lazy_function(delegate=just_print):
    return delegate(2)


# print(lazy_function(delegate=var_lambda_function))
# print(lazy_function())

str1 = "pierwszy napis"
str2 = "drugi napis"
print("{0} {1}".format(str1, str2))
print(f"laczenie znakow: {str1}: {str2}")

try:
    2 / 0
except ZeroDivisionError:
    print("""nigdy cholero nie dziel przez zero""")

integer_list = [1, 2, 3, 4, 5, 6]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]
list_length = len(integer_list)  # równa się 3
list_sum = sum(integer_list)  # równa się 6

print(sum(integer_list))
print(f"przedostatni: {str(integer_list[-2])}")
print(f"without first and last: {integer_list[1:-1]}")

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
first_three = x[:3]  # [-1, 1, 2]
three_to_end = x[3:]  # [3, 4, ..., 9]
one_to_four = x[1:5]  # [1, 2, 3, 4]
last_three = x[-3:]  # [7, 8, 9]
without_first_and_last = x[1:-1]  # [1, 2, ..., 8]
copy_of_x = x[:]  # [-1, 1, 2, ..., 9]

every_tird = x[::3]  # [0, 3, 6, 9]
print(every_tird)
five_to_three = x[5:2:-1]  # [5, 4, 3]
print(five_to_three)

print(f"1 in [1, 2, 3]: {1 in [1, 2, 3]}")  # prawda (True)
print(f"0 in [1, 2, 3]: {0 in [1, 2, 3]}")  # fałsz (False)

# rozpakowywanie kolekcji
x, y = [1, 2]  # teraz x jest równe 1, a y jest równe 2


def sum_and_product(x, y):
    return (x + y), (x * y)


print(sum_and_product(2, 3))
s, p = sum_and_product(5, 10)
print(f"s: {s}, p: {p}")

x, y, z = 1, 2, 3  # Teraz x jest równe 1, a y jest równe 2.
# x, y, z = (1, 2, 3) # Teraz x jest równe 1, a y jest równe 2.
# Pythonowy sposób zamiany wartości zmiennych; teraz x jest równe 2, a y jest równe 1.
x, y = y, x
print(f"x: {x}, y: {y}, z: {z}")

keyToList = defaultdict(list)
assert keyToList["key1"] == [], "not empty list"

# counter
counted = Counter([1, 1, 5, 6, 5, 6, 7])
print(counted.most_common(2))

# logic and sets
x = None
safe_x = x if x is not None else 0
assert safe_x == 0, "logic has worked"

# skladanie list
even_numbers = {x for x in range(10) if x % 2 == 0}
print(even_numbers)


class Counter:
    def __init__(self, count=0):
        self.count = count

    def __repr__(self):
        return f"Counter {self.count}"

    def reset(self):
        self.count = 0

    def readCount(self):
        return self.count

    def increase(self, count: int = 1):
        self.count += count


counter = Counter()
counter.increase()
counter.increase(2)
assert counter.readCount() == 3, "not equal"
counter.reset()
counter.increase()
assert counter.readCount() == 1, "expected 1"
print(counter)


# yield i generatory
def generate_even(limit: int):
    for i in range(limit):
        if(i % 2 != 0):
            yield i


even_up_to_10 = [x for x in generate_even(10)]
print(f"generated even numbers up to 10: {even_up_to_10}")

assert {1, 2} == {2, 1}

# regex
assert all([
    re.search("kot", "ma kota"),
    re.match("^ma ko[a-z]+", "ma kota")
])

# zip
list1 = ['a', 'b', 'c']
list2 = range(3)
zipped = [x for x in zip(list1, list2)]
print(f"zipped {zipped}")
unzipped = [x for x in zip(*zipped)]
# unzipped = [x for x in zip((1,2), (3,4), (5,6), (7,8))]
print(f"unzipped {unzipped}")

# argumenty nazwane i nienazwane


def magic(*args, **argumenty_nazwane):
    print("argumenty nienazwane:", args)
    print("argumenty nazwane:", argumenty_nazwane)


magic(1, 2, key="word", key2="word2")

tuple1 = 3, 4
print(f"tuple1: {tuple1}")
tupleAsList = [*tuple1]
print(f"tupleAsList{tupleAsList}")
