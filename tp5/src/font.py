font3 = [
    [0x04, 0x04, 0x02, 0x00, 0x00, 0x00, 0x00],   # 0x60, `
    [0x00, 0x0e, 0x01, 0x0d, 0x13, 0x13, 0x0d],   # 0x61, a
    [0x10, 0x10, 0x10, 0x1c, 0x12, 0x12, 0x1c],   # 0x62, b
    [0x00, 0x00, 0x00, 0x0e, 0x10, 0x10, 0x0e],   # 0x63, c
    [0x01, 0x01, 0x01, 0x07, 0x09, 0x09, 0x07],   # 0x64, d
    [0x00, 0x00, 0x0e, 0x11, 0x1f, 0x10, 0x0f],   # 0x65, e
    [0x06, 0x09, 0x08, 0x1c, 0x08, 0x08, 0x08],   # 0x66, f
    [0x0e, 0x11, 0x13, 0x0d, 0x01, 0x01, 0x0e],   # 0x67, g
    [0x10, 0x10, 0x10, 0x16, 0x19, 0x11, 0x11],   # 0x68, h
    [0x00, 0x04, 0x00, 0x0c, 0x04, 0x04, 0x0e],   # 0x69, i
    [0x02, 0x00, 0x06, 0x02, 0x02, 0x12, 0x0c],   # 0x6a, j
    [0x10, 0x10, 0x12, 0x14, 0x18, 0x14, 0x12],   # 0x6b, k
    [0x0c, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04],   # 0x6c, l
    [0x00, 0x00, 0x0a, 0x15, 0x15, 0x11, 0x11],   # 0x6d, m
    [0x00, 0x00, 0x16, 0x19, 0x11, 0x11, 0x11],   # 0x6e, n
    [0x00, 0x00, 0x0e, 0x11, 0x11, 0x11, 0x0e],   # 0x6f, o
    [0x00, 0x1c, 0x12, 0x12, 0x1c, 0x10, 0x10],   # 0x70, p
    [0x00, 0x07, 0x09, 0x09, 0x07, 0x01, 0x01],   # 0x71, q
    [0x00, 0x00, 0x16, 0x19, 0x10, 0x10, 0x10],   # 0x72, r
    [0x00, 0x00, 0x0f, 0x10, 0x0e, 0x01, 0x1e],   # 0x73, s
    [0x08, 0x08, 0x1c, 0x08, 0x08, 0x09, 0x06],   # 0x74, t
    [0x00, 0x00, 0x11, 0x11, 0x11, 0x13, 0x0d],   # 0x75, u
    [0x00, 0x00, 0x11, 0x11, 0x11, 0x0a, 0x04],   # 0x76, v
    [0x00, 0x00, 0x11, 0x11, 0x15, 0x15, 0x0a],   # 0x77, w
    [0x00, 0x00, 0x11, 0x0a, 0x04, 0x0a, 0x11],   # 0x78, x
    [0x00, 0x11, 0x11, 0x0f, 0x01, 0x11, 0x0e],   # 0x79, y
    [0x00, 0x00, 0x1f, 0x02, 0x04, 0x08, 0x1f],   # 0x7a, z
    [0x06, 0x08, 0x08, 0x10, 0x08, 0x08, 0x06],   # 0x7b, {
    [0x04, 0x04, 0x04, 0x00, 0x04, 0x04, 0x04],   # 0x7c, |
    [0x0c, 0x02, 0x02, 0x01, 0x02, 0x02, 0x0c],   # 0x7d, }
    [0x08, 0x15, 0x02, 0x00, 0x00, 0x00, 0x00],   # 0x7e, ~
    [0x1f, 0x1f, 0x1f, 0x1f, 0x1f, 0x1f, 0x1f]    # 0x7f, DEL
]

def convert_to_35_array():
    arrays_35 = []
    for char in font3:
        char_array = []
        for value in char:
            # Convert the value to a 7-bit binary string, remove the '0b' prefix, and pad with zeros
            binary_string = bin(value)[2:].zfill(5)
            # Convert the binary string to a list of integers (0 or 1)
            row = [int(bit) for bit in binary_string]
            char_array.extend(replace_zeros_with_minus_one(row))
        arrays_35.append(char_array)
    return arrays_35


def replace_zeros_with_minus_one(array):
    numbers = []
    for i in array:
        if i == 0:
            numbers.append(-1)
        else:
            numbers.append(1)
    return numbers
