# 피보나치 ..

def pi(x):
    if x <= 1:
        return x
    else:
        a, b = 0, 1
        for i in range(x):
            a, b = b, a + b
        return b

print(pi(9))
