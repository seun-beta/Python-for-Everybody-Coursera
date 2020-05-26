# Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.
email_list = list()
email_dict = dict()
file_name = input('Please input the file name: ')
try :
    file_handle = open (file_name)
except :
    file_handle = open('mbox-short.txt')
    
for line1 in file_handle :
    if not line1.startswith('From')  :
        continue
    list_word = line1.split()
    if len(list_word) < 2 :
        continue 
    email_list.append(list_word[1])
for line2 in email_list : 
    email_dict[line2] = email_dict.get(line2,0) + 1
print (email_dict)
