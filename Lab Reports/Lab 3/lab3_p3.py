# function to check if point collinear or not
def collinear(x1, y1, x2, y2, x3, y3):
    #skipped multiplication with 0.5 to avoid floating point
	a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
	if (a == 0):
		print ("Collinear")
	else:
		print ("NOT Collinear")
#taking cordinates as string
x1y1 = input("Enter (x1, y1) = ")
x2y2 = input("Enter (x2, y2) = ")
x3y3 = input("Enter (x3, y3) = ")
#spliting and storing in a list
lstx1y1 = x1y1.split(",")
lstx2y2 = x2y2.split(",")
lstx3y3 = x3y3.split(",")
#stripping for type casting
x1 = lstx1y1[0].strip()
y1 = lstx1y1[1].strip()
x2 = lstx2y2[0].strip()
y2 = lstx2y2[1].strip()
x3 = lstx3y3[0].strip()
y3 = lstx3y3[1].strip()
#type casting for calculation
collinear(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3))