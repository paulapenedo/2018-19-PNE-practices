def count_bases(seq):
    """Counting the number of bases in the string"""

    result = {}
    for base in seq:
        if base in result:
            result[base] += 1
        else:
            result[base] = 1

    return result


# Main program

s = input("Enter the sequence: ")
s = s.upper()

d = count_bases(s)

# Calculate the total length
l = len(s)

print("This sequence is", l, "bases in length")
for base in d:
    counter = d[base]
    print('Base', base)
    print(' Counter: ', counter)
    print(' Percentage: ', counter * 100.0 / l)
