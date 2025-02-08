#Problem 8
import random
def random_number_game():
    num=random.randint(1, 100)

    print("🔎 Guess the Number : ")
    for i in range(5) :
        guess = int(input(f"{5-i} left , Enter a Num :"))
        if guess==num:
            print("✅ That's Correct!!! ")
            return True
        else:
            print("❌ Try Again")
    print(f"The number was : {num}")
    return False

while True:
    isEnd=random_number_game()
    play_again=input("Enter ""yes"" if you want to play again ⚡ " ).strip().lower()

    if play_again!="yes":
        print("Thanks For Playing 😘")
        break
# I made my own version 😊
