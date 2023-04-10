#/usr/bin/python3

import os
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import time

cols = []
# Read features list
with open("data/kddcup.names", 'r') as file:
    next(file) # Start from the second row
    for row in file:
        cols.append(row.split()[0].rstrip(':'))

#print(cols)

attack_types = {}
with open("data/training_attack_types", 'r') as file:
    for row in file:
        (key, val) = row.split()
        attack_types[key] = val

print(attack_types)
