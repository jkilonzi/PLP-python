my_list = []

#appending the values to the list
my_list.append(20)
my_list.append(30) 
my_list.append(40) 
my_list.append(10)

print(my_list)
#inserting the value 15 at the second index
my_list.insert(1,15)
print(my_list)

#extending the list
my_list.extend([60, 50, 70])
print(my_list)

#removing last element
my_list.remove(70)
print(my_list)

#sorting the list in ascending order
my_list.sort()
print(my_list)

#finding the index of 30
index_of_30 = my_list.index(30)

print("Index of 30:" ,index_of_30 )
