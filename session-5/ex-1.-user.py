def count(seq):
    """Counting the number of As in the string"""

    result = 0
    for letter in seq:
        if letter == 'A':
            result += 1

    return result


# Main program

s = input("Enter the sequence: ")
s = s.upper()

n = count(s)
print("The are", n, "in the sequence")

# Calculate the total length
letter = len(s)

print("This sequence is", n, "bases in length")
print("The percentages of As is", round(100.0 * n/letter, 1), "%")