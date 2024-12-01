#say_hi
from queue import PriorityQueue #import PriorityQueue

nicknames = PriorityQueue()

for i in range (0, 4):
    classmates = input('Enter the nicknames of ' + str(i + 1) + ' : ')
    nicknames.put(classmates)

while not nicknames.empty():
    greet = input('Press H to say Hi each of them.\n')
    if 'H' == greet.upper():
        next_item = nicknames.get()
        print( "Hi " + next_item)
print('Done saying Hi')
