def square(x): # 제곱
    return x ** 2
def cube(x): # 세제곱
    return x ** 3
def power(x, n): # n제곱
    return x ** n
def factorial(n): # 팩토리얼
    if n == 0:
        return 1
    else:
        return n * factorial(n- 1)