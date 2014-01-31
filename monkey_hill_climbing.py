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

def score_attempt(attempt, target):
    score = 0

    attempt_list = [ch for ch in attempt]
    target_list = [ch for ch in target]

    if len(target_list) != len(attempt_list):
        raise Exception

    for i in range(0, len(target_list)):
        if attempt_list[i] == target_list[i]:
            score +=1

    correct_ratio = score / len(target_list)

    return correct_ratio

i = 0

best_score = 0
best_generation = ""

while True:
    generation = generate_string(28)
    score = score_attempt(generation, destination)

    if score > best_score:
        best_score = score
        best_generation = generation

    if i == 10000:
        print(best_generation, destination)
        print(best_score)
        i = 0
    i += 1

