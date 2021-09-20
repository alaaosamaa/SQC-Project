import numpy as np
import pandas as pd
import tables as tb
import os
import csv

def save_to_txt(data=None, outname=None, directory=None):
    with open(directory+outname+".txt" , 'w') as out_file:
        for line in data:
            out_file.write(line)
            out_file.write('\n')
    return None

def save_to_csv(data=None, outname=None, directory=None):
    df = pd.DataFrame(data)
    if not os.path.exists(directory):
            os.mkdir(directory)
    filename = os.path.join(directory, outname)    
    df.to_csv(filename, index=True)

def read_csv_file(file=None):
    """ This function will read the data using pandas
    """
    data_file = pd.read_csv(file,encoding = 'utf-8').fillna(0)
    return data_file

