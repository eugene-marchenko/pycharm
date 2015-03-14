def is_prime(x):
        if x < 2:
            return False
        n = x-1
        while n > 1:
            print x, n
            if x % n == 0:
                return False
            n -= 1
        else:
            return True

print is_prime(4567)