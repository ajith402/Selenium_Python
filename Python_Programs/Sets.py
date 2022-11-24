
#### Set is Unordered and doesnot contain Duplicates #####
### To create an Empty Set use set() ###

numSet= {10,20,20,30,40,40,100}
print(numSet)

set1={20,'20',30,'30',"30"}
print(set1)

cities=set(('Hyderabad','Chennai','Mumbai','Hyderabad','Delhi','Delhi'))
print(cities)

print('Find Set length:',len(cities))

##### Syntax: var in Set  ####
print('Check Whether Element is present in the Set: ', 20 in numSet)
print('Check Whether Element is present in the Set: ', 'abc' in cities)


