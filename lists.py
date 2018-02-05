my_list = [1,2,3,4,5,-6,7,-8,9]
my_list = list([1,2,3])

my_list = list()

my_list.append(7)
my_list.append(7)

print(my_list)

#print one element
print my_list[1]

#length of list
print len(my_list)

b = [8]

#combine arrays
print my_list + b

c = my_list + b
#add a value to the end of the array
print c
c.append(3)
print c

c.insert(1,1000)
print c

#slicing again
print c[1:]
print c[1:3]
print c[-1]
print c[:-1]

#sort lists
c.sort()
print c

# removes value from the end of a list, and returns it
# removes end as default but can input a value to remove
last_element = c.pop()
print last_element
last_element1 = c.pop()
print last_element1
last_element2 = c.pop()
print last_element2

print c

print "last_element: ", last_element, " rest:", c

# boolean indicators
print 7 in c
print 12 in c

#ranges
g = range(0,40)
print(g)

print ""

g = range(0,20,2)
print(g)

print ""

g = range(100,20,-5)
print(g)

f = ["bread "," elephants "," duckie"]

#join words in a last into one element
print "&".join(f)
