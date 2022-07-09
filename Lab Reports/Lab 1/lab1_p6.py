#Opening the file
hand = open("mbox-short.txt")

#creating a list
lst = []

#Reading through line by line
for line in hand:
    if not line.startswith("From:"): continue
    line = line.split()
    lst.append(line[1])

#creating dictionary
counts = dict()
for word in lst:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
#Looping through the dectionary to find highest email sender
for word,count in counts.items(): 
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
#Printing the senders email address
print (bigword,bigcount)