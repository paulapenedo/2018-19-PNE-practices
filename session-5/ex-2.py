class Seq:
    def __init__(self, strbases):
        print("New sequence created!")

        self.strbases = strbases

    def len(self):
        return len(self.strbases)

class Gene(Seq):
    pass

s1 = Gene("AGTACACTGGT")
s2 = Seq("CGTAAC")

str1 = s1.strbases
str2 = s2.strbases

l1 = s1.len()
l2 = s2.len()

print("Sequence 1: {}".format(str1))
print(" Lenght: {}".format(l1))
print("Sequence 2: {}".format(str2))
print(" Lenght: {}".format(l2))
print("Testing the sequence objects")



