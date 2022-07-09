#Opening & Reading file
fh = open("mbox.txt")
count = 0
#Reading through line by line
for lines in fh:
    line=lines.rstrip()
    #Searching lines starting with "From" and not "From:"
    if line.find("From") == -1 or line.find("From:") != -1:
        continue
    #Parsing the lines that start with 'From' with split()
    x = line.split()
    #Printing the email address
    print(x[1])
    count+=1
#Printing the count result
print("There were " + str(count) + " lines in the file with From as the first word")