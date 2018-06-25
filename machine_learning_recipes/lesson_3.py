import numpy as np
import matplotlib.pyplot as plt

grehounds = 500
labs = 500

# create vectors (500 columns) of the average height +/- 4
average_greyhound_height = 28 + 4 * np.random.randn(grehounds)
average_labrador_height = 24 + 4 * np.random.randn(labs)

# create a histogram
plt.hist([average_greyhound_height, average_labrador_height],
         stacked=True, color=['r', 'b'])
plt.show()
