#Inputs

characters = ['x','y','z']
stringArray = "xyyayyayz"


# flags


subStrings = []
subString = []


def findMinSubsequence(characters,stringArray):
    minLength = len(characters)
    maxLength = len(stringArray)
    xfound = yfound = zfound = 0
    minSubsequence = []

    for k in range(minLength,maxLength+1):
        for j in range(0,maxLength-k+1):
            minSubsequence.clear() 
            for i in range(j,k+j):
                minSubsequence.append(stringArray[i])
                if stringArray[i] == 'x':
                    xfound = 1
                if stringArray[i] == 'y':
                    yfound = 1
                if stringArray[i] == 'z':
                    zfound = 1
            
                if xfound == 1 and yfound == 1 and zfound == 1:
                    return minSubsequence
            xfound = yfound = zfound = 0

result = findMinSubsequence(characters,stringArray)

print(result)