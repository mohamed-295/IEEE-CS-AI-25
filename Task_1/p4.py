#Problem 4

s = input()
s1 = s.split()
for w in s1:
    print(w[::-1],end=' ')