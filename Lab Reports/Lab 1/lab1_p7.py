#Opening and reading mbox.txt file
f=open('mbox.txt')
hours=dict()
#Looping through line by line
for line in f:
    if line.startswith('From '):
        c=line.split()
        n=len(c)
        time=c[n-2]
        hour=time.split(':')[0]
        hours[hour]=hours.get(hour,0)+1
#Listing the distribution
lst=list(hours.keys())
lst.sort()
#Creating a table for hourse and mail number
print('Hours'+'      -  Mail Numbers')
for key in lst:
    print(key,'              ',hours[key])