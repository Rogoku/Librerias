#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def GenSubSet(df,*indices): 
    col_des = list(df.columns.values) 
    listafinal = []
    for indice in indices:
        for columna in df:
            if col_des.index(columna) == indice:
                listafinal.append(columna)

    subset = df[listafinal]
    return subset

