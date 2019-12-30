#This is the second iteration of the old incomplete and inefficient TicTacToe Engine.
#This program will render a game of TicTacToe.
#Made by Siddhant Madhur.
#Version = 2.3

def endGameX(): #This function dictates that X is the winner of the Game.
    print("The game has ended")
    print("Winner is X")
    print("Congrats to " + nameX + " for winning!")
    exit()

def endGameO(): #This function dictates that O is the winner of the Game.
    print("The game has ended")
    print("Winner is O")
    print("Congrats to " + nameO + " for winning!")
    exit()

def pr(statement): #This is an option function because all it does is make it so instead of writing print again and again I can just write pr
    print(statement)

def showTable():
    pr(" " + TL + " | " + TM + " | " + TR + " ")
    pr(" " + ML + " | " + MM + " | " + MR + " ")
    pr(" " + BL + " | " + BM + " | " + BR + " ")

def displayError(errorMessage): #Since this program uses a lot of if and elif statements, all that else statements carry is a displayError message
    print("THERE IS AN ERROR")
    print("ERROR MESSAGE: " + errorMessage)
    print("PLEASE CONSULT README.TXT")
    exit()

def convert(list):
    return tuple(list)

def checkGame(): #Checks whether all the possible win combinations have occured yet.
    if TL == "X" and TM == "X" and TR == "X":
        endGameX()
    elif ML == "X" and MM == "X" and MR == "X":
        endGameX()
    elif BL == "X" and BM == "X" and BR == "X":
        endGameX()
    elif TL == "X" and ML == "X" and BL == "X":
        endGameX()
    elif TR == "X" and MR == "X" and BR == "X":
        endGameX()
    elif TM == "X" and MM == "X" and BM == "X":
        endGameX()
    elif TL == "X" and MM == "X" and BR == "X":
        endGameX()
    elif TR == "X" and MM == "X" and BL == "X":
        endGameX()
    elif TL == "O" and TM == "O" and TR == "O":
        endGameO()
    elif ML == "O" and MM == "O" and MR == "O":
        endGameO()
    elif BL == "O" and BM == "O" and BR == "O":
        endGameO()
    elif TL == "O" and ML == "O" and BL == "O":
        endGameO()
    elif TR == "O" and MR == "O" and BR == "O":
        endGameO()
    elif TM == "O" and MM == "O" and BM == "O":
        endGameO()
    elif TL == "O" and MM == "O" and BR == "O":
        endGameO()
    elif TR == "O" and MM == "O" and BL == "O":
        endGameO()

pr("WARNING: VERY INEFFICIENT!!!!")
pr("MAY HAVE GLITCHES.")
pr("For errors or any doubt please email: siddhant.madhur@gmail.com")
pr("Copyright: siddhantmadhur on GitHub")

#Top Row:
TL = "_"
TM = "_"
TR = "_"
#Middle Row:
ML = "_"
MM = "_"
MR = "_"
#Bottom Row:
BL = "_"
BM = "_"
BR = "_"

#template = "_ | _ | _"
pr("Hello Player 1 and Player 2,")
pr("To make it feel personal might i ask you to give your name.")
pr("Lets start with Player 1, what is your name?")
playername1 = input()
pr("Player 2, What is your name?")
playername2 = input()

pr("Ok lets start, "+playername1+" and "+ playername2)

pr(" 1 | 2 | 3")
pr(" 4 | 5 | 6")
pr(" 7 | 8 | 9")


pr("Would Player 1 like to be X or O?")
Player1 = input()

if Player1 == "X":
    turn = ["X", "O"]
    nameX = playername1
    nameO = playername2
elif Player1 == "O":
    turn = ["O", "X"]
    nameO = playername1
    nameX = playername2
else:
    displayError("Error 104")

showTable()

pr(playername1 + " is startting....\nWhich number would you like to replace?")

firstMove = input("Number = ")

if firstMove == "1":
    if TL == "_":
        TL = turn[0]
    elif TL == "X" or TL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif firstMove == "2":
    if TM == "_":
        TM = turn[0]
    elif TM == "X" or TM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif firstMove == "3":
    if TR == "_":
        TR = turn[0]
    elif TR == "X" or TR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif firstMove == "4":
    if ML == "_":
        ML = turn[0]
    elif ML == "X" or ML == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif firstMove == "5":
    if MM == "_":
        MM = turn[0]
    elif MM == "X" or MM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif firstMove == "6":
    if MR == "_":
        MR = turn[0]
    elif MR == "X" or MR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif firstMove == "7":
    if BL == "_":
        BL = turn[0]
    elif BL == "X" or BL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif firstMove == "8":
    if BM == "_":
        BM = turn[0]
    elif BM == "X" or BM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif firstMove == "9":
    if BR == "_":
        BR = turn[0]
    elif BR == "X" or BR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
