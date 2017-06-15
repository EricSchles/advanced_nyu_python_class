def print_formatted(number):
    w = len(str(bin(number)[2:]))
    for i in range(1,number+1):
        d = str(i)
        o = str(int(oct(i)))
        h = str(hex(i)[2:]).upper()
        b = str(bin(i)[2:])
        print(d.rjust(w) + o.rjust(w+1) + h.rjust(w+1) + b.rjust(w+1))


