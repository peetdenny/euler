import math

def get_divisors(n):
    if n ==0: return set()
    divisors = set()
    for i in range(1, math.floor(math.sqrt(n)+1)):
        if n % i ==0:
            divisors.add(i)
            divisors.add(int(n/i))
    return divisors