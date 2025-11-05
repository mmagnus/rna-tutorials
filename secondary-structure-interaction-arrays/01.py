ss = '((....))' # -> (1, 5)
L = len(ss)
# create array of zeros with shape (1, len(ss), 1)
import numpy as np

matrix = np.zeros((L, L))
print(ss)

interaction_matrix = np.zeros((L, L), dtype=int)
print(interaction_matrix)

list_is = []
list_js = []
pairs = []
for i, s in enumerate(ss):
    if s == '(':
       list_is.append(i) 
    if s == ')':
       list_js.append(i) 
       pairs.append((list_is.pop(), i) )

print(list_is)
print(list_js)
print(pairs)

for i, j in pairs:
    interaction_matrix[i, j] = 1
    interaction_matrix[j, i] = 1

print(interaction_matrix)
