#This project asks users a bunch of questions.If they are right then 1 is added to their score
#At the end of the program ,what the user gets is printed over the total
print("welcome to my Game of Quizes")
playing =input("Do you want to play?  ")
if (playing.lower() != "yes"):
    print("Bye See you next time :)")
    quit()
else:
    print("Okay ! Let's Play:)") 
    score= 0 
answer=input("If you wish to exit our game kindly type Exit  but if you want to proceed press the Enter Button  :")
if answer=="Exit": 
    print("Chonjo Chonjo!")
    quit()
else:   
    print("Let's Proceed")
answer = input("Which is the Language with the least line of code?  ")
if answer=="Python":   
    print('correct!') 
    score +=1
else:
    print("Incorrect!")
    print("Nice try Though")
answer = input("What is the Basic social Requirement in the Modern day world? ")
if answer =="Money":
    print('correct!')  
    score+=1  
else:
    print("Incorrect!  You cannot proceed with this Game without acknowledging the importance pf money in modern societies !")
    quit()
    
answer = input("How many Years does an undergraduate take in medical school?  ")
if answer =="5":
    print('correct!') 
    score+=1
else:
    print("Incorrect!")
    print("Nice try Though")
answer = input("Which is the Best University in Kenya?  ")
if answer =="Kenyatta University":
    print('correct!')
    score+=1
else: 
    print("Incorrect!")
    print("Nice try Though")
answer = input("How many Ranks does a military commander Have?  ")
if answer =="4":
    print('correct!')
    score+=1
else:
    print("Incorrect!")
    print("Nice try Though")
answer = input("What is the Capital city of Kenya? ")
if answer =="Nairobi" :
    print('correct!')
    score+=1
else:
    print("Incorrect!")
    print("Nice try Though")


print("You got"  ,score,  "questions correct!")
print("You got"  +   str((score/6)*100) +  "%.")







