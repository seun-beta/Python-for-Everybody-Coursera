# Write a program that categorizes each mail message by
#which day of the week the commit was done. To do this look for lines
#that start with “From”, then look for the third word and keep a running
#count of each of the days of the week. At the end of the program print
#out the contents of your dictionary (order does not matter).

day_list = list()
day_dictionary = dict()
file_name = input('Please input your file name: ')
try :
    file_handle = open(file_name)
except :
    print ('The file name you input cannot be found')
    quit()
for line in file_handle :
    if not line.startswith('From') :
        continue
    list_word = line.split()
    if len(list_word) < 3 :
        continue
    day_list.append(list_word[2])
for line2 in day_list :
    day_dictionary[line2] = day_dictionary.get(line2,0) + 1
print (day_dictionary)

