# -*- Coding: UTF-8 -*-
#coding: utf-8
#!/usr/bin/env python3

import pandas as pd
from joblib import load, dump
from os import path

column_names = ['posto', 'latitude', 'longitude', 'recomendado']
def load_postos_combustiveis_data():
    df = pd.DataFrame(columns=column_names)
    rows = [{'posto': 'posto são paulo', 'latitude': 1, 'longitude': 1, 'recomendado': True}, {'posto': 'posto curitiba', 'latitude': 2, 'longitude': 2, 'recomendado': True}, {'posto': 'posto rio de janeiro', 'latitude': 3, 'longitude': 3, 'recomendado': True}, ]
    for row in rows:
        df.loc[len(df)] = row
    dump(df, 'postos_combustiveis.joblib')

def load_postos_combustiveis():
    return load('postos_combustiveis.joblib') if path.exists("postos_combustiveis.joblib") else pd.DataFrame(columns=column_names)
