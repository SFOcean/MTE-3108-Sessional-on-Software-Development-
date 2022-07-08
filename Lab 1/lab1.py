#List to dictionary
src = [ 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 7, 9 ]
result_dict = dict( [ (i, src.count(i)) for i in set(src) ] )

for key, value in result_dict.items():
    print(key, ' : ', value)

#String to list to dictionary