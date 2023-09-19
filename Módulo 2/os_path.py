# %%
from os.path import getatime, isdir, isfile, islink, os
import datetime

path = os.path.dirname(__file__)
acess_time = getatime(path)
d = datetime.datetime.fromtimestamp(acess_time)
print(d)

# %%
from os.path import join
current_dir = os.getcwd()
print(current_dir)
temp1 = join(current_dir, 'temp', 'temp1')
print(temp1)

# %%
from os.path import join, split
import os
current_dir = os.getcwd()

temp1 = join(current_dir, 'temp', 'temp1')
print(temp1)
dir, filename = split(temp1)
print(dir, filename)

# %%
from os.path import join, splitext
temp1 = join(current_dir, 'temp', 'temp2', 'file_ps.ps1')
filepath, ext = splitext(temp1)
print(filepath, ext)

#caso o path seja diretorio
temp1 = join(current_dir, 'temp', 'temp1', 'temp2')
filepath, ext = splitext(temp1)
print(filepath, ext)

# %%
with open("file_aula.txt", "r") as f:
    for line in f:
        print(line)
# %%
