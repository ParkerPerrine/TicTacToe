#SmarterTic_Tac_Toe.py
#Record Game
#CS_190
#Parker Perrine, Beck Heidmous

import random


#constants - but Python doesn't really have constants
EMPTY = " "
BAR = "|"
X = "X"
O = "O"


#functions    
def printInstructions():
    print("Tic Tac Toe")
    printDashes()
    print("You play first using X")
    print("Positions indexes begin with 1 (not 0)")
    print("The computer plays randomly using O")
    
def printDashes(n=30):
    DASH = "-"
    for i in range(n):
        print(DASH, end='')
    print()

def printTable(t):
    print()
    for row in range(3):
        for col in range(3):
            if col != 2:
                print(t[row][col], BAR, end='')
            else:
                print(t[row][col])
        if row != 2:
            printDashes(8)
    print()

def checkForTie(tbl):
    count = 0
    tie = False
    for r in range(0,3):
        for c in range(0,3):
            if tbl[r][c] == EMPTY:
                count +=1
    if count == 0:
        return True
    return False
'-------------------------------------------------------------------------'       

def getPlayerMove(tbl):
    move = False

    
    if tbl[0][0] == X and tbl[0][1] == X and tbl[0][2] == EMPTY:
        return 0, 2

    if tbl[0][1] == X and tbl[0][2] == X and tbl[0][0] == EMPTY:
        return 0, 0

    if tbl[0][0] == X and tbl[0][2] == X and tbl[0][1] == EMPTY:
        return 0, 1

    if tbl[1][0] == X and tbl[1][1] == X and tbl[1][2] == EMPTY:
        return 1, 2

    if tbl[1][1] == X and tbl[1][2] == X and tbl[1][0] == EMPTY:
        return 1, 0

    if tbl[1][0] == X and tbl[1][2] == X and tbl[1][1] == EMPTY:
        return 1, 1

    if tbl[2][0] == X and tbl[2][1] == X and tbl[2][2] == EMPTY:
        return 2, 2

    if tbl[2][1] == X and tbl[2][2] == X and tbl[2][0] == EMPTY:
        return 2, 0

    if tbl[2][0] == X and tbl[2][2] == X and tbl[2][1] == EMPTY:
        return 2, 1

    if tbl[0][0] == X and tbl[1][1] == X and tbl[2][2] == EMPTY:
        return 2, 2

    if tbl[1][1] == X and tbl[2][2] == X and tbl[0][0] == EMPTY:
        return 0, 0

    if tbl[0][0] == X and tbl[2][2] == X and tbl[1][1] == EMPTY:
        return 1, 1

    if tbl[0][2] == X and tbl[1][1] == X and tbl[2][0] == EMPTY:
        return 2, 0

    if tbl[1][1] == X and tbl[2][0] == X and tbl[0][2] == EMPTY:
        return 0, 2

    if tbl[0][2] == X and tbl[2][0] == X and tbl[1][1] == EMPTY:
        return 1, 1

    if tbl[0][0] == X and tbl[1][0] == X and tbl[2][0] == EMPTY:
        return 2, 0

    if tbl[0][0] == X and tbl[2][0] == X and tbl[1][0] == EMPTY:
        return 1, 0

    if tbl[1][0] == X and tbl[2][0] == X and tbl[0][0] == EMPTY:
        return 0, 0

    if tbl[0][1] == X and tbl[1][1] == X and tbl[2][1] == EMPTY:
        return 2, 1

    if tbl[0][1] == X and tbl[2][1] == X and tbl[1][1] == EMPTY:
         return 1, 1

    if tbl[1][1] == X and tbl[2][1] == X and tbl[0][1] == EMPTY:
         return 0, 1

    if tbl[0][2] == X and tbl[1][2] == X and tbl[2][2] == EMPTY:
        return 2, 2

    if tbl[0][2] == X and tbl[2][2] == X and tbl[1][2] == EMPTY:
        return 1, 2

    if tbl[1][2] == X and tbl[2][2] == X and tbl[0][2] == EMPTY:
        return 0, 2

    if tbl[0][0] == O and tbl[0][1] == O and tbl[0][2] == EMPTY:
        return 0, 2

    if tbl[0][1] == O and tbl[0][2] == O and tbl[0][0] == EMPTY:
        return 0, 0

    if tbl[0][0] == O and tbl[0][2] == O and tbl[0][1] == EMPTY:
        return 0, 1

    if tbl[1][0] == O and tbl[1][1] == O and tbl[1][2] == EMPTY:
        return 1, 2

    if tbl[1][1] == O and tbl[1][2] == O and tbl[1][0] == EMPTY:
        return 1, 0

    if tbl[1][0] == O and tbl[1][2] == O and tbl[1][1] == EMPTY:
        return 1, 1

    if tbl[2][0] == O and tbl[2][1] == O and tbl[2][2] == EMPTY:
        return 2, 2

    if tbl[2][1] == O and tbl[2][2] == O and tbl[2][0] == EMPTY:
        return 2, 0

    if tbl[2][0] == O and tbl[2][2] == O and tbl[2][1] == EMPTY:
        return 2, 1

    if tbl[0][0] == O and tbl[1][1] == O and tbl[2][2] == EMPTY:
        return 2, 2

    if tbl[1][1] == O and tbl[2][2] == O and tbl[0][0] == EMPTY:
        return 0, 0

    if tbl[0][0] == O and tbl[2][2] == O and tbl[1][1] == EMPTY:
        return 1, 1

    if tbl[0][2] == O and tbl[1][1] == O and tbl[2][0] == EMPTY:
        return 2, 0

    if tbl[1][1] == O and tbl[2][0] == O and tbl[0][2] == EMPTY:
        return 0, 2

    if tbl[0][2] == O and tbl[2][0] == O and tbl[1][1] == EMPTY:
        return 1, 1

    if tbl[0][0] == O and tbl[1][0] == O and tbl[2][0] == EMPTY:
        return 2, 0

    if tbl[0][0] == O and tbl[2][0] == O and tbl[1][0] == EMPTY:
        return 1, 0

    if tbl[1][0] == O and tbl[2][0] == O and tbl[0][0] == EMPTY:
        return 0, 0

    if tbl[0][1] == O and tbl[1][1] == O and tbl[2][1] == EMPTY:
        return 2, 1

    if tbl[0][1] == O and tbl[2][1] == O and tbl[1][1] == EMPTY:
         return 1, 1

    if tbl[1][1] == O and tbl[2][1] == O and tbl[0][1] == EMPTY:
         return 0, 1

    if tbl[0][2] == O and tbl[1][2] == O and tbl[2][2] == EMPTY:
        return 2, 2

    if tbl[0][2] == O and tbl[2][2] == O and tbl[1][2] == EMPTY:
        return 1, 2

    if tbl[1][2] == O and tbl[2][2] == O and tbl[0][2] == EMPTY:
        return 0, 2
    else:
        while move == False:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if tbl[r][c] != X and tbl[r][c] != O:
                move = True     
        return r, c
