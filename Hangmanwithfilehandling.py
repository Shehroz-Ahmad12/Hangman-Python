# hangman

import random

name=input("Please enter your name: ")
print("Welcome to hangman", name)

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

        print("The word has",wordlen,"letter")
        blank= "-"*len(word)
        blank=list(blank)
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
                for i in range(len(word)):
                                           
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
