class Human:
    def __init__(self, name:str, age:int, live, hobby):
        self.name = name
        self.age = age
        self.live = live
        self.hobby = hobby
    def exercise(self):
        print(f"{self.hobby}!!")
        print(f"{self.live}의 자랑 {self.name} 할 수 있다!!!")

    def eat(self):
        print("뇸뇸뇸뇸")
    
    def sleep(self):
        print("으 사람사려 너무 졸려 으어엉어엉어")

class student(Human):
    def __init__(self):
        pass
    def study():
        print("""i dont want to study anymoreeeeeeeeeeeeeeeeeeee
LET ME HOME!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Free to the students!!!!!!!!!!!!!!!!!!!!!!!!!!!!""")

seongjin = Human("위성진", 27, "인천", "빠쑝")
seongjin.exercise()
wsj = student()
student.study()