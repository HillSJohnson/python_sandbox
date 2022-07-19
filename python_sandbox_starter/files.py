# Python has functions for creating, reading, updating, and deleting files.

#Open a file
myFile = open('myfile.txt', 'w')

#Get info
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Openign Mode: ', myFile.mode)

#Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

#Append to file
myFile = open('myfile.txt', 'a')
myFile.write('I also like php')
myFile.close()
