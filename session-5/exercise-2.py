def count_bases(seq):
    """Counting the number of bases in the string"""

    result = {}
    for base in seq:
        if base in result:
            result[base] += 1
        else:
            result[base] = 1

    return result

#Request for the two sequences

s1 = input("Enter the sequence 1: ")
s2 = input("Enter the sequence 2: ")
s1 = s1.upper()
s2 = s2.upper()

d1 = count_bases(s1)
d2 = count_bases(s2)

l1 = len(s1)
l2 = len(s2)

#Sequence 1
print("Sequence 1 is", l1, "bases in length")
for base in d1:
    counter1 = d1[base]
    print("Base", base)
    print(" Counter:", counter1)
    print(" Percentage:", counter1 * 100.0 / l1)


#Sequence 1
print("Sequence 2 is", l2, "bases in lenght")
for base in d2:
    counter2 = d2[base]
    print("Base", base)
    print(" Counter:", counter2)
    print(" Percentage:", counter2 * 100.0 / l2)







