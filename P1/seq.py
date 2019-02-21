class Seq:

    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        return len(self.strbases)

    def complement(self):

        compl = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        result = ''
        for letter in self.strbases:
            result += compl[letter]

        return Seq(result)

    def reverse(self):
        l = list(self.strbases)
        l.reverse()
        r = ''.join(l)
        return Seq(r)

    def count(self, base):
        count = 0
        for letter in self.strbases:
            if letter == base:
                count += 1
        return count

    def perc(self, base):
        l = self.len()
        c = self.count(base)
        return c * 100.0 / l

