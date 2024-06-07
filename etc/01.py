x = int(input())

p_list = list(map(lambda x: int(x), input().split()))
p_list.sort(reverse=True)
sums = sum(p_list)
if sums/2 >= p_list[0]:
    print(sums)
else:
    print(sums - p_list[0] + sum(p_list[1:]) + 1)