#Taking file name "word.txt"
fname = input("Enter file name: ")
try :
    #Opening & Reading file content
    fh = open(fname)
except:
    #default
    print('Cannot open the file ',fname ,'please try again')
    quit()

for line in fh :
    line = line.upper()
    line = line.rstrip()
    print(line)