##PROBLEM 1
##guess = []
##for i in range(1,1000):
##    if i % 3 == 0 or i % 5 == 0:
##        guess.append(i)
##
##print(sum(guess))
##
##PROBLEM 2
##def fib(n):
##    result = []
##    a, b = 0, 1
##    while b < n:
##        result.append(b)
##        a, b = b, a+b
##    return result
##evens = []
##for i in fib(4000000):
##    if i % 2 == 0:
##        evens.append(i)
##
##print (sum(evens))
##    
##PROBLEM 3
##def lpf(a):
##    b=2
##    while a > b:
##        if a % b == 0:
##            a = a/b
##            b = 2
##        else:
##            b += 1
##    print(b)
##
##PROBLEM 4
##Good for y up to 3 (2.5 seconds); y = 4 (4.3 minutes); y = 5 (7.23 hours)
##def pal(x):
##    if len(str(x)) % 2 == 0:
##        y = int((len(str(x))/2))
##    else:
##        y = int((len(str(x))-1)/2)
##    x=str(x)
##    for i in range(y):
##        if x[i] != x[(len(str(x))-i)-1]:
##            return False
##    return True
##def largepal(y):
####'y' is the number of digits for the multiples
##    pals = []
##    mults = []
####    ident_pals = []
##    for i in range(10**(y-1), 10**y):
##        for j in range(10**(y-1), 10**y):
##            if pal(i*j):
##                pals.append(i*j)
##                if i*j == max(pals):
##                    mults.append("%s and %s" % (i, j))
####                if i == j:
####                    ident_pals.append(i)
##    t = max(pals)
##    return ("The multiples are %s." % (mults[-1]), "The product is %s." % (t))
##
##PROBLEM 5
##for i in range(2,1000000000000):
##    if i % 11 == 0:
##        if i % 12 == 0:
##            if i % 13 == 0:
##                if i % 14 == 0:
##                    if i % 15 == 0:
##                        if i % 16 == 0:
##                            if i % 17 == 0:
##                                if i % 18 == 0:
##                                    if i % 19 == 0:
##                                        if i % 20 == 0:
##                                            print (i)
##                                            break
##
##PROBLEM 6
##def sumsq(x):
##    i = range(1, x+1)
##    squares = []
##    for j in range (1, x+1):
##        squares.append(j**2)
##    a = (sum(squares))
##    b = (sum(i))**2
##    c = b - a
##    return c
##
##PROBLEM 7
##def isprime(x):
##    for i in range (2, x-1):
##        if x % i == 0:
##            return False
##    return x
##def is_prime(n):
##  if n == 2 or n == 3: return True
##  if n < 2 or n%2 == 0: return False
##  if n < 9: return True
##  if n%3 == 0: return False
##  r = int(n**0.5)
##  f = 5
##  while f <= r:
####    print '\t',f
##    if n%f == 0: return False
##    if n%(f+2) == 0: return False
##    f +=6
##  return n
##def primelist(x):
##    list = [2]
##    j = 3
##    while len(list)< (x+1):
##        if is_prime(j) == False:
##            j+=2
##        else:
##            list.append(is_prime(j))
##            j+= 2
####            print(list)
##    return list[x-1]
##
##PROBLEM 8
##def adjacent_13(y):
##  x = str(y)
##  winners = []
##  for i in range (0,986):
##    prod = int(x[i]) * int(x[i+1]) * int(x[i+2]) * int(x[i+3]) * int(x[i+4]) * int(x[i+5]) * int(x[i+6]) * int(x[i+7]) * int(x[i+8]) * int(x[i+9]) * int(x[i+10]) * int(x[i+11]) * int(x[i+12])
##    winners.append(int(prod))
##  winners.sort()
##  return winners[-1]
##
##PROBLEM 9
####def gcd(a, b):
####    if b == 0:
####       return a 
####    else:
####       return gcd(b, a % b)
##def trip(a,b,c):
##    return a**2 + b**2 == c**2
##for a in range(1,997):
##    for b in range (a, 999 - a):
##        c = 1000 - a - b
##        if c <= b:
##            break
##        if trip(a,b,c):
##            print (a, b, c)
##            print("Product: {}".format(a*b*c))
##            exit(0)
##
##PROBLEM 10
