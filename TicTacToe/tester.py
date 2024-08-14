from tictactoe import *
EMPTY = None


# print(player([["X","X","X"],["O","O","O"],["X", EMPTY, EMPTY]]))

# print(player([["X", EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY],
#             [EMPTY, "O", EMPTY]]))


# print(actions([["X", EMPTY, EMPTY],
#             [EMPTY, EMPTY, EMPTY],
#             [EMPTY, "O", EMPTY]]))
# print(actions([["X","X","X"],["O","O","O"],["X", EMPTY, EMPTY]]))

# print(result([["X", EMPTY, EMPTY],
#             [EMPTY, "X", EMPTY],
#             [EMPTY, "O", EMPTY]],(1,3)))


# print(winner([["X","O","X"],
            #   ["O","X","X"],
            #   ["O", "O", "O"]]))

print(terminal([["X","X","O"],
              ["O","O","O"],
              ["X", "X", "X"]]))
# print(terminal([["X","X","O"],
            #   ["O","O","X"],
            #   ["X", "X","X"]]))

# print(minimax([[None,"O","X"],
#               ["O","O","X"],
#               [None, "X", None]]))


