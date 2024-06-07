def greet(name:str, greeting = "Hello", punctuation = "!"):
    return f"{greeting}, {name}{punctuation}"

print(greet("Alice")) # 출력: "Hello, Alice!"
print(greet("Bob", greeting="Hi")) # 출력: "Hi, Bob!"
print(greet("Charlie", "Hey", punctuation="!!")) # 출력: "Hey, Charlie!!"

def divide(x,y):
    if y == 0:
        print("Error: Division by zero is not allowed.")
    else: return x/y

class Animal:
    def __init__(self, name):
        self.name = name
        self.speak = "어떤 소리를 냅니다"
class Dog(Animal):
    def __init__(self, name):
        self.name = name
        self.speak = "멍멍!"

class Cat(Animal):
    def __init__(self, name):
        self.name = name
        self.speak = "야옹!"

animals = [Dog("렉스"), Cat("위스커스"), Animal("제네릭")]
for animal in animals:
    print(f"{animal.name}(이)가 {animal.speak()}")
