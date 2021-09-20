import logging
from analysis import analysis as an
from analysis import analysis_utils as au
from analysis import plotting
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - [%(levelname)-8s] (%(threadName)-10s) %(message)s")
logger = logging.getLogger("Stat. QC")
PdfPages = PdfPages('output_results/statistics_results'+'.pdf')
output_directory = "output_results/"
input_directory = "input_data/"
plot = plotting.Plotting()
if __name__ == "__main__":
    #Load data samples
    data = au.read_csv_file(file = input_directory+"data_sample.csv")
    sample_data1 = data["A"].to_numpy()
    sample_data2 = data["B"].to_numpy()
    sample_data3 = data["C"].to_numpy()
    sample_data4 = data["D"].to_numpy() 
       
    mean1 = an.get_mean_from_array(array_data = sample_data1)
    mean2 = an.get_mean_from_array(array_data = sample_data2)
    mean3 = an.get_mean_from_array(array_data = sample_data3)
    mean4 = an.get_mean_from_array(array_data = sample_data4)
    
    std1 = an.get_std_from_array(array_data = sample_data1)
    std2 = an.get_std_from_array(array_data = sample_data2)
    std3 = an.get_std_from_array(array_data = sample_data3)
    std4 = an.get_std_from_array(array_data = sample_data4)
            
    cv1 = an.get_Coeff_variation(array_data = sample_data1)
    cv2 = an.get_Coeff_variation(array_data = sample_data2)
    cv3 = an.get_Coeff_variation(array_data = sample_data3)
    cv4 = an.get_Coeff_variation(array_data = sample_data4)
        
    pool_std_12 = an.get_pooled_std(array_data1 = sample_data1, array_data2 =sample_data2)
    pool_std_34 = an.get_pooled_std(array_data1 = sample_data3, array_data2 =sample_data4)
    
    #ewm1 = get_exp_weighted_moving_average(array_data = sample_data1)
    #ewm2 = get_exp_weighted_moving_average(array_data = sample_data2)
    
    output_data = ["###### Stat. Report ########"
                   'Sample data 1:',
                   "     "+"mean:"+str(mean1),
                   "     "+"std:"+str(std1),
                   "     "+"cv:"+str(cv1),
                   'Sample data 2:',
                   "     "+"mean:"+str(mean2),
                   "     "+"std:"+str(std2),
                   "     "+"cv:"+str(cv2),   
                   'Sample data 3:',
                   "     "+"mean:"+str(mean3),
                   "     "+"std:"+str(std3),
                   "     "+"cv:"+str(cv3),
                   'Sample data 4:',
                   "     "+"mean:"+str(mean4),
                   "     "+"std:"+str(std4),
                   "     "+"cv:"+str(cv4), 
                   
                   "#############################",           
                   "Pooled standard Deviation [1-2]= "+str(pool_std_12), 
                   "Pooled standard Deviation [3-4]= "+str(pool_std_34), 
                   "###### END OF Report ########"]
    au.save_to_txt(data=output_data, outname="data_sample_stat", directory=output_directory) 
      
    #plot output
    x = ["A", "B", "C", "D"]
    y = [mean1, mean2,mean3, mean4]
    yerr = [std1,std2,std3,std4]
    z= [cv1,cv2,cv3,cv4]
    plot.plot_lines(x=x, y=y,y_err = yerr, z=z, directory=output_directory, PdfPages=PdfPages)
    plot.close_pdf(PdfPages)
        