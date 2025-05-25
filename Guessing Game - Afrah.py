#-----------------------------------------------------------------------------
# Name:        Guess the Number
# Purpose:     A guessing game using python where the computer creates a range and the user guesses values.
#              Uses variables, input, type conversions, comparisons, lists, error checking, random and loops.          
# Author:      Afrah Iqbal
# Created:     29-Sept-2022
# Updated:     05-Oct-2022
#-----------------------------------------------------------------------------

#Features Added:
#   Score/High score
#   Lives
#   Difficulty increaser

#-----------------------------------------------------------------------------

varStr = 5 #streak/life count
ent = 0 #enter a value
mode = 0 #start mode
score = 0 #score counter
import random
largeVal = random.randint(30,40) #creates a random maximum value
ran = random.randint(0, largeVal) #selects a random number to guess
multi = [1, 2, 3] #difficulty increaser
#print (ran) #TO HELP CHECK program

#Start - waits until user types in 1 and decides to begin, using while loop
print('Rules: Begin with 5 lives, incorrect answers result in life loss, correct answers give points')
while mode != 's':
    mode = input('Press "s" key to begin!: ')

             
if mode == 's': #Game loop

    while ent != ran: #while the number guessed is not equal to number selected - run code
        #print(f'Cheat mode {ran}')
        if varStr < 1: #checking if 0 lives/lost game
            print ('You Lose!!!!!!''Total Score:' f'{score}')
            
            end = input('Would you like to retry? Type "yes" or "no": ') #retry 
            if end == 'no': #end game
                print('Game ended :(') 
                exit()
            else:
                print('Lets go again!') #restart
                ran = random.randint(0,largeVal)
                #print (ran) #to check program
                varStr = 3  #Might want to consider storing this number as a constant because right now if you want to change it, it must be changed in multiple places in your program
        
        ent = input('Guess a number between 1 and ' f'{largeVal}' ':')
        while ent.isnumeric() == False: #error checking for invalid entries
            print ('Invalid! Enter a NUMBER: ')
            ent = input('') # asking for new input
        
        if ent.isnumeric(): #if valid integer run code 
            
            if int(ent) > ran: #number guessed larger than number selected
                varStr = varStr-1
                print('Too high! ''Lost a life 'f'{varStr} ''left!')
            elif int(ent) < ran: #number guessed lower than number selected
                varStr = varStr-1
                print('Too low! ''Lost a life 'f' {varStr} ' ' left!')
            else:
                score = score+1 #correct guess
                print('Correct! The number is' f' {ent}! ' 'Score:' f' {score}')
                
                #Ask if user would like to end the game or continue
                end = input('Would you like to end? "yes" or "no": ') 

                if end == 'yes': #if yes entered end game
                    print('Game Ended! ' 'High score:' f' {score}')
                    break
                
                elif end == 'no': #if no entered ask for difficutly increase
                    end = input('Increase difficulty? "yes" or "no"?: ')
                    if end == 'no': #rerun program
                        ran = random.randint(0, largeVal)
                        #print (ran) #to check program
                        varStr = 3
                    elif end == 'yes': #level increase   #What happends if I don't type either no or yes?  Always catch the null case
                        print ('Level up!')
                        largeVal = largeVal*(random.choice(multi))
                        ran = random.randint(0, largeVal)