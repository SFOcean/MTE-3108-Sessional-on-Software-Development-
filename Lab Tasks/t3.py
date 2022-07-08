#function to test leap year
def is_leap(year):
    # Logic for finding leap year
    leap = False
    if year%4==0 and year%100!=0:
        leap =  True
    if year%400==0:
        leap = True
    
    return leap

year = int(input())  #type casting
print(is_leap(year)) # rpinting leap year