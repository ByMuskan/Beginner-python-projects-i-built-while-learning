# day 2 project=bmi

# height=float(input ("Enter your height(in meters): "))
# weight=float(input("Enter your weight(in kilograms): "))
# bmi=weight/height**2
# if bmi<=18.5:
#     print("You are Underweight")
# elif bmi>=25.0 and bmi<=29.9:
#     print("You are Overweight")
# elif bmi>30:
#    print("you are obese")
# else:
# print("You are Healthy")
# print("and Your BMI is : ",round(bmi,2))

# day_3_project = to create python pizza delivery program

# print("Welcome To Python Pizza Deliveries :)")
# size=input("What size of pizza do you want? small,medium or large : ").lower()
# pp=input("Do you want pepperoni on your pizza?(y or n): ").lower()
# extra_cheese=input("Do you want extra cheese?(y or n): ").lower()
# bill=0
# if size=="small":
#     bill+=15
#     if pp=="y":
#         bill+=2
#     if extra_cheese=="y":
#         bill+=1
#     print(f"your total Bill is:${bill}")
# elif size=="medium":
#     bill+=20
#     if pp=="y":
#         bill+=3
#     if extra_cheese=="y":
#         bill+=1
#     print(f"your total Bill is:${bill}")
# elif size=="large":
#     bill+=25
#     if pp=="y":
#         bill+=3
#     if extra_cheese=="y":
#         bill+=1
#     print(f"your total Bill is:${bill}")
# else:
#     print("Error, please try again:(")


#day_4_PROJECT= TREASURE ISLAND

# print("WELCOME TO TREASURE HUNTING")
# print("Your Mission is to find the treasure!\nIn this Game You will be asked some questions and given some choices,\nChoose any one of them wisely to win the Game :)  ")
# ques_1=input("Right now you are stuck on an island\nWhich direction do you want to take? Left or Right :").lower()
# if ques_1=="left":
#      ques_2 = input('you\'re safe now!!\nNow you\'re in a lake.There is an island in the middle of the lake,\nType "Wait"for boat and "Swim"to swim across the island :').lower()
#      if ques_2 == "wait":
#         ques_3 = input("Great!you're safe again:)\nNow choose between Red,Blue and yellow Door:").lower()
#         if ques_3=='yellow':
#             print("You Win!!!")
#         elif ques_3=='red':
#             print("You got Burned by fire\nGAME OVER")
#         elif ques_3=='blue':
#             print("You were eaten by Beasts.\nGAME OVER")
#         else:
#              print("GAME OVER:(")
#      else:
#          print("You were attacked by trouts.\nGAME OVER:(")
# else:
#      print("Oops,You fell into a hole\nGAME OVER:(")

#day_5_project= password generator# easy level
# import random
# print("Welcome To password Generator")
# letters=['a','b','c','d','e','f','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# numbers=['0' ,'1','2','3','4','5','6','7','8','9']
# symbols=['!','@','#','$','%','&','*']
#    
# user_letters=int(input("How many letters would you like in your password\n"))#why are we adding int in front of input even if letters are not numbers?
# user_numbers=int(input("How many numbers would you like\n"))
# user_symbols=int(input('How many symbols would you like\n'))#why are we adding int in front of input even if symbols are not numbers?
# password=''
# for char in range(0,user_letters):
#     character=random.choice(letters)
#     password+=character
# for num in range(0,user_numbers):
#     number=random.choice(numbers)
#     password+=number
# for sy in range(0,user_symbols):
#     symbol=random.choice(symbols)
#     password +=symbol
# print(f"Your Password is {password}")


#password generator(hard level)
# import random
# print("Welcome To password Generator")
# letters=['a','b','c','d','e','f','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# numbers=['0' ,'1','2','3','4','5','6','7','8','9']
# symbols=['!','@','#','$','%','&','*']
#
# user_letters=int(input("How many letters would you like in your password\n"))#why are we adding int in front of input even if letters are not numbers?
# user_numbers=int(input("How many numbers would you like\n"))
# user_symbols=int(input('How many symbols would you like\n'))#why are we adding int in front of input even if symbols are not numbers?
# password=[]                     
# for char in range(user_letters):
#     character=random.choice(letters)
#     password.append(character)
# for num in range(user_numbers):
#     number=random.choice(numbers)
#     password.append(number)
# for sy in range(user_symbols):
#     symbol=random.choice(symbols)
#     password.append(symbol)
# random.shuffle(password)
# shuffled_word = ''.join(password)
# print(f"Your Password is {shuffled_word}")

# day6_project= escaping a maze

#day7_project (the hangman game)

#import random
#word_list = ['camel','pizza','penguin']#this is a list which contains 3 words

#chosen_word=random.choice(word_list)# Random function will randomly choose one word from word_list
#print(chosen_word)

#place_holder=""
#word_length=len(chosen_word) #here you're checking the length of the chosen word
#for i in range(word_length):
    #place_holder += "_" #this will replace each letter of the chosen word with ( _ )
#print(place_holder)

#game_over=False
#correct_letters=[]
#lives = 6
#while not game_over: #while loop is used because we want to give user multiple chances to guess the correct word
    #guess=input("guess an alphabet:")
    #display=""
    #for letter in chosen_word:
        #if letter == guess:
            #display += letter
            #correct_letters.append(guess)
        #elif letter in correct_letters:
            #display += letter
        #else:
            #display += "_"

    #print(display)

    #if guess not in chosen_word:
        #lives-= 1
        #if lives == 0:
            #game_over=True
            #print("YOU LOSE :(")

   # if "_" not in display:
        #game_over=True
        #print|("YOU WIN")

#day8 project love calculator

#def calculate_love_score(name_1,name_2):
    #combined_names = (name_1 + name_2)
    #lower_name=combined_names.lower()

    #t = lower_name.count("t")
    #r = lower_name.count("r")
    #u = lower_name.count("u")
    #e = lower_name.count("e")
    #first_digit = t + r + u + e

    #l = lower_name.count("l")
    #o = lower_name.count("o")
    #v = lower_name.count("v")
    #e = lower_name.count("e")
    #second_digit = l + o + v + e

    #score = int(str(first_digit) + str(second_digit))
    #print(score)

#calculate_love_score("u","pizza")

# Ceaser Cipher

def encrypt():
    original_text=input("Enter original text:")
    shift_amount=int(input("Enter the amount of shift:"))














