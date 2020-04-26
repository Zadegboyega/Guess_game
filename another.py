import random 

prompt = "\nThis is a guessing game."
prompt += "\nInput your preferred level, Your options are 'easy', 'medium' and 'hard':  "
prompt = input(prompt)

easy_guess_count = 0
medium_guess_count = 0
hard_guess_count = 0

e_number = random.randint(1,10)
m_number = random.randint(1,20)
h_number = random.randint(1,50)

e_chances = 6
m_chances = 4
h_chances = 3

#while loop for the easy level
while easy_guess_count < e_chances:
    
    if prompt == 'easy':
        try:
            e_guess = input("Guess a number between 1-10: ")
            easy_guess_count += 1
            if e_guess == e_number:
                print("Congratulations You Won!")
                break
            else:
                print("Wrong number, try again.")
                print("You have " , int(e_chances - easy_guess_count) , "chances left" )
        
        except ValueError:
            print("Please enter a whole number!")
            
#while loop for medium level  
while medium_guess_count < m_chances:
    if prompt == 'medium':
        try:
            m_guess = input("Guess a number between 1-10: ")
            medium_guess_count += 1
            
            if m_guess == m_number:
                print("Congratulations You Won!")
                break
            
            else:
                print("Wrong number, try again.")
                print("You have " , int(m_chances - medium_guess_count) , "chances left" )  
    
   
        except:
            print("Please enter a whole number!")
           
#while loop for hard level
while hard_guess_count < h_chances:
    if prompt == 'hard':
        try:
            h_guess = input("Guess a number between 1-10: ")
            hard_guess_count += 1
            if h_guess == h_number:
                print("Congratulations You Won!")
                break
            else:
                print("Wrong number, try again.")
                print("You have " , int(h_chances - hard_guess_count) , "chances left" )
    
        except:
            print("Please enter a whole number!")
