from random import randint

def dice(n):
    return randint(1,n)

try:
    print dice(int(raw_input()))
except:
    print 'Next time put a fking valid number'