else:
    displayError("Please type a number from 1 to 9 only")

showTable()

checkGame()

pr(turn[1]+" is playing now...")

secondMove = input("Number = ")

if secondMove == "1":
    if TL == "_":
        TL = turn[1]
    elif TL == "X" or TL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif secondMove == "2":
    if TM == "_":
        TM = turn[1]
    elif TM == "X" or TM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif secondMove == "3":
    if TR == "_":
        TR = turn[1]
    elif TR == "X" or TR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif secondMove == "4":
    if ML == "_":
        ML = turn[1]
    elif ML == "X" or ML == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif secondMove == "5":
    if MM == "_":
        MM = turn[1]
    elif MM == "X" or MM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif secondMove == "6":
    if MR == "_":
        MR = turn[1]
    elif MR == "X" or MR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif secondMove == "7":
    if BL == "_":
        BL = turn[1]
    elif BL == "X" or BL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif secondMove == "8":
    if BM == "_":
        BM = turn[1]
    elif BM == "X" or BM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif secondMove == "9":
    if BR == "_":
        BR = turn[1]
    elif BR == "X" or BR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
else:
    displayError("Please type a number from 1 to 9 only")


showTable()

checkGame()

pr(turn[0] + " is playing now...")

thirdMove = input("Number = ")

if thirdMove == "1":
    if TL == "_":
        TL = turn[0]
    elif TL == "X" or TL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif thirdMove == "2":
    if TM == "_":
        TM = turn[0]
    elif TM == "X" or TM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif thirdMove == "3":
    if TR == "_":
        TR = turn[0]
    elif TR == "X" or TR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif thirdMove == "4":
    if ML == "_":
        ML = turn[0]
    elif ML == "X" or ML == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif thirdMove == "5":
    if MM == "_":
        MM = turn[0]
    elif MM == "X" or MM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif thirdMove == "6":
    if MR == "_":
        MR = turn[0]
    elif MR == "X" or MR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif thirdMove == "7":
    if BL == "_":
        BL = turn[0]
    elif BL == "X" or BL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif thirdMove == "8":
    if BM == "_":
        BM = turn[0]
    elif BM == "X" or BM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif thirdMove == "9":
    if BR == "_":
        BR = turn[0]
    elif BR == "X" or BR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
else:
    displayError("Please type a number from 1 to 9 only")

showTable()

checkGame()

pr(turn[1]+" is playing now...")

fourthMove = input("Number = ")

if fourthMove == "1":
    if TL == "_":
        TL = turn[1]
    elif TL == "X" or TL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fourthMove == "2":
    if TM == "_":
        TM = turn[1]
    elif TM == "X" or TM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fourthMove == "3":
    if TR == "_":
        TR = turn[1]
    elif TR == "X" or TR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fourthMove == "4":
    if ML == "_":
        ML = turn[1]
    elif ML == "X" or ML == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fourthMove == "5":
    if MM == "_":
        MM = turn[1]
    elif MM == "X" or MM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fourthMove == "6":
    if MR == "_":
        MR = turn[1]
    elif MR == "X" or MR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fourthMove == "7":
    if BL == "_":
        BL = turn[1]
    elif BL == "X" or BL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fourthMove == "8":
    if BM == "_":
        BM = turn[1]
    elif BM == "X" or BM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fourthMove == "9":
    if BR == "_":
        BR = turn[1]
    elif BR == "X" or BR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
else:
    displayError("Please type a number from 1 to 9 only")

showTable()

checkGame()

pr(turn[0] + " is playing now...")

fifthMove = input("Number = ")

if fifthMove == "1":
    if TL == "_":
        TL = turn[0]
    elif TL == "X" or TL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fifthMove == "2":
    if TM == "_":
        TM = turn[0]
    elif TM == "X" or TM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fifthMove == "3":
    if TR == "_":
        TR = turn[0]
    elif TR == "X" or TR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fifthMove == "4":
    if ML == "_":
        ML = turn[0]
    elif ML == "X" or ML == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fifthMove == "5":
    if MM == "_":
        MM = turn[0]
    elif MM == "X" or MM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fifthMove == "6":
    if MR == "_":
        MR = turn[0]
    elif MR == "X" or MR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fifthMove == "7":
    if BL == "_":
        BL = turn[0]
    elif BL == "X" or BL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fifthMove == "8":
    if BM == "_":
        BM = turn[0]
    elif BM == "X" or BM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif fifthMove == "9":
    if BR == "_":
        BR = turn[0]
    elif BR == "X" or BR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
else:
    displayError("Please type a number from 1 to 9 only")

showTable()

checkGame()

