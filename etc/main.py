import calculator as cal

def main():
    kiho = input("사용할 기호를 입력해주세요(+ - * / ** sqrt) \n 계산기를 종료하려면 exit를 입력해주세용 \n")
    if kiho == "exit": 
        print("Byeeeeee")
    else:
        x, y = list(map(int,input("계산할 숫자를 입력해주세용\n").split()))
        if kiho == "+": 
            print(cal.add(x,y))
        elif kiho == "-": 
            print(cal.subtract(x,y))
        elif kiho == "*": 
            print(cal.multiply(x,y))
        elif kiho == "/": 
            print(cal.divide(x,y))
        elif kiho == "**": 
            print(cal.power(x,y))
        elif kiho == "sqrt": 
            print(cal.sqrt(x))
        main()

if __name__ == "__main__":
    main()
