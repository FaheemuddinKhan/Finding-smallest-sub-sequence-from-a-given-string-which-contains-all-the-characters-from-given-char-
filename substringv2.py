def findMinSubsequence(characters,stringArray):
    """Function to find the smallest possible substring in stringArray that contains all the characters
    from characters list"""
    minLength = len(characters)     #The minimum possible subsequence is the no. of charatcers in characters list, which will be best case.
    maxLength = len(stringArray)    #The max possible subsequence is the no. of characters in stringArray, which will be worst case scenario.

    minSubsequence = []

    flags = {}                      #This is a dictionary to keep track of the characters found in the subsequence.
    for i in characters:            #Here we are setting all the characters' flags to zero, since no character is yet found.
        flags[i] = 0
    

    for k in range(minLength,maxLength+1):   #k here represents the current length of subsequence being processed.           
        for j in range(0,maxLength-k+1):     #j here reprsents the current start index of subsequence with k characters.     
            minSubsequence.clear() 
            for i in range(j,k+j):           #i iterates over each character in a subsequence with k characters with start index j.
                minSubsequence.append(stringArray[i])
                if stringArray[i] in flags.keys():
                    flags[stringArray[i]] = 1
                if 0 not in flags.values():
                    return minSubsequence
            flags.clear()
            for i in characters:
                flags[i] = 0

#Inputs: Change the values in order to test in different scenario.
characters = ['a','b','d','e','f']   #characters to be matched
stringArray = "adklmnjtwblldllellf"  #input string to be evaluated

result = ""
r = findMinSubsequence(characters,stringArray)
result = result.join(r)                             #To get the result in string format.

if result != None:
    print("The smallest sequence containing all the characters is " + result)
