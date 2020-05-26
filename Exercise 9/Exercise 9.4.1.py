# Write a program to read through a mail log, build a histogram 
# using a dictionary and print out the email address of the top contributor 

file_name = input ('Please input the file name: ')
file_handle = open(file_name)
new_list = list()
mail_sender = dict()
for line in file_handle :
    if not  line.startswith('From') :
        continue
    word = line.split()
    new_list.append(word[1])
for line2 in new_list :
    mail_sender[line2] = mail_sender.get(line2,0) + 1
biggest_contributor = None 
largest_count = None 
for key, value in mail_sender.items() :
    if largest_count is None : 
        largest_count = value
    elif value > largest_count  :
        largest_count = value 
        biggest_contributor = key
print ('The largest contributor is', biggest_contributor,'with a total of', largest_count,'contributions')

