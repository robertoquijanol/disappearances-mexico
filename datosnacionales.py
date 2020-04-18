# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:47:34 2020

@author: -
"""
import requests
import pandas as pd
import json
import numpy as np
#%%
var_info = pd.read_csv('desaparecidos.csv')
#%%
by_state = var_info['ENTIDAD'].value_counts().to_frame('count').sort_index()
#%%
by_state = by_state.drop(['NO ESPECIFICADO'])
#%%
by_state['percent'] = 100*by_state['count']/by_state['count'].sum()
#%
code = ['MX01', 'MX02', 'MX03', 'MX04', 'MX05', 'MX06', 'MX09', 'MX07', 'MX08', 'MX10', 'MX15','MX11','MX12', 'MX13','MX14', 'MX16','MX17','MX18','MX19','MX20','MX21','MX22','MX23','MX24','MX25','MX26','MX27','MX28','MX29','MX30','MX31','MX32']
 #%%      
num = np.arange(len(by_state))
#%%
by_state['state code'] = code
#%%
by_state['pop'] = [1312544,3315766,712029,899931,5217908,3556574,8918653,2954915,711235,1754754,16187608,5853677,3533251,2858359,7844830,4584471,1903811,1181050,5119504,3967889,6168863,2038372,1501562,2717820,2966321,2850330,2395272,3441698,1272847,8112505,2097175,1579209]
#%%
by_state['pop perc'] = 100*by_state['pop']/by_state['pop'].sum()
#%%
by_state['des100k'] = 100000*by_state['count']/by_state['pop']
#%%
by_state.to_csv('desap_por_estado.csv')
#%%
print(by_state)
