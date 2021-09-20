from __future__ import division
import numpy as np
from kafe.function_library import quadratic_3par
from numpy import loadtxt, arange
import csv
from scipy.optimize import curve_fit
import tables as tb
from mpl_toolkits.mplot3d import Axes3D
import itertools
from mpl_toolkits.mplot3d import Axes3D  # @UnusedImport
from math import pi, cos, sin
from scipy.linalg import norm
import os
import seaborn as sns
sns.set(style="white", color_codes=True)

from matplotlib.pyplot import *
import pylab as P
import matplotlib as mpl
import matplotlib.ticker as ticker
import matplotlib.transforms as mtransforms
import matplotlib.patches as patches
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import gridspec
from matplotlib.colors import LogNorm
from matplotlib.patches import Circle
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredDrawingArea
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
from matplotlib.ticker import NullFormatter
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
from analysis import analysis
from analysis import logger
import matplotlib.image as image
from scipy import interpolate
colors = ['black', 'red', '#006381', "blue", '#33D1FF', '#F5A9BC', 'grey', '#7e0044', 'orange', "maroon", 'green', "magenta", '#33D1FF', '#7e0044', "yellow"]
#an = analysis.Analysis()

class Plotting(object): 

    def __init__(self):
        self.log = logger.Logger().setup_main_logger(name = 'Plotting')
        self.log.info('Plotting initialized')


    def plot_lines(self, x=None, y=None, y_err = None,  z=None, directory=None, PdfPages=PdfPages):
        '''
        PLot a relation between two variables 
        '''
        fig = plt.figure()
        ax = fig.add_subplot(111)
        cmap = plt.cm.get_cmap('viridis', 15)
        sc = ax.scatter(x, y, c=z, cmap=cmap, s=10)
        #ax.errorbar([1,2,3,4], y, xerr=0.0, yerr=y_err, fmt='o', markersize=3, ecolor='black')
        plt.plot(x,y,"-")
        cbar = fig.colorbar(sc, ax=ax, orientation='vertical')
        cbar.set_label("Coefficient of Variation", labelpad=1, fontsize=10)
        #plt.axvline(x=2.6, linewidth=0.8, color="red", linestyle='dashed')
        ax.set_ylabel("Data mean", fontsize=10)
        ax.set_title("Data Stat", fontsize=8)
        ax.set_xlabel("Data Name", fontsize=10) 
        ax.grid(True)
        fig.savefig(directory + "data_sample_stat.png", bbox_inches='tight')
        plt.tight_layout()
        PdfPages.savefig()
           
    def close_pdf(self, PdfPages=False):
        PdfPages.close()
