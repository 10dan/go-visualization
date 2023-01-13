import pickle
import helpers

"""
Every GO board state will be represented in 3 states:
- A 3x3 integer array
    [ [0, 0, 1],
      [0, 2, 0],
      [1, 2, 0] ]
- A 18 bit binary string
    |        x - coord        |        y - coord         |
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
- A coordinate on a 2D plane
    Take the binary from above, and then scale between -100:100
    (-40, 50)
"""

with open("data.pickle", "rb") as inp:
    data = pickle.load(inp)

def create_blank_board():
    return [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
        ]

def create_board():
    return [
        [1, 0, 0],
        [0, 1, 0],
        [2, 0, 2]
        ]
                
print(helpers.convert_board_to_binary(create_board()))
