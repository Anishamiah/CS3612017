print("Exercise 6a) \n:");

def is_prime(n):
    
    if (n < 2):
        
        return False
    else:
        for i in range(2,n):
            if (n % i == 0):
               return False
        return True
print (is_prime(3), "\n");

print("Exercise 6b) \n:");
def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    print ('\t'),f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

print (is_prime(20));

print("Exercise 6c) \n:");
lower = 0
upper = 20
print("Prime numbers between",lower,"and",upper,"are:")

for n in range(lower,upper + 1):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n);
           
print("Exercise 6d) \n:");
def generate_n_primes(N):
     primes  = []
     chkthis = 2
     while len(primes) < N:
         ptest    = [chkthis for i in primes if chkthis%i == 0]
         primes  += [] if ptest else [chkthis]
         chkthis += 1
     return primes

print (generate_n_primes(3));
