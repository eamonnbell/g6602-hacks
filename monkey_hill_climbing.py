import random

destination = "methinks it is like a weasel"

alphabet = "abcdefghijklmnopqrstuvwxyz "

def generate_letter():
    return alphabet[random.randint(0,len(alphabet)-1)]

def generate_string(n):
    out_string = ""
    for i in range(n):
        out_string += generate_letter()
    return out_string

def generate_subsequence(instring, k):
    subseq_set = set()
    for i in range(len(instring) - k + 1):
        subseq_set.add(instring[i:i+k])
    return subseq_set

def score(attempt, target, k):
    common = generate_subsequence(attempt, k) | generate_subsequence(target, k)
    return len(common)

i = 0

while True:
    generation = generate_string(27)
    if i == 1000:
        print(generation, destination)
        i = 0
    i += 1

