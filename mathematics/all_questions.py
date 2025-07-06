#gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# prime numbers related 
def is_prime(n)->bool:
    if n <=1 : return False
    for i in range(2,int(n**0.5)+1):
        if n%i == 0:
            return False
    return True 

# fibbonaci related 

def fib_series(n):
    a,b = 0,1
    series = []
    for _ in range(n):
        series.append(a)
        a,b = b,a+b
    return series

def fib_n(n):
    a,b = 0,1
    for _ in range(n):
        a,b = b,a+b
    return a 


#Reverse Digits of an Integer

def rev_int(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    
    while n:
        rev  = rev*10 + n%10
        n = n//10
    return sign*rev == n 

def sum_prod_digits(n):
    total_sum,total_prod = 0,1
    while n>0:
        digit = n%10
        total_sum += digit 
        total_prod *= digit 
        n //= 10


def isArmstrong(n)->bool:
    temp = n
    digits = []
    while temp > 0:
        digits.append(temp%10)
        temp //=10
    power = len(n)
    return sum(d**power for d in digits) == n 

## factorial related 
def factorial_recursive(n):
    if n == 0 or n == 1 :
        return 1 
    return n*factorial_recursive(n-1)



