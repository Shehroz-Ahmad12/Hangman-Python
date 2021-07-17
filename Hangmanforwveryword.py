#hangman

import random


name=input("Please enter your name: ")
print("Welcome to hangman ", name)

def game():
    from GUI import hangman
    restart=input("Do you want to start the game y/n? ")
    count=0
    total=0
    while restart=="y":
        list1=["building","advanced","accident","delivery","guardian","world","phone","hangman","hello"]
        word=random.choice(list1)
        total=total+1
        wordlen=len(word)
        print("You will have 8 guesses for each word")
        rem_guess=8
        again=[]
        


        if wordlen==8:
            print("The word has 8 letters")
            blank=["-","-","-","-","-","-","-","-"]
            while rem_guess>0:
                if not "-" in blank:
                    print("Congrats!!! you have guessed correctly")
                    print()
                    count=count+1
                    
                    break
                guess=input("Enter any alphabet from a to z: ")
                print()
                if guess in again:
                    print("You have guessed this letter before: ")
                else:
                    again.append(guess)
                    if guess in word:
                        print("Right guess")
                    else:
                        print("Wrong guess")
                        print(blank)
                        rem_guess=rem_guess-1
                        print("you have only"+" " + str(rem_guess)+" " + "guesses remaining")
                        hangman(rem_guess)
                        if rem_guess==0:
                            print("The word was ", word)
                        print()
                    for i in range(8):
                                           
                        if word[i]==guess:
                            blank[i]=guess
                            print(blank)
                            print()
                            print ("you have"+" " +str(rem_guess)+" "+ "guesses remaining")
                            print()

        if wordlen==7:
            print("The word has 7 letters")
            blank=["-","-","-","-","-","-","-"]
            while rem_guess>0:
                if not "-" in blank:
                    print("Congrats!!! you have guessed correctly")
                    print()
                    count=count+1
                    break
                guess=input("Enter any alphabet from a to z: ")
                print()
                if guess in again:
                    print("You have guessed this letter before: ")
                else:
                    again.append(guess)
                    if guess in word:
                        print("Right guess")
                    else:
                        print("Wrong guess")
                        print(blank)
                        rem_guess=rem_guess-1
                        print("you have only"+" " + str(rem_guess)+" " + "guesses remaining")
                        hangman(rem_guess)
                        if rem_guess==0:
                            print("The word was ", word)
                        print()
                    for i in range(7):
                                           
                        if word[i]==guess:
                            blank[i]=guess
                            print(blank)
                            print()
                            print ("you have"+" " +str(rem_guess)+" "+ "guesses remaining")
                            print()

        if wordlen==6:
            print("The word has 6 letters")
            blank=["-","-","-","-","-","-"]
            while rem_guess>0:
                if not "-" in blank:
                    print("Congrats!!! you have guessed correctly")
                    print()
                    count=count+1
                    break
                guess=input("Enter any alphabet from a to z: ")
                print()
                if guess in again:
                    print("You have guessed this letter before: ")
                else:
                    again.append(guess)
                    if guess in word:
                        print("Right guess")
                    else:
                        print("Wrong guess")
                        print(blank)
                        rem_guess=rem_guess-1
                        print("you have only"+" " + str(rem_guess)+" " + "guesses remaining")
                        hangman(rem_guess)
                        if rem_guess==0:
                            print("The word was ", word)
                        print()
                    for i in range(6):
                                           
                        if word[i]==guess:
                            blank[i]=guess
                            print(blank)
                            print()
                            print ("you have"+" " +str(rem_guess)+" "+ "guesses remaining")
                            print()
        if wordlen==5:
            print("The word has 5 letters")
            blank=["-","-","-","-","-"]
            while rem_guess>0:
                if not "-" in blank:
                    print("Congrats!!! you have guessed correctly")
                    print()
                    count=count+1
                    break
                guess=input("Enter any alphabet from a to z: ")
                print()
                if guess in again:
                    print("You have guessed this letter before: ")
                else:
                    again.append(guess)
                    if guess in word:
                        print("Right guess")
                    else:
                        print("Wrong guess")
                        print(blank)
                        rem_guess=rem_guess-1
                        print("you have only"+" " + str(rem_guess)+" " + "guesses remaining")
                        hangman(rem_guess)
                        if rem_guess==0:
                            print("The word was ", word)
                        print()
                    for i in range(5):
                                           
                        if word[i]==guess:
                            blank[i]=guess
                            print(blank)
                            print()
                            print ("you have"+" " +str(rem_guess)+" "+ "guesses remaining")
                            print()

        if wordlen==4:
            print("The word has 4 letters")
            blank=["-","-","-","-"]
            while rem_guess>0:
                if not "-" in blank:
                    print("Congrats!!! you have guessed correctly")
                    print()
                    count=count+1
                    break
                guess=input("Enter any alphabet from a to z: ")
                print()
                if guess in again:
                    print("You have guessed this letter before: ")
                else:
                    again.append(guess)
                    if guess in word:
                        print("Right guess")
                    else:
                        print("Wrong guess")
                        print(blank)
                        rem_guess=rem_guess-1
                        print("you have only"+" " + str(rem_guess)+" " + "guesses remaining")
                        hangman(rem_guess)
                        if rem_guess==0:
                            print("The word was ", word)
                        print()
                    for i in range(4):
                                           
                        if word[i]==guess:
                            blank[i]=guess
                            print(blank)
                            print()
                            print ("you have"+" " +str(rem_guess)+" "+ "guesses remaining")
                            print()
        restart=input("Do you want to play the game again? y/n? ")
        if restart=="n":
            print("Your score is ", count, "out of" ,total)

game()


        
