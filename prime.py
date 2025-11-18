lower=int(input('enter lower limit::'))   #prime number in a limit using loop
upper=int(input('enter upper limit::'))
prime=['prime numbers in the limit ',lower,'and',upper,'are ::']
for i in range(lower,upper+1):
    isprime=True
    for k in range(2,int(i/2)+1):
        
        if(i%k==0):
            isprime=False
            break
    if(isprime==True and i>2):
        prime.append(i)
print(prime)

#prime number in a limit using recursion

def prime(n,div=2):
    if n<2:
        return
    if n%div==0:
        return False
    if(div>n/2):      #this checks if the divisor is >num/2.A num can have factors -1,num itself and numbers less than num/2
        return True   #if div>num then that means no other factors are found
    return prime(n,div+1)


def prime_range(start,end):
    if start>end:     #to stop the recursion
        return
    if prime(start):
        print(start,end=' ')
    prime_range(start+1,end)

lower=int(input('enter lower limit::'))   
upper=int(input('enter upper limit::'))
prime_range(lower,upper)
    