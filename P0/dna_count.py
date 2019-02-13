def count_A(seq_dna):
    result = 0
    for letter in seq_dna:
        if letter == "A":
            result += 1
        else:
            print("ERROR")

    return result

seq_dna = input("Introduce a valid sequence of DNA: ")
print("Total lenght of the sequence:", len(seq_dna))