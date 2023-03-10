import random
import matplotlib.pyplot as pl

sider = 6
ant = 1000
men = 0
men_m = 0
var = -1
var_m = 0
lis = []
lis_tal = []
pmf = []
for x in range(ant):
    lis.append(random.randint(1,sider))
    men = men + lis[x]/ant
    men_m = men_m + lis[x]
for i in lis:
    var = var + ((men-i)**2)/ant
    var_m = var_m + ((men-i)**2)
for i in range(1,sider+1):
    lis_tal.append([i,0])

print(lis_tal)
for i in lis:
    lis_tal[i-1][1] = lis_tal[i-1][1] + 1

for i in lis_tal:
    pmf.append([i[1]/ant,i[0]])

print(lis_tal)
#print(lis)
print("---------------")
print(men)
print(men_m/ant)
print("---------------")
print(var)
print(var_m/(ant-1))






pl.figure()
pl.plot(pmf, 'o', label="Outcomes")
pl.hist(lis_tal, bins=6)
pl.show()

