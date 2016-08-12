from concurrent.futures import thread


def move(newSource, newTarget, move):
    newTarget.color = newSource.color
    newTarget.remainingMove = newSource.remainingMove
    newSource.color = "0"
    newSource.remainingMove = 0


def paint(sourceCell, targetCell):
    if targetCell is not None and targetCell.color != "#" and targetCell.color != "0" and targetCell.color != sourceCell.color:
        if sourceCell.previousColor is None or sourceCell.previousColor == targetCell.color:
            targetCell.previousColor = targetCell.color
            targetCell.color = sourceCell.color
            paint(targetCell, targetCell.up)
            paint(targetCell, targetCell.down)
            paint(targetCell, targetCell.right)
            paint(targetCell, targetCell.left)
            targetCell.previousColor = None
            return True
    return False


def successfullyFinished(board):
    return len(set([i.color for i in board.cells if i.color != "0" and i.color != "#"])) == 1


def prepareForStep(board, sourceCell, targetCell, direction, previousPath):
    if targetCell is not None and targetCell.color != "#" and targetCell.color != sourceCell.color:
        currentPath = previousPath + str(sourceCell.index) + "-" + sourceCell.color + "-" + str(direction)
        newBoard = board.clone()
        newSource, newTarget = newBoard.cells[sourceCell.index], newBoard.cells[targetCell.index]
        newSource.remainingMove -= 1
        if newSource.remainingMove == 0:
            newBoard.availableCells.remove(newSource)
        if targetCell.color == "0":
            move(newSource, newTarget,direction)
        else:
            if not paint(newSource, newTarget):
                currentPath = previousPath

        for i in newBoard.availableCells:
            nextStep(newBoard, i, currentPath)
        if successfullyFinished(newBoard):
            raise ValueError(currentPath)
            # print(currentPath)
            # sys.exit()


def nextStep(board, i, currentPath):
    prepareForStep(board, i, i.up, 0, currentPath)
    prepareForStep(board, i, i.down, 1, currentPath)
    prepareForStep(board, i, i.right, 2, currentPath)
    prepareForStep(board, i, i.left, 3, currentPath)


def simulate(board):
    for i in board.availableCells:
        nextStep(board, i, "")
