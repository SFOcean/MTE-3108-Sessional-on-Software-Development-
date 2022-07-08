#Task 1: Finding in string
string = input("Inpur a string")                    # taking input string

print ("Alphanumeric Characters :" + str(any(c.isalnum() for c in string)))  # finding aplhanumeric in string
print ("Alphabetical Characters :" + str(any(c.isalpha() for c in string)))  #and then type casting it into string
print ("Digits :" + str(any(c.isdigit() for c in string)))                   # To concatinate with a string
print ("Lowercase Characters :" + str(any(c.islower() for c in string)))
print ("Uppercase Characters :" + str(any(c.isupper() for c in string)))
