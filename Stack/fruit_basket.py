basket = [] #stack for storing the data

print("Catch and eat any of these fruits:('apple', 'orange', 'mango', 'guava')")
count_fruit = int(input("How many fruits would you like to catch? "))

print("Choose a fruit to catch. Press A, O, M, or G.")
for i in range(count_fruit):
    catch_fruit = input(f'Fruits {i + 1} of {count_fruit}: ')

    if catch_fruit.upper() == "A":
            basket.append('apple')
    elif catch_fruit.upper() == "O":
            basket.append('orange')
    elif catch_fruit.upper() == "M":
            basket.append('mango')
    elif catch_fruit.upper() == "G":
            basket.append('guava') 
    else:
        print('fruit cannot be catch in the basket!')    

print("Your basket now has: " + str(basket))

for i in range(count_fruit):
        eat_fruit = input("Press E to eat fruit. ")

        if eat_fruit.upper() == "E":
            basket.pop()

            if not basket:
                print('No more fruits')
            else:
                print("Eating " + basket[-1] + " nomnom! ")
                print("Fruit(s) in the basket: " + str(basket))