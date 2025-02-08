#Problem 3
N = int(input())
list1=[]
for i in range(1,N+1):
    type=input().split()
    if type[0]=="insert":
        list1.insert(int(type[1]),int(type[2]))
    elif type[0]=="print":
        print(list1)
    elif type[0]=="remove":
        list1.remove(int(type[1]))
    elif type[0]=="append":
        list1.append(int(type[1]))
    elif type[0]=="sort":
        list1.sort()
    elif type[0]=="pop":
        list1.pop()
    elif type[0]=="reverse":
        list1.reverse()
    else:
        pass
