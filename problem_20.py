import math, functools
functools.reduce(lambda x,y: x+y, [int(x) for x in str(math.factorial(100))])
