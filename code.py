from numpy.random import choice

result=choice(["Rock","Paper","Scissors"])


player = False

while player == False:
    player = input("Rock, Paper, Scissors?")
    if player == result:
        print("Computer Choose ",result)
        print("Tie!")
    elif player == "Rock":
        if result == "Paper":
            print("Computer Choose ",result)
            print("You lose!", "[0 1 0]")
        else:
            print("Computer Choose ",result)
            print("You win!", "1 0 0")
    elif player == "Paper":
        if result == "Scissors":
            print("Computer Choose ",result)
            print("You lose!", result, "cut", player)
        else:
            print("Computer Choose ",result)
            print("You win!", "0 1 0")
    elif player == "Scissors":
        if result == "Rock":
            print("Computer Choose ",result)
            print("You lose...", result, "smashes", player)
        else:
            print("Computer Choose ",result)
            print("You win!", player, "cut", result)
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    result=choice(["Rock","Paper","Scissors"])

