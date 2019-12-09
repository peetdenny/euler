from m37.math.factors import get_proper_divisors

def get_amicable_numbers(limit):
    divisors = {}
    amis = []
    for i in range(1,limit):
        s = sum(get_proper_divisors(i))
        divisors[i] = s
        # if d(n) < n, then we should already have a record of d(d(n))
        if s < i and s in divisors and divisors[s] == i:
            amis.append(s)
            amis.append(i)
    return amis