import numpy as np
import math as mth
import pandas as pd
    
def get_mean_from_array(array_data = [0]):
    ''' Compute average of an array that represents a histogram 
        array_data : Array containing numbers whose mean is desired 
    '''
    mean_value = np.mean(array_data)
    return mean_value
    
   
def get_std_from_array(array_data = [0]):
    ''' Compute RMS of an array that represents a histogram along the specified axis.
        Parameters
        ----------
         array_data : Array containing numbers whose std is desired : 
    '''
    std_value = np.std(array_data)
    return std_value

def get_pooled_std(array_data1 = [0], array_data2 =[0]):
    ''' Compute the Pooled standard Deviation of two data sets
        
        Parameters
        ----------
         array_data1 : Array containing the first data sample
         array_data2 : Array containing the second data sample 
    '''
    
    sd1 = get_std_from_array(array_data1)# Computing sample standard deviation and mean for sample1
    sd2 = get_std_from_array(array_data2)# Computing sample standard deviation and mean for sample2
    n1, n2 = len(array_data1), len(array_data2)
    pooled_std = mth.sqrt(((n1 - 1)*sd1 * sd1 + (n2-1)*sd2 * sd2) / (n1 + n2-2))
    return pooled_std

def get_Coeff_variation(array_data = None):
    ''' Compute the Coefficient of Variation for a specific data set with mean and std
        
        Parameters
        ----------
         array_data : Array containing the  data sample
    '''
    mean_value = get_mean_from_array(array_data)
    sd_value = get_std_from_array(array_data)
    cv_value = (sd_value/mean_value)*100
    return cv_value

def get_exp_weighted_moving_average(array_data = [0]):
    ''' Compute the Calculate the Exponentially weighted moving average (EWMA)
        
        Parameters
        ----------
         array_data1 : Array containing the data sample
    '''
    # Calculate the Exponentially weighted moving average (EWMA)
    EWMA = pd.DataFrame.ewm(array_data)
    return EMWA
