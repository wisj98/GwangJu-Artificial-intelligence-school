while 1:
    inp = input()
    if inp == '0': break
    arr = list(map(int, inp.split()[1:]))
    n = len(arr)
    counter = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                counter += 1
    if counter % 2 == 1:
        print("Marcelo")
    else: print("Carlos")