# %%
import os
print (os.listdir())
print(os.path.dirname(__file__))

# %%
import os

#verifica se arquivo existe, se é possível escrever, ler e executar. Consecutivamente
os.access("expressoes_regulares.py", os.F_OK)
os.access("expressoes_regulares.py", os.W_OK)
os.access("expressoes_regulares.py", os.R_OK)
os.access("expressoes_regulares.py", os.X_OK)

# %%
import os 

for path in os.walk("temp"):
    print(path)

# %%
import os
def onError(error):
    print("Some error on: ", error)

for path in os.walk("temp", True, onerror=onError):
    print(path)
    
# %%
