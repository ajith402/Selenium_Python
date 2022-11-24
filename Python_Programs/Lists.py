
a=[10,20,30,10]
b=[1,2.45,'abc',200]
print(a)
print(b)
print(b[0])
print(b[1:])


Cars=['Maruthi Suzuki','Kia','Hyundai']
print(Cars)

print('Append')
Cars.append('Tata Motors')
print(Cars)

##### Insert ####
print('Insert')
Cars.insert(2,"Volvo")
print(Cars)

##### Carsount ####
print('Count', Cars.count('Volvo'))


##### Sort ###
print('Sort')
Cars.sort()
print(Cars)

print('Reverse')
Cars.reverse()
print(Cars)

##### Remove #### Removes the First Occurance of the value in the list ####
print('Remove')
Cars.remove('Hyundai')
print(Cars)


##### Pop ####
print('Pop')
Cars.pop()
print(Cars)

#### Remove at any index ####
print("Remove at an Index")
Cars.pop(1)
print(Cars)

##### Carsopy ####
print('Copy')
e=Cars.copy()
print(e)
e.append(3)
print(e)

print('Clear')
Cars.clear()
print(Cars)

