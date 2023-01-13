import pickle

def create_pickle_jar(): 
    data = {}
    for i in range(2**18):
        binary = bin(i)[2:].zfill(18)

        x_bin_arr = binary[:9]
        y_bin_arr = binary[9:]

        # Convert from binary arr to string.
        x_bin = "".join(str(i) for i in x_bin_arr)
        y_bin = "".join(str(i) for i in y_bin_arr)

        # Convert from binary string to decimal
        x = int(x_bin, 2)
        y = int(y_bin, 2)

        x = ((x / (2 ** len(x_bin))) * 200) - 100
        y = ((y / (2 ** len(y_bin))) * 200) - 100
        data[binary] = (x, y)
        print(x,y)

    with open("data.pickle", "wb") as out:
        pickle.dump(data, out)

def convert_board_to_binary(board):
    black_arr = []
    white_arr = []
    for row in board:
        for col in row:
            if col == 0:
                black_arr.append(0)
                white_arr.append(0)
            if col == 1:
                black_arr.append(1)
                white_arr.append(0)
            if col == 2:
                black_arr.append(0)
                white_arr.append(1)
    return black_arr + white_arr