'-------------------------------------------------------------------------'       

    
#------------------------------------------------------------------------#
def getComputerMove(tbl):
    goodMove = False

    if tbl[0][0] == X and tbl[0][1] == X and tbl[0][2] == EMPTY:
        return 0, 2

    if tbl[0][1] == X and tbl[0][2] == X and tbl[0][0] == EMPTY:
        return 0, 0

    if tbl[0][0] == X and tbl[0][2] == X and tbl[0][1] == EMPTY:
        return 0, 1

    if tbl[1][0] == X and tbl[1][1] == X and tbl[1][2] == EMPTY:
        return 1, 2

    if tbl[1][1] == X and tbl[1][2] == X and tbl[1][0] == EMPTY:
        return 1, 0

    if tbl[1][0] == X and tbl[1][2] == X and tbl[1][1] == EMPTY:
        return 1, 1

    if tbl[2][0] == X and tbl[2][1] == X and tbl[2][2] == EMPTY:
        return 2, 2

    if tbl[2][1] == X and tbl[2][2] == X and tbl[2][0] == EMPTY:
        return 2, 0

    if tbl[2][0] == X and tbl[2][2] == X and tbl[2][1] == EMPTY:
        return 2, 1

    if tbl[0][0] == X and tbl[1][1] == X and tbl[2][2] == EMPTY:
        return 2, 2

    if tbl[1][1] == X and tbl[2][2] == X and tbl[0][0] == EMPTY:
        return 0, 0

    if tbl[0][0] == X and tbl[2][2] == X and tbl[1][1] == EMPTY:
        return 1, 1

    if tbl[0][2] == X and tbl[1][1] == X and tbl[2][0] == EMPTY:
        return 2, 0

    if tbl[1][1] == X and tbl[2][0] == X and tbl[0][2] == EMPTY:
        return 0, 2

    if tbl[0][2] == X and tbl[2][0] == X and tbl[1][1] == EMPTY:
        return 1, 1

    if tbl[0][0] == X and tbl[1][0] == X and tbl[2][0] == EMPTY:
        return 2, 0

    if tbl[0][0] == X and tbl[2][0] == X and tbl[1][0] == EMPTY:
        return 1, 0

    if tbl[1][0] == X and tbl[2][0] == X and tbl[0][0] == EMPTY:
        return 0, 0

    if tbl[0][1] == X and tbl[1][1] == X and tbl[2][1] == EMPTY:
        return 2, 1

    if tbl[0][1] == X and tbl[2][1] == X and tbl[1][1] == EMPTY:
         return 1, 1

    if tbl[1][1] == X and tbl[2][1] == X and tbl[0][1] == EMPTY:
         return 0, 1

    if tbl[0][2] == X and tbl[1][2] == X and tbl[2][2] == EMPTY:
        return 2, 2

    if tbl[0][2] == X and tbl[2][2] == X and tbl[1][2] == EMPTY:
        return 1, 2

    if tbl[1][2] == X and tbl[2][2] == X and tbl[0][2] == EMPTY:
        return 0, 2

    
