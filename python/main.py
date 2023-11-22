import random
# first_number = int (input("Enter the 1st num "))
# second_number = int (input("Enter the 2nd num "))

# print(first_number + second_number)


#mood = "look"
#if mood == "drunk":
#    print("yeah man!")
#elif mood == "ok":
#    print("Oh boy")
#elif mood == "not good":
#    print("Opening up!")
#else:
#    print("Have a drink")

#secret_num = int(input("Try the secret number? From 10 to 30."))

#if secret_num == 22:
#    print("Nice one! You got it!")
#elif secret_num == 23:
#    print("Nooo but you are this .. close")
#elif secret_num == 21:
#    print("Nooo but you are this .. close")
#else: 
#    print("Nope, try again.")

#num1 = int(input("Number 1: "))
#num2 = int(input("Number 2: "))
#oper = input ("+,-,*,/")

#if oper == "+":
#    print (num1 + num2)
#elif oper == "-":
#    print (num1 - num2)
#elif oper == "*":
#    print (num1 * num2)
#elif oper == "/":
#    print (num1 / num2)
#else:
#    print("error")



#secret = 22
#guess = int (input("Guess the number 1-30 "))

#if guess == secret:
#    print("You got it")
#else:
#    print("Nope, wrong one" + str(guess))
#loooooooops.................................................
#secret = 22
#guess = 0

#while guess != secret:
 #   guess = int(input("Guess the number 1 - 30 "))

#if guess == secret:
#    print("You got it")
#else:
#   print("Nope, wrong one" + str(guess))

#secret = 22
#for x in range(5):
    #guess = int(input("Guess the number 1 - 30 "))

    #if guess == secret:
      #  print("You got it")
       # break
    #else:
     #   print("Nope, wrong one " + str(guess))

#secret = 22
#while True:
  #guess = int(input("Guess the secret number (between 1 and 30): "))
  #if guess == secret:
   # print("You've guessed it - congratulations! It's number 22.")
   # break
  #else:
 #   print("Sorry, your guess is not correct... The secret number is not "
#+ str(guess))

#secret = 10
#while True:
 #   guess = int(input("Guess the number"))

  #  if guess == secret:
   #     print("Bravo!")
    #    break
    #elif guess > secret:
     #   print("Try again the number is lower then",(guess))
   # elif guess < secret:
    #    print("Try again the number is larger then",(guess))

secret = random.randint(1,30)#random select number between 1 and 30

while True:
    guess = int(input("Guess the num 1 to 30 "))

    if guess == secret:
        print("Bravo its",(secret))# PITAJ DOMENA ZA +str(secret)
        break
    elif guess > secret:
        print("Try smaller then",(guess))
    elif guess < secret:
        print("Try larger then",(guess))