pr(turn[1] + " is playing now...")

sixthMove = input("Number = ")

if sixthMove == "1":
    if TL == "_":
        TL = turn[1]
    elif TL == "X" or TL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sixthMove == "2":
    if TM == "_":
        TM = turn[1]
    elif TM == "X" or TM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sixthMove == "3":
    if TR == "_":
        TR = turn[1]
    elif TR == "X" or TR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sixthMove == "4":
    if ML == "_":
        ML = turn[1]
    elif ML == "X" or ML == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sixthMove == "5":
    if MM == "_":
        MM = turn[1]
    elif MM == "X" or MM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sixthMove == "6":
    if MR == "_":
        MR = turn[1]
    elif MR == "X" or MR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sixthMove == "7":
    if BL == "_":
        BL = turn[1]
    elif BL == "X" or BL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sixthMove == "8":
    if BM == "_":
        BM = turn[1]
    elif BM == "X" or BM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sixthMove == "9":
    if BR == "_":
        BR = turn[1]
    elif BR == "X" or BR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
else:
    displayError("Please type a number from 1 to 9 only")

showTable()

checkGame()

pr(turn[0] + " is playing now...")

sevenMove = input("Number = ")

if sevenMove == "1":
    if TL == "_":
        TL = turn[0]
    elif TL == "X" or TL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sevenMove == "2":
    if TM == "_":
        TM = turn[0]
    elif TM == "X" or TM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sevenMove == "3":
    if TR == "_":
        TR = turn[0]
    elif TR == "X" or TR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sevenMove == "4":
    if ML == "_":
        ML = turn[0]
    elif ML == "X" or ML == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sevenMove == "5":
    if MM == "_":
        MM = turn[0]
    elif MM == "X" or MM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sevenMove == "6":
    if MR == "_":
        MR = turn[0]
    elif MR == "X" or MR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sevenMove == "7":
    if BL == "_":
        BL = turn[0]
    elif BL == "X" or BL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sevenMove == "8":
    if BM == "_":
        BM = turn[0]
    elif BM == "X" or BM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif sevenMove == "9":
    if BR == "_":
        BR = turn[0]
    elif BR == "X" or BR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
else:
    displayError("Please type a number from 1 to 9 only")

showTable()

checkGame()

pr(turn[1] + " is playing now...")

eigthMove = input("Number = ")

if eighthMove == "1":
    if TL == "_":
        TL = turn[1]
    elif TL == "X" or TL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif eighthMove == "2":
    if TM == "_":
        TM = turn[1]
    elif TM == "X" or TM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif eighthMove == "3":
    if TR == "_":
        TR = turn[1]
    elif TR == "X" or TR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif eighthMove == "4":
    if ML == "_":
        ML = turn[1]
    elif ML == "X" or ML == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif eighthMove == "5":
    if MM == "_":
        MM = turn[1]
    elif MM == "X" or MM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif Move == "6":
    if MR == "_":
        MR = turn[1]
    elif MR == "X" or MR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif eighthMove == "7":
    if BL == "_":
        BL = turn[1]
    elif BL == "X" or BL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif eighthMove == "8":
    if BM == "_":
        BM = turn[1]
    elif BM == "X" or BM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif eighthMove == "9":
    if BR == "_":
        BR = turn[1]
    elif BR == "X" or BR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
else:
    displayError("Please type a number from 1 to 9 only")

showTable()

checkGame()

pr(turn[0] + " is playing now...")

ninthMove = input("Number = ")

if ninthMove == "1":
    if TL == "_":
        TL = turn[0]
    elif TL == "X" or TL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif ninthMove == "2":
    if TM == "_":
        TM = turn[0]
    elif TM == "X" or TM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif ninthMove == "3":
    if TR == "_":
        TR = turn[0]
    elif TR == "X" or TR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif ninthMove == "4":
    if ML == "_":
        ML = turn[0]
    elif ML == "X" or ML == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif ninthMove == "5":
    if MM == "_":
        MM = turn[0]
    elif MM == "X" or MM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif ninthMove == "6":
    if MR == "_":
        MR = turn[0]
    elif MR == "X" or MR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif ninthMove == "7":
    if BL == "_":
        BL = turn[0]
    elif BL == "X" or BL == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif ninthMove == "8":
    if BM == "_":
        BM = turn[0]
    elif BM == "X" or BM == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
elif ninthMove == "9":
    if BR == "_":
        BR = turn[0]
    elif BR == "X" or BR == "O":
        pr("Collision Detected! As penalty your move is being skipped....")
    else:
        displayError("Error Code 100")
else:
    displayError("Please type a number from 1 to 9 only")

showTable()

checkGame()

print("The Game has ended as a tie now.")
