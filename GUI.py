
def hangman(rem_guess):
    if rem_guess==8:
        print("      ---------   ")
        print("     |/       |   ")
        print("     |            ")
        print("     |            ")
        print("     |            ")
        print("     |            ")
        print("     |            ")
        print(" ____|____        ")


    if rem_guess==7:
        print("      ---------   ")
        print("     |/       |   ")
        print("     |       (_)  ")
        print("     |            ")
        print("     |            ")
        print("     |            ")
        print("     |            ")
        print(" ____|____        ")

    if rem_guess==6:
        print("      ---------   ")
        print("     |/       |   ")
        print("     |       (_)  ")
        print("     |        |   ")
        print("     |        |   ")
        print("     |            ")
        print("     |            ")
        print(" ____|____        ")

    if rem_guess==5:

        print("      ---------   ")
        print("     |/       |   ")
        print("     |       (_)  ")
        print("     |       \|   ")
        print("     |        |   ")
        print("     |            ")
        print("     |            ")
        print(" ____|____        ")

    if rem_guess==4:
        print("      ---------   ")
        print("     |/       |   ")
        print("     |       (_)  ")
        print("     |       \|/  ")
        print("     |        |   ")
        print("     |            ")
        print("     |            ")
        print(" ____|____        ")

    if rem_guess==3:
        print("      ---------   ")
        print("     |/       |   ")
        print("     |       (_)  ")
        print("     |       \|/  ")
        print("     |        |   ")
        print("     |       /    ")
        print("     |            ")
        print(" ____|____        ")

    if rem_guess==2:
        print("      ---------   ")
        print("     |/       |   ")
        print("     |       (_)  ")
        print("     |       \|/  ")
        print("     |        |   ")
        print("     |       / \ ")
        print("     |            ")
        print(" ____|____        ")

    if rem_guess==1:
        print("      ---------   ")
        print("     |/       |   ")
        print("     |       (_)  ")
        print("     |       \|/  ")
        print("     |        |   ")
        print("     |      _/ \  ")
        print("     |            ")
        print(" ____|____        ")

    if rem_guess==0:
        print("      ---------   ")
        print("     |/       |   ")
        print("     |       (_)  ")
        print("     |       \|/  ")
        print("     |        |   ")
        print("     |      _/ \_ ")
        print("     |            ")
        print(" ____|____        ")
        print()
        print("You Lose")

