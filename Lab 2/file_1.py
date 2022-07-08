file1 = open("mbox.txt", "r")

for line in file1:
    if 'is' in line:
        print (line)