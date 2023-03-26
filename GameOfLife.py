import os
import time
import copy
class Cell:
    def __init__(self, alive, visual) -> None:
        self.alive = alive
        self.visual = visual

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
    else: CreateBoard()

def CreateLife():
    Continue = True
    while Continue:
        try:
            y = int(input("Row: "))
            x = int(input("Column: "))
        except:
            continue
        Board[y][x].alive = True
        Board[y][x].visual = " ■ "
        RepeatInput = True
        while(RepeatInput):
            DoContinue = input("Choose another cell?    y/n \n: ")
            if(DoContinue == "y"):
                PrintBoard()
                RepeatInput = False
            elif(DoContinue == "n"):
                RepeatInput = False
            else:
                print("invalid input")

    PrintBoard()
    time.sleep(1)

def LifeSimulation():
    global Board
    ToUpdate = copy.deepcopy(Board)
    for r in Board:
        for c in r:
            LivingCells = 0
            if r.index(c)-1 > -1 and r[r.index(c)-1].alive == True:
                LivingCells+=1
            if r.index(c)+1 < BoardSize and r[r.index(c)+1].alive == True:
                LivingCells+=1

            UpBoard = Board.index(r)-1
            DownBoard = Board.index(r)+1
            AdjacentRows = [UpBoard, DownBoard]

            for row in AdjacentRows:
                if row == UpBoard and UpBoard < 0: continue
                elif DownBoard > BoardSize-1: continue

                if Board[row][r.index(c)].alive == True:
                    LivingCells+=1
                if Board[row][r.index(c)-1].alive == True:
                    LivingCells+=1
                if r.index(c)+1<BoardSize and Board[row][r.index(c)+1].alive == True:
                    LivingCells+=1

            if LivingCells < 2 or LivingCells > 3:
                ToUpdate[Board.index(r)][r.index(c)].alive = False
                ToUpdate[Board.index(r)][r.index(c)].visual = " · "
            elif LivingCells == 3:
                ToUpdate[Board.index(r)][r.index(c)].alive = True
                ToUpdate[Board.index(r)][r.index(c)].visual = " ■ "
    Board = ToUpdate
    PrintBoard()
            
def StartLifeSimulation():
    while True:
        LifeSimulation()
        time.sleep(.5)

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
PrintBoard()
CreateLife()
StartLifeSimulation()