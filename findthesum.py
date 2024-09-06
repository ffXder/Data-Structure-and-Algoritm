#Find the sum
def find_sum(num):
    if num == 0: #if the num is not equal to 0 the function will call itself until it reach 0
       return num 
    return num + find_sum(num - 1)
       

num = int(input("Enter a number: "))
print("The sum of first "+ str(num) + " integer is " + str(find_sum(num)))





        