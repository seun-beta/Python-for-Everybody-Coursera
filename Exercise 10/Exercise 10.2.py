file_name = input ('Please input file name: ')
file_handle = open(file_name)
hour_list = list()
hour_dict = dict()
for line1 in file_handle :
    if not line1.startswith('From') :
        continue 
    word_list = line1.split()
    if len(word_list) < 6 :
        continue 
    new_list = word_list[5].split(':')
    hour = new_list[0]
    hour_list.append(hour)
for line2 in hour_list : 
    hour_dict[line2] = hour_dict.get(line2,0) + 1
hour_tuple_list = list()
for key,value in sorted(hour_dict.items()) :
    print (key,value)

# hour_tuple_list.sort(reverse= True)
# for key,value in hour_tuple_list :
    # print (value,key)


