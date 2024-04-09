import numpy as np
import pandas as pd
data = [
    ["Alabama", 4779736, 5.7],
    ["Alaska", 710231, 5.6],
    ["Arizona", 6392017, 4.7],
    ["Arkansas", 2915918, 5.6],
    ["California", 37253956, 4.4],
    ["Colorado", 5029196, 2.8],
    ["Connecticut", 3574097, 2.4],
    ["Delaware", 897934, 5.8],
]
murder=[]
df=pd.DataFrame(data,columns=["state","population","murder Rate"])

df["Murder"] = (df["population"]*df["murder Rate"])/100000
x=list(df["Murder"])
print(x)
mean=np.mean(x)
median=np.median(x)
var=np.var(x)
print("The mean is: ",mean)
print("The median is: ",median)
print("The variancee is: ",var)
"""


df["Murder"] = df["Population"]*df["Murder Rate"]
#print(df["Murder"])

x=list(df["Murder"])
for i in range(0,len(x)):
    x[i] = x[i]/100000
#print(x)

mean=np.mean(x)
med=np.median(x)
var=np.var(x)
print("Mean: ",mean)
print("Median: ",med)
print("Variance: ",var)
"""