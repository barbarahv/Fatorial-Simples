def f(n):
    if n == 1:
        return 1
    if n == 0:
        return 1
    if n > 1:
        return f(n-1) * n

i = int(input())
print(f(i))


from math import factorial as fat
print(fat(int(input())))