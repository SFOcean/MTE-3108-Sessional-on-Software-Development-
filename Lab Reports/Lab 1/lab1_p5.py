#Opening & Reading file
fh = open("mbox.txt")
count = 0
#Reading through line by line
for line in fh:
    x=line.rstrip().split()
    #Searching lines with 'From" and not 'From:"
    if 'From' in x:
        #Printing the email addresses
        print(x[1])
        count+=1
    else:
        continue
#printing total count
print("There were " + str(count) + " lines in the file with From as the first word")
