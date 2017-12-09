print ("Exercise 12:");

def fib(n):
  
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))


n = 10


n = int(input("How many terms? "))

if n <= 0:
   print("Please enter a positive value:")
else:
   print("Fibonacci sequence:")
   for i in range(n):
       print("The fibonacci number", (i+1), "is:",fib(i))
