
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


# Lists *************************************

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[0])

print(thislist[2:5])

print(thislist[:5])

print(thislist[2:])


for x in thislist:
    print(x)

if 'apple' in thislist:
    print('Yes, Apple exists in this list')

print(len(thislist))

thislist.append('testing')

thislist.insert(3, 'another test')

print(len(thislist))
print(thislist)


thislist.remove('another test')

print(thislist)



thislist.pop(7)

print(thislist)


del thislist[0]

print(thislist)

thislist.clear()

print(thislist)

# del thislist

print(thislist)



thislist = ["apple", "banana", "cherry"]

newlist = thislist.copy()

print(newlist + newlist)


anotherlist = list(newlist)


print(anotherlist)

# Tuples *********************

# Unchangable

thistuple = ('apple', 'banana', 'cherry')

print(thistuple)


#Sets **************

thisset = {'apple', 'banana', 'mango'}

print(thisset)

# Once a set is created, you cannot change its items, but you can add new items.

thisset.add('test1')

print(thisset)

thisset.update(['test2', 'test3', 'test3'])

print(thisset)

thisset.remove('test1')

thisset.discard('test2')

print(thisset)

#join two sets

thisset2 = {'orange', 'grapes', 'pineapple'}


thisset3 = thisset.union(thisset2)

thisset3 = thisset.union(thisset2)

print(thisset3)



#Dictonaries *****************

thisdict = {
    'brand' : 'Royal Enfield',
    'model' : 'Himalayan',
    'year'  : 2017
}

print(thisdict['brand'])

for x in thisdict:
  print(x, thisdict[x]) 

for x in thisdict.values():
  print(x) 
