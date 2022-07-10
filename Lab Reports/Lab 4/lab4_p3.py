#Immporting module for dictionary operation
from collections import OrderedDict

#Function to sort out and print print letters in decreasing order of frequency
def most_frequent(string):
    d = dict()
    dct = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    #Reversing dictionary map
    dct = {v:k for k,v in d.items()}
    res = OrderedDict(reversed(list(dct.items())))
    #sorting by decreasing frequency
    for i in sorted(res.keys()):
        print(res[i], end=" ")
    return None

newString = input ("Enter a String: ")
print ("The letters in decreasing order of frequency: ")
ans = most_frequent(newString)