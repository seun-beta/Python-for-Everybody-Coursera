#This program records the domain name (instead of the
#address) where the message was sent from instead of who the mail came
#from (i.e., the whole email address). At the end of the program, print
#out the dictionary with the domain names in histogram format

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
    domain_list = new_list[1].split('@')

    email_list.append(domain_list[1])
for line2 in email_list :
    email_dict[line2] = email_dict.get(line2,0) + 1
print (email_dict)