"""
Challenge #2: Lexicographic Sorting

Summary: Write a function to sort an array of strings based on an arbitrary 
lexicographic ordering. The function will take two parameters: an array of 
strings to sort and a string specifying the lexicographic order.
 
Example input #1: ( ["acb", "abc", "bca"], "abc")
Example output #1: ["abc","acb","bca"]
 
Example input #2: ( ["acb", "abc", "bca"], "cba")
Example output #2: ["bca", "acb", "abc"]
 
Example input #3: (["aaa","aa",""], "a")
Example output #3: ["", "aa", "aaa"]
 
You may assume that the strings to be sorted consist only of characters from 
the specified lexicographical ordering. You may also assume that the characters
in the strings to sort consist only of lowercase a-z.
"""

def lexStringSort(stringArray, lexOrder):
	"""Sorts an array of strings based on an arbitrary lexicographic ordering.
	Arguments:
		stringArray: a list, contains a collections of strings to be sorted.
		lexOrder: a string, definining a lexicographic ordering to sort the array
						  of strings by.
	"""
	# Determine the maximume string length.
	maxStringLength = None
	for string in stringArray:
		if len(string) > maxStringLength:
			maxStringLength = len(string)

	if maxStringLength is None:
		# Could not determine a maximum string length so just return.
		return stringArray
	
	# Assign values to characters in lexOrder to define a basis for ordering.
	lexValues = {}
	for characterIndex in range(len(lexOrder)):
		lexValues[lexOrder[characterIndex]] = characterIndex

	firstCharValue = lexValues[lexOrder[0]] - 1
	numBuckets     = len(lexOrder) + 1 # Plus 1 to account for empty char "".
	buckets        = [list() for i in range(0, numBuckets)]

	# Start by sorting the string array by length of each string.
	stringArray.sort(key=len)
	
	# Iterate over strings and assemble buckets with 
	for stringIndex in reversed(range(0, maxStringLength)):
	  for string in stringArray:
	    bucketIndex = 0
	    if stringIndex < len(string):
				bucketIndex = lexValues[string[stringIndex]] - firstCharValue
	    buckets[bucketIndex].append(string)
	  del stringArray[:]
	  
	  # Reorder the the string array using the content of the buckets.
	  for bucket in buckets:
	    stringArray.extend(bucket)
	    del bucket[:]
	
	return stringArray

# Runtime - This algorithm utilize the radix sort sorting algorithm and thus
# running time of lexStringSort() depends on the length of the strings provided 
# within the stringArray argument. Since this implementation will sort starting
# from the least significant character and then proceed to the most significant
# character for each string, the run time is said to be O(nk), where n is
# representative of the number of strings in stringArray and k is the average
# length of those string.