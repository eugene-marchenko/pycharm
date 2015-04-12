def prime(n):
    if n <= 3:
        if n == 2 or n == 3:
            return True
        else:
            return False
    else:
        for devision in range(2, int(n**0.5)+1):
            if n % devision == 0:
                return False
        return True

print prime(52)

