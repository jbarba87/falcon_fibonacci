# fibonacci.py
# ejecutar: $ python fibonacci.py

def fib_rec(n):
    if n == 2:
        return 2
    if n == 1:
        return 1
    return fib_rec(n-1) + fib_rec(n-2)

def fib_it(n):
    l = [1, 2]
    for i in range(2, n):
        sig = l[-1] + l[-2]
        l.append(sig)
    return l[-1]


if __name__ == "__main__":
    print 'Fibonacci recursivo de 8:', fib_rec(8)
    print 'Fibonacci iterativo de 8:', fib_it(8)

