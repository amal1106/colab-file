# -*- coding: utf-8 -*-
"""First_Colab_File.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lnVv3yiM0b_6DS1g5IvzIc3s1-nf0jtv
"""



"""# Matrix (Array)"""

matrix=[[1,2,3],       #size=3x3      #Inialisation d'une variable de type "array"
       [4,5,6],          #matrix or array is defined by [[]]
       [7,8,9] ]

print("voila la matrice :", matrix)

import numpy as np     #numpy bib des stats et matrices
matrix=np.array([[1,2,3],
                [4,5,6],
                [7,8,9] ])
mean_value= np.mean(matrix)
print("la moyenne est :", mean_value)

median_value= np.median(matrix)
median_value

"""list"""

liste=[-1,5,3,-8,0]
liste

max(liste)

min(liste)

sum(liste)

#index=indice  #l'indexation debute de 0
liste[0]