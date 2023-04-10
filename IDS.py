#/usr/bin/python3
"""
A simple experiment with Intrusion Detection System Based on Geeksforgeeks article:
https://www.geeksforgeeks.org/intrusion-detection-system-using-machine-learning-algorithms/
"""
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
    cols.append("target")

attack_types = {}
with open("data/training_attack_types", 'r') as file:
    attack_types['normal'] = 'normal'
    for row in file:
        (key, val) = row.rstrip("\n").split(' ')
        attack_types[key] = val

df = pd.read_csv("data/kddcup.data_10_percent.gz", names = cols)
# Add attack type column
df['Attack Type'] = df.target.apply(lambda r:attack_types[r[:-1]])
#print(df.shape)
#print(df.isnull().sum())

# Find categorical features
num_cols = df._get_numeric_data().columns

cate_cols = list(set(df.columns)-set(num_cols))
cate_cols.remove('target')
cate_cols.remove('Attack Type')

print(cate_cols)
