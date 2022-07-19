# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
 
#Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes')) #(constructer)

#Single value needs trailing comma to be conisdered a tuple
fruits2 = ('Apples',)

#Cant change values
# fruits[0] = 'Pears'

print(fruits)
# print(fruits2, type(fruits2))

# A Set is a collection which is unordered and unindexed. No duplicate members.
# Create a set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

#Add to set
fruits_set.add('Apples')

# fruits_set.remove('Grape')

#This empties the set but does not delete it
# fruits_set.clear()

#Gets rid of set all together and is as if it is undefined
# del fruits_set

print(fruits_set)