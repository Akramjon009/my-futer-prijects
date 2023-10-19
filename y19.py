def fibonacci_piramida(N):
    a, b = 0, 1
    count = 0
    ind = 0
    for i in range(N):
        if count+i < N:
            ind += 1
            count += i
        else:
            break
    count = 0
    for i in range(ind):
        for j in range(N - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            if count < N:
                print(f"{b} ", end="")
                a, b = b, a + b
                count += 1
            else:
                break
        print("")

N = int(input("N= "))
fibonacci_piramida(N)