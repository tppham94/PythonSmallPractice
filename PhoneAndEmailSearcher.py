#! python3
#Program to search through a text the email and phone number
import re

text =('''Child welfare
ASSISTANCE AUX FEMMES DE MONTRÉAL
Confidential Address
514 270-8291 Fax: 514 270-1176
Website: www.assistanceauxfemmes.ca
Email: information@assistanceauxfemmes.ca
Something@something.ca
''')
#print(text)
#Using regex to find the patterns of number and email
#Pattern such as xxx-xxxx (xxx) xxx-xxxx with extension number ext xxxxx
#Email pattern such as xxxxxx@xxxxxx.xxx including period and underscore if needed
#VERBOSE Allows to write line by line instead of only having 1 line

#Creating regex for phone number 
phoneNumberRegex = re.compile(r'''
(((\d\d\d)|(\(\d\d\d))? #optional to have area code, this also includes parenthesis
\s #space in between 
(\d\d\d-\d\d\d\d) #Number format with area code
(ext(\.)?\s (\d{2,6}))?) #Optional extension that has a period or not
''', re.VERBOSE)

#Creating regex for email address 
emailRegex = re.compile(r'''
[a-zA-Z0-9_.]+ #The first part of the email with combination of . and _ if needed
@              #For the symbol @
[a-zA-Z0-9_.]+ #Same as the first part of the email address  
''', re.VERBOSE)

#Getting the email address and phone number
getPhoneNumber = phoneNumberRegex.findall(text)
getEmail = emailRegex.findall(str(text))

#Getting the first value of the tuple which is the phone number 
phoneDirectory = []
for phoneNumbers in getPhoneNumber:
  phoneDirectory.append(phoneNumbers[0])

#Printing the value line by line 
print('\n'.join(phoneDirectory))
print('\n'.join(getEmail))
