def add_and_multiply(a,b):
    tuple1 = (a+b, a*b)
    return tuple1

def apply_callback(a,b,callback):return callback(a,b)
def add(a,b): return a+b

sum_lambda = lambda a,b: a+b

def higher_order_function(a,b,c): return c(a,b)
def multiply(a,b): return a*b

def write_to_file(a,b):
    with open(a, 'w') as file:
        file.write(b)
write_to_file("basic.txt", "가위바위보")

with open("basic.txt", "r") as file:
    print(file.read())