import sys

from Simulator import simulate
from board.Board import Board

try:
    args = list(sys.argv[1:])
    board = Board(args[: - 2], int(args[ - 2]), int(args[ - 1]))
    simulate(board)
    print("this board can not be finished successfully")
except ValueError as result:
    print(result.args[0].replace("-0", "[↑]\n").replace("-1", "[↓]\n").replace("-2", "[→]\n").replace("-3", "[←]\n"))
