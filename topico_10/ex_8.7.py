def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)
print(f"MDC de 10 e 5 ==>: {mdc(10, 5)}")
print(f"MDC de 53 e 35 ==>: {mdc(55, 35)}")
print(f"MDC de 57 e 4 ==>: {mdc(5, 3)}")
