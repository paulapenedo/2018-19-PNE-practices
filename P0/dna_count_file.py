seq_dna = input("Introduce a sequence of DNA: ")

def count(seq_dna):
    count_A = 0
    count_G = 0
    count_C = 0
    count_T = 0

    for letter in seq_dna:
        if letter != 'A' and letter != 'C' and letter != 'G' and letter != 'T':
            print("Error, the letters must be A, C, G, T")
        else:
            print("Total lenght: ", len(seq_dna))
            if letter == "A":
                count_A += 1
            elif letter == "G":
                count_G += 1
            elif letter == "C":
                count_C += 1
            elif letter == "T":
                count_T += 1

            print("A:", count_A)
            print("G:", count_G)
            print("C:", count_C)
            print("T:", count_T)

            break

count(seq_dna)