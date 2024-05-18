# Guessing the number game
import random

sec_no=random.randint(1,20)
print("I am thinking of a number between 1 and 20")

for i in range(6):
    n=int(input("Make a guess:"))
    
    if n<sec_no:
        print("Your guess is too small")
    elif n>sec_no:
        print("Your guess us too large")
    else:
        break

if n==sec_no:
    print("Good job!.You guessed my number in ",i+1," guesses")
else:
    print("No\nThe number that i was thinking is ",sec_no,"\nBetter luck next time")