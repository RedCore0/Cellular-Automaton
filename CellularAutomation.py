#This script controls user's input. And prints current state of the board

#imports all the necessary modules
import os
import time
from GameOfLife import LifeSimulation

#Cell is a single point on board
class Cell:
    def __init__(self, alive, visual) -> None:
        self.alive = alive
        self.visual = visual

#Creates 2 dimentional board made out of cells
Board = []
def CreateBoard():
    global BoardSize
    try:
        BoardSize = int(input("Board size   MIN(10)/MAX(100): "))
    except:
        CreateBoard()
        return
    RowRecursion = 0
    if BoardSize > 9 and BoardSize < 101:
        while RowRecursion < BoardSize:
            Column = []
            ColumnRecursion = 0
            while ColumnRecursion < BoardSize:
                NewCell = Cell(False, " · ")
                Column.append(NewCell)
                ColumnRecursion+=1
            Board.append(Column)
            RowRecursion+=1
        ColumnIndex()
        PrintBoard()
        CreateLife()
    else: CreateBoard()

#Creates string showing column's index at the top of the board
ColumnCount = ""
def ColumnIndex():
    print(BoardSize)
    global ColumnCount
    Index = 0
    while(Index < BoardSize):
        Number = ""
        if Index < 10:
            Number = (" " + str(Index) + " ")
        else:
            Number = (" "+ str(Index))
        ColumnCount+=str(Number)
        Index+=1

#Allows user to modify cells on the board before starting simulation
#needs cleaning
HERE = os.path.dirname(os.path.abspath(__file__))
def CreateLife():
    BoardLayout = input("Create new Layout: a   Load Existing Layout: b \n")
    if BoardLayout == "a":
        FileName = input("Name: ")
        Continue = True
        while Continue:
            try:
                y = int(input("Row: "))
                x = int(input("Column: "))
            except:
                continue
            with open(HERE+"/Saves/"+FileName+".txt", "a+") as f:
                f.write(str(y)+" "+str(x)+"\n")
            Board[y][x].alive = True
            Board[y][x].visual = " ■ "        
            PrintBoard()
            RepeatInput = True
            while(RepeatInput):
                DoContinue = input("Choose another cell?    y/n \n: ")
                if(DoContinue == "y"):
                    RepeatInput = False
                elif(DoContinue == "n"):
                    Continue = False
                    RepeatInput = False
                else:
                    print("invalid input")
    elif BoardLayout == "b":
        Again = True
        while Again:
            Continue = False
            SaveName = input("Layout name: ")
            with open(HERE+"/Saves/"+SaveName+".txt", "r") as f:
                for i in f.readlines():
                    x = i.split()
                    if int(x[0]) > len(Board[0]): 
                        print("Board too small for this layout")
                        Continue = True
                        break
                    elif int(x[1]) > len(Board[0]):
                        print("Board too small for this layout")
                        Continue = True
                        break
                    Board[int(x[0])][int(x[1])].alive = True
                    Board[int(x[0])][int(i[1])].visual = " ■ "
                if Continue == True: CreateLife()
                Again = False
    else:
        CreateLife()

    time.sleep(1)

#Runs Simulation
def StartLifeSimulation():
    global Board
    while True:
        Board = LifeSimulation(BoardSize, Board)
        PrintBoard()
        time.sleep(.5)

#prints board
def PrintBoard():
    os.system("cls")
    RowID = 0
    for r in Board:
        if Board.index(r) == 0: print("    ",ColumnCount,"\n", RowID, "  ", end="")
        elif Board.index(r) < 10: print("\n", RowID, "  ", end="")
        else: print("\n", RowID, " ",end="")
        RowID+=1
        for c in r:
            print(c.visual, end="")
    print("")

CreateBoard()
StartLifeSimulation()