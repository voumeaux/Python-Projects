import random

def game():
    number_tries = 0
    print("Let's play a game, guess a random number within ranges 1-100! ")
    random_int = random.randint(1, 100)
    answer = random_int
    player = int(input(" Your Answer: "))

    while player != answer:
        number_tries += 1
        player = int(input("Try Again: "))
        if number_tries == 5:
            hint(number_tries, answer)

    correct(player, answer)

def correct(player, answer):
    if player == answer:
        print("CORRECT! GREAT JOB!")

def hint(number_tries, answer):
    yes_no = input("Would you like a hint? (yes/no)").lower()
    if yes_no == "yes":
        print("It's close to the number. " + str(answer - 5))
    else:
        print("Ok... here's your number of tries: " + str(number_tries))

game()
