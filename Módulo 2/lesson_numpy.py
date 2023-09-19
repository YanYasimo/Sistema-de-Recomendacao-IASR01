#%%

import numpy as np 
data = np.array([1,2,3,4,5])
data

# %%
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
matriz

# %%
matriz = np.zeros((3,3))
matriz

# %%
%%time
identidade = np.eye(9)
identidade

# %%
%%time
total = 0
for i in range(100):
    for j in range(100):
        total += i*j
        if i > 0 and j > 0:
            total += (i/j)*5
total

# %%