#------------------------------Zero attempts to win-----------------------------------------#

    if tbl[0][0] == O and tbl[0][1] == O and tbl[0][2] == EMPTY:
        return 0, 2

    if tbl[0][1] == O and tbl[0][2] == O and tbl[0][0] == EMPTY:
        return 0, 0

    if tbl[0][0] == O and tbl[0][2] == O and tbl[0][1] == EMPTY:
        return 0, 1

    if tbl[1][0] == O and tbl[1][1] == O and tbl[1][2] == EMPTY:
        return 1, 2

    if tbl[1][1] == O and tbl[1][2] == O and tbl[1][0] == EMPTY:
        return 1, 0

    if tbl[1][0] == O and tbl[1][2] == O and tbl[1][1] == EMPTY:
        return 1, 1

    if tbl[2][0] == O and tbl[2][1] == O and tbl[2][2] == EMPTY:
        return 2, 2

    if tbl[2][1] == O and tbl[2][2] == O and tbl[2][0] == EMPTY:
        return 2, 0

    if tbl[2][0] == O and tbl[2][2] == O and tbl[2][1] == EMPTY:
        return 2, 1

    if tbl[0][0] == O and tbl[1][1] == O and tbl[2][2] == EMPTY:
        return 2, 2

    if tbl[1][1] == O and tbl[2][2] == O and tbl[0][0] == EMPTY:
        return 0, 0

    if tbl[0][0] == O and tbl[2][2] == O and tbl[1][1] == EMPTY:
        return 1, 1

    if tbl[0][2] == O and tbl[1][1] == O and tbl[2][0] == EMPTY:
        return 2, 0

    if tbl[1][1] == O and tbl[2][0] == O and tbl[0][2] == EMPTY:
        return 0, 2

    if tbl[0][2] == O and tbl[2][0] == O and tbl[1][1] == EMPTY:
        return 1, 1

    if tbl[0][0] == O and tbl[1][0] == O and tbl[2][0] == EMPTY:
        return 2, 0

    if tbl[0][0] == O and tbl[2][0] == O and tbl[1][0] == EMPTY:
        return 1, 0

    if tbl[1][0] == O and tbl[2][0] == O and tbl[0][0] == EMPTY:
        return 0, 0

    if tbl[0][1] == O and tbl[1][1] == O and tbl[2][1] == EMPTY:
        return 2, 1

    if tbl[0][1] == O and tbl[2][1] == O and tbl[1][1] == EMPTY:
         return 1, 1

    if tbl[1][1] == O and tbl[2][1] == O and tbl[0][1] == EMPTY:
         return 0, 1

    if tbl[0][2] == O and tbl[1][2] == O and tbl[2][2] == EMPTY:
        return 2, 2

    if tbl[0][2] == O and tbl[2][2] == O and tbl[1][2] == EMPTY:
        return 1, 2

    if tbl[1][2] == O and tbl[2][2] == O and tbl[0][2] == EMPTY:
        return 0, 2
