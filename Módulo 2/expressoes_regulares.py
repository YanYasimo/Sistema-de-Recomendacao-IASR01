
#Search

#%%
import re
entrada = r"Sistemas de Recomendação"
teste = re.search("(a|b)", entrada, re.IGNORECASE)
print(teste)

#%%
import re
entrada = r"cccbeeee"
teste = re.search("\A(a|b)", entrada)
print(teste)

# %%
import re
entrada = r"cccbeeee"
teste = re.search("\A(a|b|c*)", entrada)
print(teste)

# %%
import re
entrada = r"cccbeeee"
teste = re.search("\A(a|b|c*)\Z", entrada)
print(teste)

#Match & Fullmatch
# %%
import re
entrada = r"bcccbeeee"
teste = re.match("a|b", entrada)
print(teste)

# %%
import re
entrada = r"a"
teste = re.fullmatch("a|b", entrada)
print(teste)

#Compile
# %%
import re

teste = re.compile("ab*")
entrada = "abbbaba"
print(teste.search(entrada))
print(teste.match(entrada))
print(teste.fullmatch(entrada))

# %%
import re

teste = re.compile("\d*")

print(teste.fullmatch(r"63992152379"))

#Findall
# %%
import re
teste = re.compile("\A(ab*)\Z")
entrada = "abbb"
teste = teste.findall(entrada)
print(len(teste), teste)

# %%
import re
teste = re.compile("(ab*)")
entrada = "abbbaababbbbba"
teste = teste.findall(entrada)
print(len(teste), teste)

# %%
import re
teste = re.compile("\d{5}-?\d{3}")
print(teste.match("77015583"))

# %%
import re
teste = re.compile("\(\d{2}\)\d{4,5}\-\d{4}")
print(teste.match("(63)99215-2379"))

#Split
# %%
import re
teste = re.compile("\s")
entrada = "Estou estudando expressões regulares!"
teste = teste.split(entrada)
print(teste)

#Sub
# %%
import re
teste = re.compile("alunos")
entrada = "Bom dia, alunos! "
teste = teste.sub("estudantes", entrada)
print(teste)

# %%
#Escape & Purge
entrada = "Olá mundo.  (Python)"
entrada_escapada = re.escape(entrada)
print("Entrada original: ", entrada)
print("Entrada escapada: ", entrada_escapada)

re.purge()

# %%