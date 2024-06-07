#1
def describe_person(name, age = 0):return f"{name} is {age} years old."

print(describe_person("Alice", 30))
print(describe_person("Bob"))        

#2
def divide(x, y): return x/y if y != 0 else "Cannot divide by zero"

result = divide(10, 2)
print(result)  # 출력: 5.0

result = divide(10, 0)
print(result)  # 출력: Cannot divide by zero

#3
def divide(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Cannot divide by zero"
result = divide(10, 2)
print(result)  # 출력: 5.0
result = divide(10, 0)
print(result) 

#4
import math as m

def calculate_square_root(x):return m.sqrt(x)

print(calculate_square_root(9))   # 출력: 3.0
print(calculate_square_root(16))  # 출력: 4.0

#5
import datetime

def get_current_datetime():return datetime.datetime.now()

print(get_current_datetime())  # 출력: 현재 날짜와 시간이 출력됩니다 (예: 2024-06-03 10:20:30)

#6
import random

def generate_lotto_numbers():
    out = []
    while len(out) < 6:
        a = random.randint(1,45)
        if a not in out:
            out.append(a)
    return out

print(generate_lotto_numbers())

#7
class Book:
    def __init__(self, x,y,z): self.title, self.author, self.year = x, y, z

    def description(self): return(f"{self.title} by {self.author}, published in {self.year}")

    def is_classic(self): return True if 2024 - self.year >= 70 else False

# 객체 생성 및 사용 예시
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

print(book1.description())  # 출력: 1984 by George Orwell, published in 1949
print(book2.description())  # 출력: The Great Gatsby by F. Scott Fitzgerald, published in 1925
print(book3.description())  # 출력: To Kill a Mockingbird by Harper Lee, published in 1960

print(book1.is_classic())  # 출력: True
print(book2.is_classic())  # 출력: True
print(book3.is_classic())  # 출력: False

#8
def print_pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

# 시간복잡도 = O(n제곱)

#11
def list_operations(my_list):
    sum_of_elements = sum(my_list)
    max_element = max(my_list)
    min_element = min(my_list)
    length_of_list = len(my_list)
    return sum_of_elements, max_element, min_element, length_of_list

example_list = [1, 2, 3, 4, 5]
result = list_operations(example_list)
print(result)  # 출력: (15, 5, 1, 5)

#12
def list_methods(my_list):
    # 1. 3을 리스트의 맨 끝에 추가하세요
    my_list.append(3)
    # 2. 5를 리스트의 첫 번째 위치에 추가하세요
    my_list.insert(0,5)
    # 3. 리스트의 첫 번째 요소를 제거하세요
    my_list.pop(0)
    # 4. 리스트를 오름차순으로 정렬하세요
    my_list.sort()

example_list = [4, 2, 1, 5]
list_methods(example_list)
print(example_list)  # 출력: [1, 2, 3, 4, 5]

#13
def add_entry(my_dict, key, value):
    my_dict[key] = value

original_dict = {'a': 1, 'b': 2}
add_entry(original_dict, 'c', 3)
print(original_dict)  # 출력: {'a': 1, 'b': 2, 'c': 3}

add_entry(original_dict, 'd', 4)
print(original_dict)  # 출력: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#14
def check_duplicate_keys(dict1:dict, dict2:dict):
    for i in dict1.keys():
        if i in dict2.keys():
            print(f"Key {i} is duplicated")

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
check_duplicate_keys(dict1, dict2)
# 출력:
# Key b is duplicated

#15
def dict_methods(my_dict):
    # 1. 'd': 4 항목을 추가하세요
    my_dict['d'] = 4
    # 2. 'a' 항목을 제거하세요
    del my_dict['a']
    # 3. 딕셔너리를 키 기준으로 정렬된 리스트로 반환하세요
    a = list(my_dict.keys())
    a.sort
    return [(x, my_dict[x]) for x in a]

example_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_dict = dict_methods(example_dict)
print(sorted_dict)  # 출력: [('b', 2), ('c', 3), ('d', 4)]

#16
def add_element(my_set, element):
    my_set.add(element)

original_set = {1, 2, 3}
add_element(original_set, 4)
print(original_set)  # 출력: {1, 2, 3, 4}

add_element(original_set, 5)
print(original_set)  # 출력: {1, 2, 3, 4, 5}

#17
def check_duplicates(my_list):
    dic = {}
    out = []
    for i in my_list:
        if i not in dic.keys():
            dic[i] = 1
        else: dic[i] += 1
    for i in dic.keys():
        if dic[i] >= 2:
            out.append(i)
    print(f"Duplicates found: {out}")

duplicate_list = [1, 2, 2, 3, 4, 4, 4, 5]
check_duplicates(duplicate_list)
# 출력:
# Duplicates found: {2, 4}

#18
def set_operations(set1, set2):
    # 여기에 코드를 작성하세요
    union_set = set1 | set2
    intersection_set = set1 - (set1 - set2)
    difference_set = set1 - set2
    return union_set, intersection_set, difference_set

set1 = {1, 2, 3}
set2 = {2, 3, 4}
result = set_operations(set1, set2)
print(result)  # 출력: ({1, 2, 3, 4}, {2, 3}, {1})

#19
def set_methods(my_set):
    # 1. 5를 집합에 추가하세요
    my_set.add(5)
    # 2. 3을 집합에서 제거하세요
    my_set.remove(3)
    # 3. 집합이 비어있는지 확인하세요
    return True if len(my_set) == 0 else False

example_set = {1, 2, 3, 4}
is_empty = set_methods(example_set)
print(example_set)  # 출력: {1, 2, 4, 5}
print(is_empty)     # 출력: False