#-----------------------------------------------------------------------#
    else:
        while goodMove == False:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
            if tbl[r][c] != X and tbl[r][c] != O:
                goodMove = True     
        return r, c

#------------------------------------------------------------------------#


def recordPlayerMove(tbl, r, c):
    tbl[r][c] = X
    
def recordComputerMove(tbl, r, c):
    tbl[r][c] = O
    
def checkRow(tr, mark):
    for v in tr:
        if v != mark:
            return False
    return True

def checkCol(t, col, mark):
    for i in range(3):
        if t[i][col] != mark:
            return False
    return True

#********** define your diagonal checking here

def CheckDiag(tbl, mark):
    count = 0
    for i in range(0, 3, 1):
        if tbl[i][i] == mark:
            count = count + 1
    if count == 3:
        return True
    count = 0
    if tbl[0][2] == mark:
        count += 1
    if tbl[1][1] == mark:
        count+= 1
    if tbl[2][0] == mark:
        count += 1
    if count == 3:
        return True
    return False


#********** define your diagonal checking here
def CheckFor3s(tbl):
    #check rows
    if checkRow(tbl[0], X):
        return X
    if checkRow(tbl[1], X):
        return X
    if checkRow(tbl[2], X):
        return X
    if checkRow(tbl[0], O):
        return O
    if checkRow(tbl[1], O):
        return O
    if checkRow(tbl[2], O):
        return O
    #check columns
    if checkCol(tbl, 0, X):
        return X
    if checkCol(tbl, 1, X):
        return X
    if checkCol(tbl, 2, X):
        return X
     #check rows 0
    if checkRow(tbl[0], O):
        return O
    if checkRow(tbl[1], O):
        return O 
    if checkRow(tbl[2], O):
        return O
    if checkRow(tbl[0], X):
        return X
    if checkRow(tbl[1], X):
        return X
    if checkRow(tbl[2], X):
        return X
    #check columns 0
    if checkCol(tbl, 0, O):
        return O
    if checkCol(tbl, 1, O):
        return O
    if checkCol(tbl, 2, O):
        return O
   #Check Diag
    if CheckDiag(tbl,X):
        return X
    if CheckDiag(tbl, O):
        return O
    
    #********** check diagonals
    #you need to write the function calls for checking diagonals
    #for X and O, and to define the function itself where
    #indicated above

    #no winner
    
    

#main part of the program
random.seed() #different sequence of randoms each run, so the
              #game plays differently every time

printInstructions()
table = [[EMPTY for i in range(3)] for i in range(3)]
printTable(table)
printDashes(60)
    
gameOver = False
while gameOver == False:
    print("Player move: ")
    r, c = getPlayerMove(table)
    recordPlayerMove(table, r, c)
    printTable(table)
    ToeArchive = open('Game.txt', 'a')
    ToeArchive.write("Player: X at " + str(r + 1) + ", " + str(c + 1) + '\n')


    tie = checkForTie(table)
    print()
    if tie == True:
        print("Draw!")
        gameOver = True
        break
    print("Computer move: ")
    r, c = getComputerMove(table)
    recordComputerMove(table, r, c)
    printTable(table)
    ToeArchive = open('Game.txt', 'a')
    ToeArchive.write("Computer: O at " + str(r + 1) + ", " + str(c + 1) + '\n')    

    winningPlayer = CheckFor3s(table)
    

    if winningPlayer == X:
        print("Player X Has Won This Round")
        gameOver = True
    elif winningPlayer == O:
        print("Player 0 Has Won This Round")
        gameOver = True
    else:
        print()
        print("No winner yet")
    printDashes(60)

print('To check game files open the Game.txt File')
        
        
        
