# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:35:10 2021

@author: Mamma Georgina
"""

import pandas as pd
df_cab = pd.read_csv('Cab_Data.csv')
date_adjust = lambda x: pd.to_datetime('1900-01-01') + pd.to_timedelta(x,'D')
df_cab['Date of Travel'] = df_cab['Date of Travel'].apply(date_adjust)
df_cab.to_csv('Cab_Data_formatted.csv')
