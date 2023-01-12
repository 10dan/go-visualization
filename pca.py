import numpy as np
with open("bin_to_coords.txt", "w") as out:
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

        # As the X dimension 14 01s, scale.
        x = (x / (2 ** len(x_bin))) * 100
        y = (y / (2 ** len(y_bin))) * 100
        print(x,y)
        out.write(str(binary) + ":" + "{:.2f}".format(x) + ":" + "{:.2f}".format(y) + "\n")