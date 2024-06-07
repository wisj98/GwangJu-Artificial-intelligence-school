a, b = list(map(int, input().split()))
cal = []
result = [0]
def refresh(x):
    for i in range(x, len(result)):
        if cal[i - 1][0] == '+':
            result[i] = (result[i - 1] + cal[i-1][1]) % 1000000007
        else:
            result[i] = (result[i - 1] * cal[i-1][1]) % 1000000007
for i in range(a): 
    cal.append(input().split())
    cal[i][1] = int(cal[i][1])
    result.append(0)
refresh(1)

for i in range(b):
    x,y,z = input().split()
    x = int(x)
    cal[x - 1][0] = y
    cal[x - 1][1] = int(z)
    refresh(x)
    print(result[-1])