#!/usr/bin/env python
# program that plots XRD data from untreated and treated Si-fiber

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm 
from findIndices import *

# TODO: Maybe gather everything in a main function


def print_x_and_y_values(x_array, y_array, length):
	for i in range(length):
		print str(i+1) + ": x: \t "+ str(x_array[i]) + "\t y: \t" + str(y_array[i])
			

def find_phi(phi_angle,data_firstpeak_t):


        derivative_y_limit = 5
        # defining arrays where all found peaks wil be stored
        peak_y_values = []
        peak_x_values = []
        peak_i_values = []

        # Find all peaks
        length_of_data = len(phi_angle)
        number_of_steps_for_one_degree = length_of_data / float(360)
        #print "number_of_steps_for_one_degree: " + str(number_of_steps_for_one_degree)
        i = 0
        while i < length_of_data-1:
                # if we see a "jump" of more than "derivative_y_limit" units for one step, we assume one peak wil be within the next degree
                if(data_firstpeak_t[i+1] - data_firstpeak_t[i] > derivative_y_limit ):
                        # Found start of peak.
                        temp_y_max = float(0)
                        temp_i_max = 0
                        for i in range(i,i+int(number_of_steps_for_one_degree)):
                                if i == length_of_data:
                                        # Ignoring that we might get a peak at the end which we don't want
                                        break

                                # finding the max y-value within one degree and defining that one as the peak
                                if temp_y_max < data_firstpeak_t[i]:
                                        temp_i_max = i
                                        temp_y_max = data_firstpeak_t[i]
                                        temp_x_max = phi_angle[i]
                                
                                # print "----------------------------------------------------------------------"
                                # print str(i) +"x:\t" + str(phi_angle[i]) + ", y:\t" + str(data_firstpeak_t[i])
                        
                        
                        peak_y_values.append(temp_y_max)
                        peak_i_values.append(temp_i_max)
                        peak_x_values.append(temp_x_max)
                
                # printing every x- and y-value, including the index, so we can manualy overlook at the raw-data 
                #print str(i) +"x:\t" + str(phi_angle[i]) + ", y:\t" + str(data_firstpeak_t[i])
                                
                i += 1
                
        #print "-------------------------------------------------------------------------"
        #print "peak_y_values: " + str(peak_y_values)
        #print "peak_x_values: " + str(peak_x_values)
        #print "peak_i_values: " + str(peak_i_values)
        #print "number_of_steps_for_one_degree: " + str(number_of_steps_for_one_degree)
        #print "Length of data: " + str(length_of_data)
        #print "-------------------------------------------------------------------------"  

        return peak_x_values
        # finding differance between peaks in degrees and printing those
def find_difference_in_peaks(peak_x_values):
	
	
	peak_diff = np.zeros(len(peak_x_values)-1)
	for i in range(len(peak_x_values)-1):
		peak_diff[i] = peak_x_values[i+1]-peak_x_values[i]

	# This will include differance in angle between last peak and first peak. Remember adjust size of peak_diff on initiateing with zeros
	#peak_diff[len(peak_x_values)-1] = 360 - peak_x_values[len(peak_x_values)-1] + peak_x_values[0]
	return peak_diff


def find_unique_angles(angles_between_peaks):
	unique_angles = [angles_between_peaks[0]]
	isUnique = True
	
	rangeAroundDegree = 0.5
	
	for angle in angles_between_peaks:
		for i in range(len(unique_angles)):
			if(angle <  unique_angles[i] + rangeAroundDegree and angle >  unique_angles[i] - rangeAroundDegree):
				isUnique = False
				break
					
		if(isUnique):
			unique_angles.append(angle)
		isUnique = True

	return unique_angles
		
	
def main():

	print "hello MAN"	
	
        #first peak [2 2 0]
		
        data = np.loadtxt("../data/DE35214_UMG_treated_U03_firstpeak.xy")
		
		
        phi_angle = data[:,0]
        data_firstpeak_t = data[:,1]

        list_first_peaks_found_x = find_phi(phi_angle,data_firstpeak_t)
        list_peak_diff_first = find_difference_in_peaks(list_first_peaks_found_x)

        #second peak
        data = np.loadtxt("../data/DE35214_UMG_treated_U03_secondpeak.xy")
        phi_angle = data[:,0]
        data_secondpeak_t = data[:,1]

        list_second_peaks_found_x = find_phi(phi_angle,data_secondpeak_t)
        list_peak_diff_second = find_difference_in_peaks(list_second_peaks_found_x)

        #third peak
        data = np.loadtxt("../data/DE35214_UMG_treated_U03_thirdpeak.xy")
        phi_angle = data[:,0]
        data_thirdpeak_t = data[:,1]

        list_third_peaks_found_x = find_phi(phi_angle,data_thirdpeak_t)
        list_peak_diff_third = find_difference_in_peaks(list_third_peaks_found_x)

        #fourth peak
        data = np.loadtxt("../data/DE35214_UMG_treated_U04_02_fourthpeak.xy")
        phi_angle = data[:,0]
        data_fourthpeak_t = data[:,1]

        list_fourth_peaks_found_x = find_phi(phi_angle,data_fourthpeak_t)
        list_peak_diff_fourth = find_difference_in_peaks(list_fourth_peaks_found_x)

        #plotting phi-rotation of treated fiber
        color=iter(cm.rainbow(np.linspace(0,1,6)))

        fig2 = plt.figure()

        c1=next(color)   
        plt.plot(phi_angle, data_firstpeak_t, color=c1, label=r'$\langle 220 \rangle$ planes')
        c=next(color)   
        plt.plot(phi_angle, data_secondpeak_t, color=c, label=r'$\langle 400 \rangle$ planes')
        c=next(color)   
        plt.plot(phi_angle, data_thirdpeak_t, color=c, label=r'$\langle 440 \rangle$ planes')
        c=next(color)   
        #plt.plot(phi_angle, data_fourthpeak_t, color=c, label=r'$\langle 440 \rangle$ planes')

        #Plot peaks found
        for i in range(len(list_first_peaks_found_x)):
                plt.axvline(x=list_first_peaks_found_x[i],ymin=0.7, ymax=1, linewidth = 2, color = 'r') 

        for i in range(len(list_second_peaks_found_x)):
                plt.axvline(x=list_second_peaks_found_x[i],ymin=0.7, ymax=1, linewidth = 2, color = 'b') 

        for i in range(len(list_third_peaks_found_x)):
                plt.axvline(x=list_third_peaks_found_x[i],ymin=0.7, ymax=1, linewidth = 2, color = 'g') 

        #for i in range(len(list_fourth_peaks_found_x)):
                #plt.axvline(x=list_fourth_peaks_found_x[i],ymin=0.7, ymax=1, linewidth = 2, color = 'k') 


        plt.xlabel('$\phi$ rotation angle', fontsize=12)
        plt.ylabel('intensity', fontsize=12)
        plt.xlim(0,360)
        #plt.ylim(0,4500)
        plt.xticks(fontsize = 8)
        plt.yticks(fontsize = 8)
        plt.grid()
        plt.legend(loc='upper right', prop={'size':10})
        fig2.savefig("./U3_phi.pdf") 

        plt.show()




if __name__ == "__main__":
    main()
#This function is ran if program is read







	
			
			
			
	
