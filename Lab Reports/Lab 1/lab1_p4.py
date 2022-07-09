#Opening & Reading File
fhand = open("romeo.txt")

#Creating a empti list
lst = []

#Going through line by line
for line in fhand:
    #striping any trailing character like space
    line = line.rstrip()
    line = line.split()
    for i in line:
        if i not in lst:
            lst.append(i)
#sorting in alphabetical order
lst.sort()

print ("Sorted words in alphabetical order:")
print(lst)