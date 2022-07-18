#Function for finding unique characters
def printUnique(words):
    UniqueList = []
    for word in words:
        temList = []
        for i in word:
            if i not in temList:
                temList.append(i)
        UniqueList.append(temList)
    #Lopping through each string
    for i in range(len(words)):
        print(f'Unique characters in {words[i]}:')
        for letter in UniqueList[i]:
            print(letter)
        print()
#Calling Function
stringList = tuple(input("Enter Variable Number of Strings: ").split())
printUnique(stringList)