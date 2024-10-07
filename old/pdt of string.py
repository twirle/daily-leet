def multiply(num1: str, num2: str) -> str:
    m, n = map(len, (num1, num2))
    print(m, n);
    prod = [0] * (m + n)
    print(prod)
    for i, a in enumerate(reversed(num1)): 
        for j, b in enumerate(reversed(num2)): 
            print("j = ", j, "a = ", a, "b = ", b)
            prod[i + j] += int(a) * int(b)
            prod[i + j + 1] += prod[i + j] // 10
            prod[i + j] %= 10
    while len(prod) > 1 and prod[-1] == 0:
        prod.pop()
    return ''.join(map(str, prod[:: -1]))

num1 = str(2)
num2 = str(3)
print(multiply(num1, num2));