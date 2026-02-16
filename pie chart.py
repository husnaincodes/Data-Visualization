import numpy as np
import matplotlib.pyplot as plt

y = np.array([35, 25, 15, 100])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.legend()
plt.show()