#!/usr/bin/env python
#coding: utf-8

import random

TARGET = "METHINKS IT IS LIKE A WEASEL"
MUTATION_CHANCE = 0.05

def copy_gene(gene):
    if random.random() < MUTATION_CHANCE:
        char = random.randint(65,91)
        if char == 91:
            return ' '

        return chr(char)

    return gene

def breed(individual):
    newborn = ''
    for char in individual:
        newborn += copy_gene(char)
    return newborn

def score(individual):
    score = 0
    for i in range(0,len(individual)):
        if individual[i] == TARGET[i]:
            score += 1
    return score

def generate_seed():
    seed = ""
    for i in range(0,len(TARGET)):
        char = random.randint(65,91)
        if char == 91:
            seed += ' '
        else:
            seed += chr(char)
    return seed


fittest = generate_seed()
generation = 0

print "Generation seed %s" % fittest

while fittest != TARGET:
    best_candidate = ""
    best_candidate_score = 0
    
    for i in range(0,100):
        newborn = breed(fittest)
        newborn_score = score(newborn)
        if newborn_score >= best_candidate_score:
            best_candidate = newborn
            best_candidate_score = newborn_score

    fittest = best_candidate
    print "Generation %d best candidate: %s (%d)" % (generation, best_candidate, best_candidate_score)
    generation += 1
