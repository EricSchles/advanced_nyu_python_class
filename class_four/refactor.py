def print_formatted(number):
    binary_width = len(str(bin(number)[2:]))
    for index in range(1, number+1):
        decimal_rep = str(index)
        octal_rep = str(int(oct(index)))
        hex_rep = str(hex(index)[2:].upper())
        binary_rep = str(bin(index)[2:])
        print(
            decimal_rep.rjust(binary_width)
            + octal_rep.rjust(binary_width+1)
            + hex_rep.rjust(binary_width+1)
            + binary_rep.rjust(binary_width+1)
        )
