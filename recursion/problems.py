#1.
def printName( N,name):
        if N == 0:      # Base case
           return
        print(name)
        printName(N-1) # Recursive call with smaller input

printName(5,"moaz") 

#2.
# Top down approach 
def print1toN(i,n):
      if  i >n:
         return
      print(i)
      print1toN(i+1,n)

print1toN(1,5)

# Bottom up approach 
def print_1to_N(n):
     if n == 0:
          return
     print_1to_N(n-1)
     print(n)

print_1to_N(5)

#3.
def printNto1(n):
     if n == 0:
          return
     print(n)
     printNto1(n-1)
     
printNto1(5)

def print_N_to_1(i,n):
     if i > n:
          return
     print_N_to_1(i+1,n)
     print(i)

print_N_to_1(1,5)
          
#4.
def sumNnumbers(n):
     if n == 0:
          return
     sum_n = n + sumNnumbers(n-1)
     return sum_n

sumNnumbers(5)

#5.
def factorialNumbers(n):
    #  if n <= 1:
    #       return 1
    #  return n*factorialNumbers(n-1)

    # result = 1
    # while n > 1:
    #      result *= n
    #      n -= 1 
    # return result






     
     


