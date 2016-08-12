from board.Cell import Cell


class Board:
    width, height, cells, availableCells = None, None, None, None

    def __init__(self, cells, width, height):
        self.cells = list(self.makeCells(cells))
        self.availableCells = [i for i in self.cells if i.remainingMove > 0]
        self.makeBoard(self.cells, width, height)
        self.width = width
        self.height = height

    def makeCells(self, cells):
        i = 0
        for cell in cells:
            splited = cell.split(":")
            yield Cell(splited[0], int(splited[1]), i)
            i += 1

    def makeBoard(self, cells, width, height):
        i = 0
        cellsCount = len(cells)
        for a in cells:
            topIndex, downIndex = i - width, i + width
            if topIndex >= 0:
                a.up = cells[topIndex]
            if downIndex < cellsCount:
                a.down = cells[downIndex]
            if i % width != 0:
                a.left = cells[i - 1]
            if (i + 1) % width != 0:
                a.right = cells[i + 1]
            i += 1

    def clone(self):
        return Board([i.color + ":" + str(i.remainingMove) for i in self.cells], self.width, self.height)
