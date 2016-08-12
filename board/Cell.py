class Cell:
    remainingMove = 0
    previousColor, index, color, up, down, left, right = None, None, None, None, None, None, None

    def __init__(self, color, remainingMove, index):
        self.remainingMove = remainingMove
        self.color = color
        self.index = index
