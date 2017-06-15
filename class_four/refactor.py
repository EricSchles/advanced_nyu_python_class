

def combine_number_reps(decimal_rep,
                        binary_width,
                        octal_rep, hex_rep,
                        binary_rep):
    """
    Description:

    Combine all four representations of the number.
    Representations we are combining:
    * decimal,
    * octal,
    * hexidecimal
    * binary

    Parameters
    ----------
    * decimal_rep - The decimal representation of the number
    e.g. 0.5
    * octal_rep - the octal representation of the number
    e.g. 10%8 = 12
    * hex_rep - the hexidecimal representation of the number
    e.g. 10A
    * binary_rep - the binary representation of the number
    e.g 0100
    * binary_width - the binary width of the number
    e.g. len(0100), so 4
    """
    result = decimal_rep.rjust(binary_width)
    result += octal_rep.rjust(binary_width+1)
    result += hex_rep.rjust(binary_width+1)
    result += binary_rep.rjust(binary_width+1)
    return result


def print_formatted(number):
    binary_width = len(str(bin(number)[2:]))
    for index in range(1, number+1):
        decimal_rep = str(index)
        octal_rep = str(int(oct(index)))
        hex_rep = str(hex(index)[2:].upper())
        binary_rep = str(bin(index)[2:])
        print(
            combine_number_reps(
                decimal_rep,
                binary_width,
                octal_rep,
                hex_rep,
                binary_rep
            )
        )
