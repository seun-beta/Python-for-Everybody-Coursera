email_list = list()
email_dict = dict()
file_name = input('Please input the file name: ')
try :
    file_handle = open(file_name)
except :
    print ('The file name',file_name, 'your input cannot be found ')
    quit()
for line1 in file_handle :
    if not line1.startswith('From') :
        continue
    new_list = line1.split()
    if len(new_list) < 2 :
        continue 
    email_list.append(new_list[1])
for line2 in email_list :
    email_dict[line2] = email_dict.get(line2,0) + 1

biggest_contributor = None 
largest_value = None 
for key,value in email_dict.items() :
    if largest_value is None :
        largest_value = value
    elif largest_value < value :
        largest_value = value 
        biggest_contributor = key
print (biggest_contributor,'is the biggest contributor with',largest_value,'contributions')