#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 14:39:14 2020

@author: oisinbrannock
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('eda_data.csv')

# Choose the relevant columns to analyze for model building 
df.columns

df_model = 