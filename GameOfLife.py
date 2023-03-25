import os
import time
import copy
class Cell:
    def __init__(self, alive, visual) -> None:
        self.alive = alive
        self.visual = visual

Board = []
def CreateBoard():
    RowRecursion = 0
    while RowRecursion < 10:
        Column = []
        ColumnRecursion = 0
        while ColumnRecursion < 10:
            NewCell = Cell(False, " - ")
            Column.append(NewCell)
            ColumnRecursion+=1
        Board.append(Column)
        RowRecursion+=1

def CreateLife():
    Continue = True
    while Continue:
        y = int(input("Row: "))
        x = int(input("Column: "))
        Board[y][x].alive = True
        Board[y][x].visual = " O "
        DoContinue = input("Choose another cell?    y/n \n: ")
        if(DoContinue == "y"):
            pass
        elif(DoContinue == "n"):
            Continue = False
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
            if r.index(c)+1 < 10 and r[r.index(c)+1].alive == True:
                LivingCells+=1

            UpBoard = Board.index(r)-1
            DownBoard = Board.index(r)+1
            AdjacentRows = [UpBoard, DownBoard]

            for row in AdjacentRows:
                if row == UpBoard and UpBoard < 0: continue
                elif DownBoard > 9: continue

                if Board[row][r.index(c)].alive == True:
                    LivingCells+=1
                if Board[row][r.index(c)-1].alive == True:
                    LivingCells+=1
                if r.index(c)+1<10 and Board[row][r.index(c)+1].alive == True:
                    LivingCells+=1

            if LivingCells < 2 or LivingCells > 3:
                ToUpdate[Board.index(r)][r.index(c)].alive = False
                ToUpdate[Board.index(r)][r.index(c)].visual = " - "
            elif LivingCells == 3:
                ToUpdate[Board.index(r)][r.index(c)].alive = True
                ToUpdate[Board.index(r)][r.index(c)].visual = " O "
    Board = ToUpdate
    PrintBoard()
            
def StartLifeSimulation():
    while True:
        LifeSimulation()
        time.sleep(1)

def PrintBoard():
    os.system("cls")
    for r in Board:
        print("\n", end="")
        for c in r:
            print(c.visual, end="")
    print("")

CreateBoard()
PrintBoard()
CreateLife()
StartLifeSimulation()