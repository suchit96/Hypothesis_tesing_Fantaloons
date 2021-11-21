# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 15:30:22 2020

@author: Wellson
"""

import pandas as pd
import scipy
from scipy import stats
import statsmodels.api as sm

Fant=pd.read_csv("C:/Users/Wellson/Documents/R/360/Hypothesis testing/Fantaloons.csv")
Fant
Fant.dtypes

obj_Fant=Fant.select_dtypes(include=['object']).copy()

obj_Fant.head()
obj_Fant[obj_Fant.isnull().any(axis=1)]

obj_Fant['Weekdays'].value_counts()
scipy.stats.binom_test(x=113,n=287,p=0.5)

obj_Fant['Weekend'].value_counts()
scipy.stats.binom_test(x=167,n=233,p=0.5)
