
x = "priyo@gmail.com"

index1 = x.find("@")
index2 = x.find(".")

st = slice(index1+1, index2)
print (x[st])
#temp1 = x.split(".")

#temp2 = temp1[0].split("@")

#temp3 = temp2 + [temp1[1]]

#print (temp3)

#temp4 = slice(1,2)

#print (temp3[temp4])