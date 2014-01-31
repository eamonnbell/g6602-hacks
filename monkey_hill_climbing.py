import random
import os
import time

destination = ("Methinks it is like a weasel\n"
               "Shall I compare thee\n"
               "Methinks it is like a weasel\n"
               "Shall I compare thee\n"
               "Are you so lovely\n"
               "Are you so lovely\n"
               )

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz \n"

def generate_letter():
    return alphabet[random.randint(0,len(alphabet)-1)]

def generate_string(n):
    out_string = ""
    for i in range(n):
        out_string += generate_letter()
    return out_string

def find_index_of_errors(attempt, target):
    position_list = []

    attempt_list = list(attempt)
    target_list = list(target)

    if len(target_list) != len(attempt_list):
        raise Exception

    for i in range(0, len(target_list)):
        if attempt_list[i] != target_list[i]:
            position_list.append(i)
    return position_list

def score_attempt(attempt, target):
    score = 0

    attempt_list = list(attempt)
    target_list = list(target)

    if len(target_list) != len(attempt_list):
        raise Exception

    for i in range(0, len(target_list)):
        if attempt_list[i] == target_list[i]:
            score +=1

    correct_ratio = score / len(target_list)

    return correct_ratio

def mutate(instring, position_list):
    instring_list = list(instring)
    char_to_mutate = position_list[random.randint(0,len(position_list) - 1)]
    gend_letter = generate_letter()
    instring_list[char_to_mutate] = gend_letter

    return "".join(instring_list)

i = 0
seed = generate_string(len(destination))
generation = seed
best_score = 0

while True:
    error_index = find_index_of_errors(generation, destination)
    mutation = mutate(generation, error_index)
    print(mutation)
    if score_attempt(mutation, destination) > best_score:
        generation = mutation
        best_score = score_attempt(generation, destination)

