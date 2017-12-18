print ("Exercise 13: \n")




import re

file = open('emails.txt', 'r')
file = file.read()

emails = re.findall(r'([^ ]+[@][^ ]+[.][a-z]+)', file)
print(emails)
