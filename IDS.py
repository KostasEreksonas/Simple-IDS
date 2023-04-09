#/usr/bin/python3

import os
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import time

# Read features list
with open("data/kddcup.names", 'r') as file:
    print(file.read())
