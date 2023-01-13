import main
def test_bin_arr_correct():
    board = [
        [1, 0, 0],
        [0, 1, 0],
        [2, 0, 2]
        ]
    expected = [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1]
    actual = main.convert_board_to_binary(board)
    if expected == actual:
        print("😄 test_bin_arr_correct passed ")
        return True
    else: 
        print("⛔ test_bin_arr_correct failed ")
        return False

test_bin_arr_correct()