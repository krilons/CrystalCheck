#!/usr/bin/env python
# program that plots XRD data from untreated and treated Si-fiber

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm 
from findIndices import *
from find_phi import *

np.set_printoptions(suppress=True)


def getXValuesFromFile(filepath):
	data = np.loadtxt(filepath)
	x_values = data[:,0]
	return x_values

def getYValuesFromFile(filepath):
	data = np.loadtxt(filepath)
	y_values = data[:,1]
	return y_values


def returnAllFilePathsToSamples():
	filepaths = []
	filepaths.append(["../data/KTH_Si1_bc_05_firstpeak.xy", "../data/KTH_Si1_bc_05_secondpeak.xy","../data/KTH_Si1_bc_05_thirdpeak.xy", ""  ])
	filepaths.append(["../data_CrystalCheck/KTH_Si3_f1_02_firstpeak.xy", "../data_CrystalCheck/KTH_Si3_f1_02_secondpeak.xy","../data_CrystalCheck/KTH_Si3_f1_02_thirdpeak.xy", ""  ])
	filepaths.append(["../data/KTH_Si5_b_03_firstpeak.xy", "../data/KTH_Si5_b_03_secondpeak.xy","../data/KTH_Si5_b_03_thirdpeak.xy", ""  ])

	filepaths.append(["../data_CrystalCheck/DE35214_UMG_treated_U01_firstpeak_02.xy", "../data_CrystalCheck/DE35214_UMG_treated_U01_secondpeak_02.xy","../data_CrystalCheck/DE35214_UMG_treated_U01_thirdpeak_02.xy", ""  ])
	filepaths.append(["../data/DE35214_UMG_treated_U04_02_firstpeak.xy", "../data/DE35214_UMG_treated_U04_02_secondpeak.xy","../data/DE35214_UMG_treated_U04_02_thirdpeak.xy", "../data/DE35214_UMG_treated_U04_02_fourthpeak.xy"  ])
	filepaths.append(["../data/DE35214_UMG_treated_U03_firstpeak.xy", "../data/DE35214_UMG_treated_U03_secondpeak.xy","../data/DE35214_UMG_treated_U03_thirdpeak.xy", ""  ])
	filepaths.append(["../data_CrystalCheck/DE35214_UMG_treated_U05_02_noslit_firstpeak.xy", "../data_CrystalCheck/DE35214_UMG_treated_U05_02_noslit_thirdpeak.xy","../data_CrystalCheck/DE35214_UMG_treated_U05_02_noslit_fifthpeak.xy", ""  ])
	# filepaths.append(["../data_CrystalCheck/DE35214_UMG_treated_U06_firstpeak.xy", "../data_CrystalCheck/DE35214_UMG_treated_U06_fourthpeak.xy","../data_CrystalCheck/DE35214_UMG_treated_U06_fifthpeak.xy", ""  ])	
	filepaths.append(["../data_CrystalCheck/DE35214_UMG_treated_V01_firstpeak.xy", "../data_CrystalCheck/DE35214_UMG_treated_V01_secondpeak.xy","../data_CrystalCheck/DE35214_UMG_treated_V01_fourthpeak.xy", ""  ])

	filepaths.append(["../data_CrystalCheck/DA34316_O212_untreated_A04_firstpeak.xy", "../data_CrystalCheck/DA34316_O212_untreated_A04_secondpeak.xy","../data_CrystalCheck/DA34316_O212_untreated_A04_thirdpeak.xy", ""  ])
	filepaths.append(["../data_CrystalCheck/DA34316_O212_untreated_B01_firstpeak.xy", "../data_CrystalCheck/DA34316_O212_untreated_B01_secondpeak.xy","../data_CrystalCheck/DA34316_O212_untreated_B01_thirdpeak.xy", ""  ])
	filepaths.append(["../data_CrystalCheck/DA34316_O212_untreated_C05_firstpeak.xy", "../data_CrystalCheck/DA34316_O212_untreated_C05_secondpeak.xy","../data_CrystalCheck/DA34316_O212_untreated_C05_thirdpeak.xy", ""  ])
	filepaths.append(["../data_CrystalCheck/DA34416_E944_untreated_E01_firstpeak.xy", "../data_CrystalCheck/DA34416_E944_untreated_E01_secondpeak.xy","../data_CrystalCheck/DA34416_E944_untreated_E01_thirdpeak.xy", ""  ])
	filepaths.append(["../data_CrystalCheck/DA34316_O212_treated_A03_firstpeak.xy", "../data_CrystalCheck/DA34316_O212_treated_A03_secondpeak.xy","../data_CrystalCheck/DA34316_O212_treated_A03_thirdpeak.xy", ""  ])
	filepaths.append(["../data_CrystalCheck/DA34316_O212_treated_A06_firstpeak_02.xy", "../data_CrystalCheck/DA34316_O212_treated_A06_secondpeak_02.xy","../data_CrystalCheck/DA34316_O212_treated_A06_thirdpeak_02.xy", ""  ])
	filepaths.append(["../data_CrystalCheck/DA34316_O212_treated_C05_02_firstpeak.xy", "../data_CrystalCheck/DA34316_O212_treated_C05_02_secondpeak.xy","../data_CrystalCheck/DA34316_O212_treated_C05_02_thirdpeak.xy", ""  ])

	
	return filepaths

