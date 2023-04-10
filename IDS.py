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

def get_columns(filename):
    """Get features list to columns array"""
    cols = []
    # Read features list
    with open(filename, 'r') as file:
        next(file) # Start from the second row
        for row in file:
            cols.append(row.split()[0].rstrip(':'))
        cols.append("target")
    print(cols)

def get_attacks(filename):
    """Create a dictionary of attack types"""
    attack_types = {}
    with open(filename, 'r') as file:
        attack_types['normal'] = 'normal'
        for row in file:
            (key, val) = row.rstrip("\n").split(' ')
            attack_types[key] = val
    print(attack_types)

get_columns("data/kddcup.names")
get_attacks("data/training_attack_types")
