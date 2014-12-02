from matplotlib import pyplot as plt
from numpy import arange
from numpy import random

plt.plot([1,2,3,4,5], [2,4,6,8,10])
plt.show()

plt.plot([2,4,6,8,10])
plt.show()

plt.plot([2,4,6,8,10], "g-o")
plt.show()

x_points = arange(1,21)
baseline = arange(0,20)
plt.plot(x_points, baseline**2, "g-o", x_points, baseline, "r-^")
plt.show()

x_points = arange(1,21)
baseline = arange(0,20)
plt.plot(x_points, baseline**2, 'g-o', x_points, baseline, 'r-^')
plt.axis([0,21,0,400])
plt.show()

x_points = arange(1,21)
baseline = arange(0,20)
plt.plot(x_points, baseline**2, 'g-o', x_points, baseline, 'r-^')
plt.axis([0,21,0,400]) # shows the space left
plt.title("Amount of Python learned over time")
plt.xlabel("Days")
plt.ylabel("Standardized knowledge index score")
plt.legend(("Real Python", "Other course"), loc=2)
plt.show()

plt.bar(arange(0,10), arange(1,21,2))
plt.show()

plt.bar(arange(0,10), arange(1,21,2), width=.5)
plt.show()

plt.bar(arange(0,10)*2, arange(1,21,2))
plt.bar(arange(0,10)*2 +1 , arange(1,31,3), color='red')
plt.show()

plt.bar(arange(0,10)*3, arange(1,21,2))
plt.bar(arange(0,10)*3 +1, arange(1,31,3), color='red')
plt.xticks(arange(0,10)*3 +1, arange(1,11), fontsize=20, color='green')
plt.show()

plt.bar(arange(0,10)*3, arange(1,21,2))
plt.bar(arange(0,10)*3+1, arange(1,31,3), color='red')
plt.xticks(arange(0,10)*3+1, arange(1,11), fontsize=20)
plt.title("Coffee consumption due to sleep deprivation")
plt.xlabel("Group number")
plt.ylabel("Cups of coffee consumed")
plt.legend(("Control group", "Test group"), loc=2)
plt.show()

plt.hist(random.randn(10000), 20)
plt.show()

plt.hist(random.randn(10000), 20)
plt.annotate("expected mean", xy=(0,0), xytext=(0,300), ha="center", arrowprops=dict(facecolor='black'), fontsize=20)
plt.show()

plt.hist(random.rand(10000), 20)
plt.annotate(r"$\hat \mu = 0$", xy=(0,0), xytext=(0,300), ha="center", arrowprops=dict(facecolor='black'), fontsize=20)
plt.show() 
