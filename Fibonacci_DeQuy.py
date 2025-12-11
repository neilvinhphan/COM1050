A = [[0,1], [1,0]]
mod = 10**9 +7

def mult(x, y):
    return [[(x[0][0] * y[0][0] + x[0][1] * y[1][0]) % mod,
            (x[0][0] * y[0][1] + x[0][1] * y[1][1]) % mod],
            [(x[1][0] * y[0][0] + x[1][1] * y[1][0]) % mod,
            (x[1][0] * y[0][1] + x[1][1] * y[1][1]) % mod]]

def pow(a, b):
    if b == 0:
        return a

    t = pow(a, b//2)
    if b % 2 == 0:
        return mult(t, t)
        
    return mult(mult(t, t), a)


def fi(n):
    if n == 0:
        return 0
    result = pow(A, n)
    return result[0][1] % mod

print(fi(10))

