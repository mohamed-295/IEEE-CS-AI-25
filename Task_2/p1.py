# #Problem 1

list1=[]
for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])

grades=sorted(set([grade for name, grade in list1]))
second=grades[1]
names=sorted([name for name,grade in list1 if grade==second])
for name in names:
    print(name)