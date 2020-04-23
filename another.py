import random

def guess_a_number():
    guess_count = 0
    level_with_range = {'e': 10, 'm': 20, 'h':50}

    while True:
        level= input ("\nEnter your game preference, Type E for Easy with range (1,10), M for Medium with range (1,20) and H for Hard with range(1,50)").lower()
        try:
            number = random.randint(1,level_with_range[level])
            break
        except KeyError:
            print("Wrong input, try again")
    while True:
        try:
            guess = input(int("Guess: "))
            guess_count += 1
            if number == guess:
                print("Congratulations you won!")
                return guess_a_number()
        except ValueError:
            print("\nEnter a whole number!")
def main():
    guess_a_number()

if __name__ == "__main__":
    main()
