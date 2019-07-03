import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[10,20,30,40])
print (s)

#A dict can be passed as input and if no index is specified, then the dictionary keys are taken in a sorted order to construct index.
#If index is passed, the values in data corresponding to the labels in the index will be pulled out.
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print (s)


s= pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print (s[0])


#Dataframe

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,30]}
df = pd.DataFrame(data)
print (df)
df.to_excel("output.xlsx")
