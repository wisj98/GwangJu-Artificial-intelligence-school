# func2
def p1(a,b): return a+b
def p2(a:str): return a*3
def p3(a,b): return a+b, a*b
def p4(a):
    long = ''
    for i in a:
        if len(i) >= len(long):
            long = i
    return long
def p5(*args): return sum(args)
def p6(*args):
    output = args[0]
    for i in args[1:]:
        output = output + f' {i}'
    return output
def p7(a, b =1):return a*b
def p8(a:str, b =1):return a*b
def p9(name, age): print(f"name:{name}, age:{age}")
def p10(**args):
    for a,b in args.items():
        print(f"{a}:{b}")