def returnAllSampleIndices(number_of_samples):
	planeFamilies_per_sample = 4
	
	# making 3D array
	sample_indices = np.zeros((number_of_samples, planeFamilies_per_sample, 3))
	sample_indices[0] = [[2,2,0], [4,2,2],[4,4,0],[0,0,0]] # 0'te object is a 2d-array,
	sample_indices[1] = [[2,2,0], [4,2,2], [3,3,1],[0,0,0]]
	sample_indices[2] = [[1,1,1], [3,1,1], [4,2,2],[0,0,0]]

	sample_indices[3] = [[2,2,0], [4,2,2], [5,3,1], [0,0,0]]
	sample_indices[4] = [[2,2,0], [3,1,1],[4,2,2],[4,4,0]] # 0'te object is a 2d-array,
	sample_indices[5] = [[2,2,0], [4,0,0],[4,4,0],[0,0,0]] # 0'te object is a 2d-array,
	sample_indices[6] = [[2,2,0], [3,3,1], [5,3,1], [0,0,0]]
	# sample_indices[7] = [[1,1,1], [4,2,2], [5,3,1], [0,0,0]]	
	sample_indices[7] = [[2,2,0], [3,3,1], [5,3,1], [0,0,0]]


	sample_indices[8] = [[2,2,0], [4,2,2], [4,4,0], [0,0,0]]
	sample_indices[9] = [[2,2,0], [4,2,2], [4,4,0], [0,0,0]]
	sample_indices[10] = [[2,2,0], [4,2,2], [4,4,0], [0,0,0]]		
	sample_indices[11] = [[2,2,0], [3,3,1], [5,1,1], [0,0,0]]	
	sample_indices[12] = [[3,1,1], [4,0,0], [3,3,1], [0,0,0]]
	sample_indices[13] = [[3,1,1], [3,3,1], [4,2,2], [0,0,0]]
	sample_indices[14] = [[1,1,1], [4,2,2], [5,3,1], [0,0,0]]

	return sample_indices

def returnAll2thetaAngles(number_of_samples): #all correction angles
	planeFamilies_per_sample = 3
	
	# making 3D array
	theta_angles = np.zeros((number_of_samples, planeFamilies_per_sample))
	theta_angles[0] = [21.29, 37.33, 43.37] # 0'te object is a 2d-array,
	theta_angles[1] = [21.29, 37.33, 33.09]
	theta_angles[2] = [12.99, 25.03, 37.33]

	theta_angles[3] = [21.29, 37.33, 45.47]
	theta_angles[4] = [21.29, 25.03, 37.33] # 0'te object is a 2d-array,
	theta_angles[5] = [21.29, 30.29, 43.37] # 0'te object is a 2d-array,
	theta_angles[6] = [21.29, 33.09, 45.47]
	# theta_angles[1] = [[1,1,1], [4,2,2], [5,3,1], [0,0,0]]	
	theta_angles[7] = [21.29, 33.09, 45.47]


	theta_angles[8] = [21.29, 37.33, 43.37]
	theta_angles[9] = [21.29, 37.33, 43.37]
	theta_angles[10] = [21.29, 37.33, 43.37]		
	theta_angles[11] = [21.29, 33.09, 39.69]	
	theta_angles[12] = [25.03, 30.29, 33.09]
	theta_angles[13] = [25.03, 33.09, 37.33]
	theta_angles[14] = [12.99, 37.33, 45.47]

	return theta_angles

