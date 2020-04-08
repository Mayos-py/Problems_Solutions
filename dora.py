# Dora is very much interested in gardening and she decides to plant more trees in her garden. She plant trees in the order of rows and columns. She numbered the trees in column wise order. She planted the mango tree in the second column from both first and last. But later when the trees grew up, she forgot where she planted mango trees. So help her out whether the given tree number is a number of mango trees or not, Display whether "It is a Mango tree".


import numpy as np
row=int(input("Enter Row: "))
col=int(input("Enter Col: "))
arr1=[]
arr2=[]
m = np.arange(1, row*col+1, 1)
m = m.reshape(col,row)
matrix=m.tolist()
print(matrix)

arr1=matrix[1]
arr2=matrix[col-2]
tree=int(input("Enter tree no. : "))

for _ in arr2:
    arr1.append(_)

[print("It's a Mango Tree !") for i in arr1 if i is tree]
# for i in arr1:
#     if i==tree:
#         print("It's Mango Tree !")



