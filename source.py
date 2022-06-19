def min(a,b):
    return a-b

def plus(a, b, c=2):
    if c == 0:

        min(a,b)
        return a+b
    else:
        return plus(a, b, c-1)
plus(5, 8, 4)   # or whatever kicks off your script
