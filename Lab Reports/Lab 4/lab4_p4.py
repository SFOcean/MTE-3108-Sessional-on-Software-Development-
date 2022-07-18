givenString = "brontosaurus"
#Creating histogram function
def histogram(s):
    #using dictionary to store the keys and values
    d = dict() 
    for c in s: 
        if c not in d: 
            d[c] = 1 
        else: 
            d[c] = d[c] + 1 
    return d
#Creating print_hist function
def print_hist(h): 
    key_list = sorted(h.keys()) 
    for key in key_list: 
        print(key, h.get(key))
#printing output 
print_hist(histogram(givenString)) 