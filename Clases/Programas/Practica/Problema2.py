def cuadrados(n):
    if n == 1:
        return 1
    else:
        return n**2 + cuadrados(n-1)
