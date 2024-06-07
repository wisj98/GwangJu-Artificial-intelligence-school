def solution(r1, r2):
    r1_dot = set()
    r2_dot = set()
    for i in range(r1+1):
        max_j = int((r1**2 - i**2)**0.5)
        r1_dot.add([i,j] for j in range(max_j + 1) if i**2 + j**2 != r1**2)
    for i in range(r2+1):
        max_j = int((r2**2 - i**2)**0.5)
        r2_dot.add([i,j] for j in range(max_j + 1) if j != 0)
    print(r2_dot - r1_dot)
    return (len(r2_dot - r1_dot)) * 4

solution(2,3)