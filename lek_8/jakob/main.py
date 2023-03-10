import random
import matplotlib.pyplot as plt

input =[]
fig = plt.figure(figsize = (10, 5))
#Random tempareture genrator
for x in range(100):
    input.append(random.normalvariate(0,10))








plt.plot(input)

plt.show()