def main():
	
	
	# When adding new sample(3/4 filer altsaa), do this:
		# 1. append new filepaths. Copy line 28 and change filenames, if no forth file, use empty string=> ,""
		# 2. add Miller Indices by copying line 39. If no forth indices, just place random indices there, they will not get testet anyways
		# 3. Inkrement "number_of_samples" to correct number
	

	print "Starting our big main-file"
	number_of_samples = 15
	planeFamilies_per_sample = 4
	angle_deviation_accepted = 0.5
	
	filepaths = returnAllFilePathsToSamples()
	sample_indices = returnAllSampleIndices(number_of_samples)
	theta_angles = returnAll2thetaAngles(number_of_samples)
	print "Filepaths:"
	print filepaths
	print "Sample_indices:"
	print sample_indices
	
	
	all_found_angles = np.ones((number_of_samples, planeFamilies_per_sample))
	all_first_peaks = np.zeros((number_of_samples, planeFamilies_per_sample))
	closest_angle_during_crossplane = np.zeros((number_of_samples, 3))

	
	for i in range(number_of_samples):
		print "===================================================="
		print "\t\t Checking new sample"
		print "===================================================="

				
		for j in range(planeFamilies_per_sample):

			if(filepaths[i][j]):
				print "===================================================="
				print "\t\t Testing new family[a,b,c]"
				print "===================================================="
				print str(filepaths[i][j])
				print "i: " + str(i)
				print "j: " + str(j)
				
				x_values = getXValuesFromFile(filepaths[i][j])
				y_values = getYValuesFromFile(filepaths[i][j])
				
				peaks = find_phi(x_values, y_values)
				
				print "peaks: "
				print peaks
				
				# Store first Peak for use when testing for crossplain
				all_first_peaks[i][j] = peaks[0]
				

				angles_between_peaks = find_difference_in_peaks(peaks)
				#print "Angles Between Peaks: "
				#print angles_between_peaks
				unique_angles = find_unique_angles(angles_between_peaks)
				
				print "Unique angles"
				print unique_angles
				
				# Find all combinations of Miller Indices for the first family
				millerCombinations = allCombinationOfMillerIndices(sample_indices[i][j])
				
				# Make 2D array with all angles between all combinations of Miller Indices
				twoD_array_with_all_angles = make_2d_array_with_all_angle_combinations(millerCombinations, millerCombinations)
				
				twoD_size_rows = len(twoD_array_with_all_angles[:,0])
				twoD_size_columns = len(twoD_array_with_all_angles[0,:])
				print "2D array interplane from " + str(sample_indices[i][j])
				# print twoD_array_with_all_angles
				
				
				# Find if our angles from the inter-family matches with any angles from our 2D array
				found_angle_array = np.zeros(len(unique_angles))
				o = 0
				teller = 0
				for unique_angle in unique_angles:
					for row in range(twoD_size_rows):
						for column in range(twoD_size_columns):
						
							if(twoD_array_with_all_angles[row][column]  > unique_angle - angle_deviation_accepted and twoD_array_with_all_angles[row][column]  < unique_angle + angle_deviation_accepted):
								found_angle_array[teller] = 1
								print "We found match between unique angle and angle in 2d array. Unique angle was: " + str(twoD_array_with_all_angles[row][column]) + "\tsample_indices[i][j]: " + str(sample_indices[i][j])
								print "Row: " + str(row) + " Column: " + str(column)
								
								
								print "Unique angle" + str(unique_angle)
								o = o + 1
								print "I: " + str(o)
			
								break
						if(found_angle_array[teller]):
							break
					teller = teller+1
				print "Unique angles and if they were found: " + str(unique_angles) + " found: " + str(found_angle_array)	
				all_found_angles[i][j] = 1
				for k in range(len(found_angle_array)):
					if(not found_angle_array[k]):
						all_found_angles[i][j] = 0
						break
					
					
		# print "---------------------------------------------"	
		# print "All found angles (1 for found in this family): "
		# print all_found_angles
		# print "All found first peaks (peak from each family): " 
		# print all_first_peaks
		#Checking crossplain
		
		
	print "============================================================="
	print "\t\t\t\t Checking Crossplain"
	print "============================================================="
	hei  = True 
	for i in range(number_of_samples):
		print "----------------------------------------------"
		print "\t\tChecking new sample" + str(filepaths[i][0])
		print "----------------------------------------------"
		if (hei):
		#if(all_found_angles[i][0] and all_found_angles[i][1] and all_found_angles[i][2] and all_found_angles[i][3]):
			for k in range(3):
				print "----------------------------------------------"
				print "\t\tChecking new crossplain"
				print "----------------------------------------------"
				#[2,2,0], [3,1,1],[5,3,1],[4,4,0]
				# 1. Check 1. and 2. Miller Indices 
				# 2. Check 2. and 3.
				# 3. Check 3. and 1.
				miller_combinations_1 = allCombinationOfMillerIndices(sample_indices[i][k])

				if(k == 2):
					miller_combinations_2 = allCombinationOfMillerIndices(sample_indices[i][0])
				else:
					miller_combinations_2 = allCombinationOfMillerIndices(sample_indices[i][k+1])


					# Make 2D array with all angles between [2,2,0] and [3,1,1], (first and second family)
				twoD_array_with_all_angles = make_2d_array_with_all_angle_combinations(miller_combinations_1, miller_combinations_2)

				twoD_size_rows = len(twoD_array_with_all_angles[:,0])
				twoD_size_columns = len(twoD_array_with_all_angles[0,:])
				if(k == 2):
					difference_between_first_peaks = np.absolute(all_first_peaks[i][k] - all_first_peaks[i][0])+(np.absolute(theta_angles[i][k]-theta_angles[i][0])/2) #is here adding a correction angle
					print "added angle is: " + str((np.absolute(theta_angles[i][k]-theta_angles[i][0])/2))
				else:
					difference_between_first_peaks = np.absolute(all_first_peaks[i][k] - all_first_peaks[i][k+1])+(np.absolute(theta_angles[i][k]-theta_angles[i][k+1])/2) #is here adding a correction angle
					print "added angle is: " + str((np.absolute(theta_angles[i][k]-theta_angles[i][k+1])/2))
				found_angle_array = np.zeros(len(unique_angles))
				o = 0
				#print "Miller_combinations_1: " + str(miller_combinations_1)
				#print "Miller_combinations_2: " + str(miller_combinations_2)
				if(k == 2):
					print "Difference between " + str(all_first_peaks[i][k]) + " and " + str(all_first_peaks[i][0]) + " is: " + str(difference_between_first_peaks)
					print "Looking at all angles between combinations of " + str(sample_indices[i][k]) + " and " + str(sample_indices[i][0])
				else:
					print "Difference between " + str(all_first_peaks[i][k]) + " and " + str(all_first_peaks[i][k+1]) + " is: " + str(difference_between_first_peaks)
					print "Looking at all angles between combinations of " + str(sample_indices[i][k]) + " and " + str(sample_indices[i][k+1])


				#print twoD_array_with_all_angles

				closest_angle = 1000
				found_angle_in_crossplane = False	

				for row in range(twoD_size_rows):
					for column in range(twoD_size_columns):
						newTall = min(closest_angle, np.absolute(twoD_array_with_all_angles[row][column] - difference_between_first_peaks))
						#newTall was before closest_angle

					if(newTall < closest_angle):
						closest_angle = newTall

						
						if(twoD_array_with_all_angles[row][column]  > difference_between_first_peaks - angle_deviation_accepted and twoD_array_with_all_angles[row][column]  < difference_between_first_peaks + angle_deviation_accepted):
							found_angle_in_crossplane = True
							print "\n\nWe found match between 'difference in first peaks' and angle in 2d array. 'Difference in first peaks was: " + str(difference_between_first_peaks) + "\tIndices: " + str(miller_combinations_1[row]) + " and " + str(miller_combinations_2[column]) 
							print "Row: " + str(row) + " Column: " + str(column)
							print "Angle match in 2D array: " + str(twoD_array_with_all_angles[row][column])
							o = o + 1
							print "O: " + str(o)

							break
					if(found_angle_in_crossplane):
						break
				
				
				closest_angle_during_crossplane[i][k] = closest_angle	

				if(not found_angle_in_crossplane):
					print "\n\n"
					print "UPS. Didn't find any match for angle: " + str(difference_between_first_peaks)
					print "\n"

			
			
		else:
			print "Interplane match FAILED. Therefore no crossplane check. This was for sample : " + str(i+1)
			print "all_found_angles[i][0], all_found_angles[i][1], all_found_angles[i][2], all_found_angles[i][3]: "
			print str(all_found_angles[i][0]) + "\t" + str(all_found_angles[i][1])  + "\t" + str(all_found_angles[i][2])  + "\t" + str(all_found_angles[i][3])


	print "SUMMARY"
	print "---------------------------------------------"	
	print "Filepaths:"
	print filepaths
	print "Sample_indices:"
	print sample_indices
	print "All found angles (1 for found in this family): "
	print all_found_angles
	print "All found first peaks (peak from each family): " 
	print all_first_peaks
	#Checking crossplain	
	print "closest_angle_during_crossplane (1-2) (2-3) (3-1)"
	print closest_angle_during_crossplane

	
	#write to file

	np.savetxt("closest_angle_during_crossplane.txt", closest_angle_during_crossplane,  fmt='%.18e', delimiter=' ', newline='\n')

	# f.write( "Filepaths:")
	# f.write( filepaths)
	# f.write( "Sample_indices:")
	# f.write( sample_indices)
	# f.write( "All found angles (1 for found in this family): ")
	# f.write( all_found_angles)
	# f.write( "All found first peaks (peak from each family): " )
	# f.write( all_first_peaks)
	# #Checking crossplain	
	# f.write( "closest_angle_during_crossplane (1-2) (2-3) (3-1)")
	# f.write( closest_angle_during_crossplane)

if __name__ == "__main__":
    main()
#This function is ran if program is read







	
			
			
			
	
