from P1.seq import Seq

s1 = input('Introduce the first sequence: ')
s1 = s1.upper()
s2 = input('Introduce teh second sequence: ')
s2 = s2.upper()

seq1 = Seq(s1)
seq2 = Seq(s2)
seq3 = seq1.complement()
seq4 = seq3.reverse()

seqs = [seq1, seq2, seq3, seq4]

bases = ['A', 'T', 'C', 'G']

i = 0
for seq in seqs:
    i += 1
    print('Sequence', i, ':')
    print(' Length:', seq.len())
    count = dict.fromkeys(bases)
    perc = dict.fromkeys(bases)
    for base in bases:
        count[base] = seq.count(base)
        perc[base] = round(seq.perc(base), 1)

    count_str = ''.join('{}:{}, '.format(k, v) for k, v in count.items())
    perc_str = ''.join('{}:{}%, '.format(k, v) for k, v in perc.items())
    print(' Bases count:', count_str)
    print(' bases percentage:', perc_str, '\n')

