import math
import statistics
import pandas
import numpy as np

np.random()
sample1 = [4.5, 5, 6]
sample2 = [10, 12, 14, 16, 18, 20]
  
# Computing sample standard deviation and mean for sample1
SD1 = statistics.stdev(sample1)
Mean1 = statistics.mean(sample1) 

# Computing sample standard deviation and mean for sample2
SD2 = statistics.stdev(sample2)   
  
# calculate length of 1st sample
n1 = len(sample1)
  
# calculate length of 2nd sample
n2 = len(sample2)
  
# calculate pooled standard deviation 
pooled_standard_deviation = math.sqrt(((n1 - 1)*SD1 * SD1 +(n2-1)*SD2 * SD2) / (n1 + n2-2))

# Calculate Coefficient of Variation for each sample
cv = (SD1/Mean1)*100

# Calculate the Exponentially weighted moving average (EWMA)
EWMA = pandas.DataFrame.ewm(sample1)
print("Pooled Standard Deviation = ",pooled_standard_deviation)
print("Mean1 = ",Mean1 , ",SD1 = ", SD1 , ",CV1 = ",cv, ",EWMA = ",EWMA)

