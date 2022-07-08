tpl = ""

num = input ("How many entries you want to make: ")
for x in range(int(num)):
    temp_str = input ()
    tpl = tpl + " " + temp_str


lst = [tuple(x.split(',')) for x in tpl.split()]

print(sorted(lst, key=lambda x: (x[0], x[1], x[2])))
