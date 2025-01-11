list1= [1,2,3,4,5,6,]

#append
list1.append(7)
print(list1)
#[1, 2, 3, 4, 5, 6, 7]

#extend
list1.extend([8,9,10])
print(list1)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


#insert
list1.insert(10,11)
print(list1)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

#remove
list1.remove(11)
print(list1)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#pop
list1.pop(3)
print(list1)
#[1, 2, 3, 5, 6, 7, 8, 9, 10]

#index
l=list1.index(5)
print(l)
#3 is the index of the number 5 from the list

#count
print(list1.count(7))
#1

#sorted()
l1=sorted(list1)
print(l1)
#[1, 2, 3, 5, 6, 7, 8, 9, 10]
print(sorted(list1,reverse=True))          #descending order
#[10, 9, 8, 7, 6, 5, 3, 2, 1]

#sort()
list1.sort(reverse=False)                  #ascending order
print(list1)
#[1, 2, 3, 5, 6, 7, 8, 9, 10]
list1.sort(reverse=True)
print(list1)
#[10, 9, 8, 7, 6, 5, 3, 2, 1]

#copy()
list2=list1.copy()
print(list2)
#[10, 9, 8, 7, 6, 5, 3, 2, 1]