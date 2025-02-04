#Problem 7
def prime_factors(out,n):
    i=2
    while n>1:
        if n%i==0:
            out.append(i)
            n=n//i
        else:
            i+=1

n=int(input("Enter a number : "))
out=[]
prime_factors(out,n)
print("Prime factors : ",end=' ')
for i in set(out):
    print(i,end=', ')