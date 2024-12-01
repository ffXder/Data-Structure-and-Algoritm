#birth_month
group1 = set([])
group2 = set([])
self = set([])

#adds the first three birth months into set group1
for i in range(0, 3):
    birth_month = input('Enter a birth month ' + str(i + 1) + ' : ')
    group1.add(birth_month)

#adds the remaining birth months into set group2
for i in range(0, 3):
    birth_month = input('Enter a birth month ' + str(i + 1) + ' : ')
    group2.add(birth_month)

print('Group 1: ' + str(group1))
print('Group 2: ' + str(group2))

my_birthmonth = input('Enter your birth month: ')
self.add(my_birthmonth)

union = group1 | group2 #combines all the elements from different set
inter = group1 & group2 #finds the common elements from set group1 & group2
diff = group1 - group2 #finds the differenct elements from set group1 & group2

print("Union of Set Group 1 and Group 2: " + str(union))
print("Intersection of Set Group 1 and Group 2: "+ str(inter))
print("Difference of Set Group 1 and Group 2: " + str(diff))

if my_birthmonth in group1 or my_birthmonth in group1:
    print('You have the same birth month with one of your classmates.')
else:
    print("You don't have the same birth month with one of your classmates.")
