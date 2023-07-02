import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('Qt5Agg')
print(matplotlib.get_backend())


plt.plot([1,2,3,4])
plt.show()