def divisor(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i
    while True:
        yield None


n=2
var=divisor(n)
print(next(var))
print(next(var))
print(next(var))
print(next(var))
print(next(var))
