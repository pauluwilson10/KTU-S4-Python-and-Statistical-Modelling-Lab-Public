import numpy as np

class_interval=['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80']
frequency=[5,10,20,40,30,20,10,5]
middle_class=[]
for i in class_interval:
    x=i.split("-")
    middle=(int(x[0])+int(x[1]))/2
    middle_class.append(middle)
mean=np.average(middle_class,weights=frequency)
var=np.average((middle_class-mean)**2,weights=frequency)
sd=np.sqrt(var)
cv=(sd/mean)
print("Mean is: ",mean)
print("Variance: ",var)
print("Standard Deviation: ",sd)
print("Coefficient of variation: ",cv)
