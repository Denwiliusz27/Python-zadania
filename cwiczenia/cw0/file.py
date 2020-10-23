thislist = ["apple", "banana", "cherry"]
thislist.append([x.upper() for x in thislist])

flat_list = []

for i in thislist:
    if(isinstance(i, list)):
        for j in i:
            flat_list.append(j)
    else:
        flat_list.append(i)

print(flat_list)
