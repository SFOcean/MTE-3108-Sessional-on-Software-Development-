print ("All number which are divisble by 7 but are not multiple of 5 \nincluded range of 2000 to 3200: \n")
for i in range(2000, 3201):
    if (i%7 == 0 and i%5 != 0):
        print(i, end=", ")