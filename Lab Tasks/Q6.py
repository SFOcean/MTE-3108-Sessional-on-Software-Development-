print ("Print a sequence of whitespace seperated words: ")
words = list(map(str, input().split()))
uniqueWords = []
for i in words:
    if i not in uniqueWords:
        uniqueWords.append(i)
uniqueWords.sort()
print(uniqueWords)