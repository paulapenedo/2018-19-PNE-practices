import http.client
import json

from P7.Seq import Seq

PORT = 80
SERVER = 'rest.ensembl.org'

conn = http.client.HTTPConnection(SERVER, PORT)

conn.request("GET", "/homology/symbol/human/FRAT1?content-type=application/json")
r1 = conn.getresponse()
print("Response received!: {} {}\n".format(r1.status, r1.reason))

data1 = r1.read().decode("utf-8")
gene = json.loads(data1)
id = gene['data'][0]['id']
print(id)


conn.request("GET", '/sequence/id/' + id + '?content-type=application/json')
r1 = conn.getresponse()
data1 = r1.read().decode("utf-8")
gene = json.loads(data1)
print(gene)
bases = gene['seq']
print(bases)

seq1 = Seq(bases)

# Number of bases of DNA sequence
print("The total number of bases in the DNA gene is:", len(bases))

# Number of T nucleotides in the DNA sequence
print("The number of T nucleotides in the DNA sequence is:", seq1.count('T'))

# Ths most popular base in the gene
if seq1.count('A') > seq1.count('T') and seq1.count('A') > seq1.count('C') and seq1.count('A') > seq1.count('G'):
    print("The most popular base is A. It is repeated", seq1.count('A'), "times and the percentage is", seq1.perc('A'), "%")
elif seq1.count('T') > seq1.count('A') and seq1.count('T') > seq1.count('C') and seq1.count('T') > seq1.count('G'):
    print("The most popular base is T. It is repeated", seq1.count('T'), "times and the percentage is", seq1.perc('T'), "%")
elif seq1.count('C') > seq1.count('A') and seq1.count('C') > seq1.count('T') and seq1.count('C') > seq1.count('G'):
    print("The most popular base is C. It is repeated", seq1.count('C'), "times and the percentage is", seq1.perc('C'), "&")
elif seq1.count('G') > seq1.count('A') and seq1.count('G') > seq1.count('T') and seq1.count('G') > seq1.count('C'):
    print("The most popular base is G. It is repeated", seq1.count('G'), "times and the percentage is", seq1.perc('G'), "%")

# Percentage of nucleotides in the sequence
print("The percentage of A is", seq1.perc('A'), "%")
print("The percentage of T is", seq1.perc('T'), "%")
print("The percentage of C is", seq1.perc('C'), "%")
print("The percentage of G is", seq1.perc('G'), "%")

