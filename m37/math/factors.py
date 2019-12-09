import math

# returns a list of the divisors of n, including n
def get_divisors(n):
    if n ==0: return list()
    divisors = set()
    for i in range(1, math.floor(math.sqrt(n)+1)):
        if n % i ==0:
            divisors.add(i)
            divisors.add(int(n/i))
    return list(divisors)


def get_proper_divisors(n):
    d = get_divisors(n)
    if len(d) <1:
        return 0
    d.sort()
    d.pop()
    return d