# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    #default
    print("Cannot open the file ",fname ,"please try again")
    quit()

count = 0
total = 0
#reading the file line by line
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    t=line.find("0")
    number= float(line[t:])
    count = count + 1
    total = total + number

average = total/count
print ("Average spam confidence:" + str(average))