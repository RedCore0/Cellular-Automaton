"""
Conway's Game of life

Created by John Horton Conway in 1970.
Conway made the Game of Life because he wanted to know if he could make
an imaginary robot out of cells that would be able to get bigger.

Rules:
    1: Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    2: Any live cell with two or three live neighbours lives on to the next generation.
    3:  Any live cell with more than three live neighbours dies, as if by overpopulation.
    4: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

"""

import copy
  
def LifeSimulation(BoardSize, Board):
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
    return Board