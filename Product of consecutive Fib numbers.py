#https://www.codewars.com/kata/5541f58a944b85ce6d00006a/python

#MySolution
def productFib(prod):
    n1, n2 = 0, 1
    if prod == 0: return [n1, n2, True]
    for i in range(200):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        if n1 * n2 == prod:
            return [n1, n2, True]
        elif n1 * n2 > prod:
            return [n1, n2, False]
    return 

#BestPractice
def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]


