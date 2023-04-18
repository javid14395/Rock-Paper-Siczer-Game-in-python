
import os
import random
#print(dir(random))

# Storing Result of Both Candidate
co_result = 0
user_result = 0

# Taking User Name in Input
Name = input("Enter Your Name :")
print(f"{Name} Scoor is: {user_result} !!! Computer Scor is : {co_result}")
#os.system("timeout /t 3")
# This Logic for computer and user valid input 
while True:

    while True:
        print("Welcome to Over Game")
        print("1.Rock \n2.Paper \n3.Siczer")
        User1 = int(input("Answer: "))
        if User1 <=  3:
            break
        else:
            print("Please Enter Valid Number")
            #os.system("timeout /t 3")
            os.system("cls")
    Co_coice = [1, 2, 3]
    Computer1 = random.choice(Co_coice)
    cho_name = ("Rock", "Paper", "Siczer")
    print(f"{Name} Choice is {cho_name[User1-1]} And Computer Coice is {cho_name[Computer1-1]}")
    print("Please Wait We will show your result")


    # Calculatin Result and Increesing User and Computer Score
    while True:
        os.system("cls")
        print(f"{Name} Scoor is: {user_result} !!! Computer Scor is : {co_result}")
        if User1 == Computer1:
            print("It's Draw")
            os.system("timeout /t 2")
            os.system("cls")
            break
        elif User1 == 1:
            if Computer1 == 2:
                print("Paper covers rock! You lose.")
                co_result +=1
                break
            else:
                print("Rock smashes scissors! You win!")
                user_result += 1
                break
        elif User1 == 2:
            if Computer1 == 3:
                print("Scissors cuts paper! You lose.")
                co_result += 1
                break
            else:
                print("Paper covers rock! You Win.")
                user_result += 1
                break
        elif User1 == 3:
            if Computer1 == 1:
                print("Rock smashes scissors! You lose!")
                co_result += 1
                break
            else:
                print("Scissors cuts paper! You win!")
                user_result += 1
                break
    k = input("Rematch 'Y' Quite 'N'")
    os.system("cls")
    j = k.capitalize()
    if j == 'N':
        os.system("cls")
        print(f"{Name} Scoor is: {user_result} !!! Computer Scor is : {co_result}")
        print("\n Thnak You For Plying Game")
        os.system("timeout /t 5")
        os.system("cls")

        break
    else:
        print(f"{Name} Scoor is: {user_result} !!! Computer Scor is : {co_result}")