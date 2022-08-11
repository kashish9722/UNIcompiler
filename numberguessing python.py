# Program to generate a random number between 0 and 9

# importing the random module
import random
score = 10;
print("you get 10 chances")
c = (random.randint(0,100));
val = input("Guess the number: ") 
val = int(val)
if(c % 5 == 0):
        print("HINT :The number is divisibe by 5")
if(c % 2 == 0):
        print("HINT :The number is divisibe by 2")
if(c % 8 == 0):
        print("HINT :The number is divisibe by 8")
while(val != c):
    
    
    if(val > c ):
       score = score-1
       val = input("Enter a smaller number: ")
       val = int(val) 
       
    if(val < c ):
        score = score-1
        val = input("Enter a larger number: ")
        val = int(val)

    if(score <= 0):
        print("OOPS! you lost all your chances")
        break;

if(val == c):
        print("Correct Answer!!")
        print ("SCORE: ")
        print (score)
        
    

    
    

