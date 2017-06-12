# Made: 17.05.2017 22:00
import numpy as np
np.set_printoptions(threshold='nan')


def addNewCombinationsIfNotAlreadyExist(combinations, testCombination):
	# checks if testCombination already excist in combination. If yes, returns the original combinations, if no, adds testCombinations to combinations and returns it
	
	for i in range(len(combinations)):
		if((testCombination == combinations[i]).all()):
			return combinations
	
	return np.concatenate((combinations, np.array([testCombination])),axis = 0)


def allCombinationOfMillerIndices(indices):
	
	# Extracting each digit
	n1 = indices[0]
	n2 = indices[1]
	n3 = indices[2]
	
	# combinations wil contain all current found combinations of Miller-Indices. In the end, our result wil be this array
	combinations = np.array([[n1,n2,n3]])
	
	# testCombination is to ment for testing if a new combinations already excist in combinations
	testCombination = np.array([n1,n2,n3])
	

	# We will start with the input 'indices' with three digits, a, b and c
	# We will check each six combinations of the input indices in the following order
	# a c b
	# c a b
	# c b a
	# b c a
	# b a c
	# a b c
	# Notice we change alternative the first and middle number, and the middle and last number. Thats why  we have switchEachTime
	switchEachTime = True
	tempTall = 0;
	
	for i in range(7):
		if(switchEachTime):
			switchEachTime = False
			tempTall = testCombination[0]
			testCombination[0] = testCombination[1]
			testCombination[1] = tempTall
			
			# if testCombinations already exist in combinations we don't want to add it. 
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, testCombination)
			
			
			# Check all negative combinations in the following order
			# -a b c
			# a -b c
			# a b -c
			# -a -b c
			# a -b -c
			# -a b -c
			# -a -b -c

			negativeVersion = testCombination

			negativeVersion[0] = -negativeVersion[0]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[0] = -negativeVersion[0]

			negativeVersion[1] = -negativeVersion[1]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[1] = -negativeVersion[1]
			
			negativeVersion[2] = -negativeVersion[2]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[2] = -negativeVersion[2]
			
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[1] = -negativeVersion[1]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[1] = -negativeVersion[1]
			
			negativeVersion[1] = -negativeVersion[1]
			negativeVersion[2] = -negativeVersion[2]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[1] = -negativeVersion[1]
			negativeVersion[2] = -negativeVersion[2]
			
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[2] = -negativeVersion[2]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[2] = -negativeVersion[2]	
			
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[1] = -negativeVersion[1]
			negativeVersion[2] = -negativeVersion[2]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[1] = -negativeVersion[1]
			negativeVersion[2] = -negativeVersion[2]
			
			
				
		else:
			switchEachTime = True
			tempTall = testCombination[2]
			testCombination[2] = testCombination[1]
			testCombination[1] = tempTall
			
			# if testCombinations already excist in combinations we don't want to add it. 
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, testCombination)
			
			# Check all negative combinations in the following order
			# -a b c
			# a -b c
			# a b -c
			# -a -b c
			# a -b -c
			# -a b -c
			# -a -b -c
			negativeVersion = testCombination

			negativeVersion[0] = -negativeVersion[0]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[1] = -negativeVersion[1]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[1] = -negativeVersion[1]
			
			negativeVersion[2] = -negativeVersion[2]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[2] = -negativeVersion[2]
			
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[1] = -negativeVersion[1]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[1] = -negativeVersion[1]
			
			negativeVersion[1] = -negativeVersion[1]
			negativeVersion[2] = -negativeVersion[2]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[1] = -negativeVersion[1]
			negativeVersion[2] = -negativeVersion[2]
			
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[2] = -negativeVersion[2]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[2] = -negativeVersion[2]	
			
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[1] = -negativeVersion[1]
			negativeVersion[2] = -negativeVersion[2]
			combinations = addNewCombinationsIfNotAlreadyExist(combinations, negativeVersion)
			negativeVersion[0] = -negativeVersion[0]
			negativeVersion[1] = -negativeVersion[1]
			negativeVersion[2] = -negativeVersion[2]

	return combinations
	
	
	
def make_2d_array_with_all_angle_combinations(x_combinations, y_combinations):
	length_x = len(x_combinations[:,0])
	length_y = len(y_combinations[:,0])
	twoD_array_with_all_angles = np.zeros((length_x, length_y))

	
	for i in range(length_x):
		for j in range(length_y):
			teller = x_combinations[i,0] * y_combinations[j,0] +  x_combinations[i,1] * y_combinations[j,1] +  x_combinations[i,2] * y_combinations[j,2] 
			nevner = np.sqrt(np.power(x_combinations[i,0],2) + np.power(x_combinations[i,1],2) + np.power(x_combinations[i,2],2)) * np.sqrt(np.power(y_combinations[j,0],2) + np.power(y_combinations[j,1],2) + np.power(y_combinations[j,2],2))
			
			twoD_array_with_all_angles[i,j] = np.arccos(teller/nevner)* 180 / np.pi
		
	
	#print "Printing two_d array: "
	#print twoD_array_with_all_angles
	
	return twoD_array_with_all_angles
	
def main():
	
	# Origin Indice which we want to find all combinations of Miller-indices
	indices_1 = [1,3,2]
	indices_2 = [2,2,3] 
	indices_3 = [2,0,2]
	
	
	# 1. Check 1 3 2 interplane
	indices_1_combinations = allCombinationOfMillerIndices(indices_1)
	twoD_array_with_all_angles = make_2d_array_with_all_angle_combinations(indices_1_combinations, indices_1_combinations)
	
	
	
	
	
#	x_combinations = allCombinationOfMillerIndices(indices_1)
#	y_combinations = allCombinationOfMillerIndices(indices_2)
#	print "====="
#	print x_combinations[2,0]
#	print "====="
	
	
	
	
	
	#twoD_array_with_all_angles = make_2d_array_with_all_angle_combinations(x_combinations, y_combinations)
	
	
	
	print "I'm in main loop. Printing combinations again:"
	#print x_combinations
	print "------------------------------------------------------------"
	#print y_combinations

	
if __name__ == "__main__":
	main()

