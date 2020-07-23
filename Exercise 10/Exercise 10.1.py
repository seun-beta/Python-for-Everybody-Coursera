file_name = input ('Please input your file name: ')
email_file_handle = open(file_name)
email_list = list()
email_dict = dict()
for line1 in email_file_handle :
    if not line1.startswith('From') :
        continue 
    word_list = line1.split()
    if len(word_list) < 2 :
        continue
    email = word_list[1]
    email_list.append(email)
for i in email_list:
    email_dict[i] = email_dict.get(i,0) + 1
tuple_list = list()
for key,value in email_dict.items() :
    tuple_list.append((value,key))
tuple_list.sort(reverse = True)
print (tuple_list)
for line2, line3 in tuple_list[0] :
    print (line3,line2)




