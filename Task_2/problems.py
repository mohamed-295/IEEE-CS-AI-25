# # #Problem 1
#
# list1=[]
# for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         list1.append([name,score])
#
# grades=sorted(set([grade for name, grade in list1]))
# second=grades[1]
# names=sorted([name for name,grade in list1 if grade==second])
# for name in names:
#     print(name)




# #Problem 2
#
# n = int(input())
# arr = map(int, input().split())
#
# scores=sorted(set(arr))
# print(scores[-2])


# #Problem 3
# N = int(input())
# list1=[]
# for i in range(1,N+1):
#     type=input().split()
#     if type[0]=="insert":
#         list1.insert(int(type[1]),int(type[2]))
#     elif type[0]=="print":
#         print(list1)
#     elif type[0]=="remove":
#         list1.remove(int(type[1]))
#     elif type[0]=="append":
#         list1.append(int(type[1]))
#     elif type[0]=="sort":
#         list1.sort()
#     elif type[0]=="pop":
#         list1.pop()
#     elif type[0]=="reverse":
#         list1.reverse()
#     else:
#         pass

# #Problem 4
# library_catalogue={
#     "Book1" : {
#         "title" : "Electronics 2",
#         "auther" : "Dr/Rania Ahmed",
#         "publication_year": 2022,
#     },
#     "Book2" : {
#         "title" : "Fluid Mechanics",
#         "auther" : "Dr/Salem Anos",
#         "publication_year": 2020,
#     },
#     "Book3" : {
#         "title" : "Data Structure",
#         "auther" : "Sara Khalil",
#         "publication_year": 1980,
#     },
#     "Book4" : {
#         "title" : "Logic Design",
#         "auther" : "Howaida AbdEl-latif",
#         "publication_year": 2002,
#     },
#     "Book5" : {
#         "title" : "Electric Field",
#         "auther" : "Dr/Ashraf Samir",
#         "publication_year": 2001,
#     }
# }
#
# print(library_catalogue['Book1'])

# #Problem 5
# from collections import Counter
#
#
# def count_word(file_path):
#         with open(file_path, 'r') as file:
#             text = file.read()
#
#         lines=text.split('\n')
#
#         words=[]
#         for l in lines:
#             line=l.split(": ",1)
#             if len(line)>1:
#                 person,content=line
#                 words.append(person)
#                 content_words=content.split()
#                 words.extend(content_words)
#
#         counts=Counter(words)
#
#         for word, count in counts.items():
#             print(f"{word}: {count}")
#
#
# file_path = "simple_text.txt"
# count_word(file_path)
#

# #Problem 6
# import random
# import string
# def generate_password(length):
#     characters = string.digits+string.ascii_letters
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password
#
# print(generate_password(8))

#
# #Problem 7
# set1={1,2,3,4,5}
# set2={3,4,5,6,7}
#
# print(set1.intersection(set2))


# #Problem 8
# import random
# def random_number_game():
#     num=random.randint(1, 100)
# 
#     print("🔎 Guess the Number : ")
#     for i in range(5) :
#         guess = int(input(f"{5-i} left , Enter a Num :"))
#         if guess==num:
#             print("✅ That's Correct!!! ")
#             return True
#         else:
#             print("❌ Try Again")
#     print(f"The number was : {num}")
#     return False
# 
# while True:
#     isEnd=random_number_game()
#     play_again=input("Enter ""yes"" if you want to play again ⚡ " ).strip().lower()
# 
#     if play_again!="yes":
#         print("Thanks For Playing 😘")
#         break