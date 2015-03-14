def factorial(n):
    if n == 0:
        result = 1
        return result
    else:
        result = n * factorial(n-1)

        return result


print factorial(522)

