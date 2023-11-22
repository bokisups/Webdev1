#file_store = open("text.txt", "r")#pride do datoteke/odpre
#contents = file_store.read()
#print(contents)

#file_store.close()

#with open("text.txt", "r") as reserv_file:
 #   contents = reserv_file.read()
  #  print(contents)

#with open("text2.txt", "w") as reserv_file:
 #   contents = reserv_file.write("We are ninjas, again")#overwrite
import random
secret = random.randint(1, 30)

attempts = 0
with open("records.txt", "r") as reserv_file:
    best_score = int(reserv_file.read())
    print(f"Record is {best_score}")
while True:
    guess = int(input("Guess the num 1 to 30 "))

    attempts += 1
    
    if guess == secret:
        if attempts < best_score:
            with open("records.txt", "w") as reserv_file:
                reserv_file.write(str(attempts))

      
        print("Bravo its",(secret))
        print(f"You did it in {attempts} attempt")
        break
    elif guess > secret:
        print("Try smaller then",(guess))
    elif guess < secret:
        print("Try larger then",(guess))