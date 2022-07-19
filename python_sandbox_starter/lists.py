# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create a list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use a constructor
# numbers2 = list((1,2,3,4,5))

#Get a value
print( fruits[1])

#Get lenght
print(len(fruits))

#Append to list
fruits.append('Mangos')

fruits.remove('Grapes')

fruits.insert(2, 'Strawberries')

fruits.pop(2)
print(fruits)