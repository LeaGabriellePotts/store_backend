from mock_data import catalog

def print_catalog_total():
    total = 0
    for prod in catalog:
        total = total + prod["price"]
        
    print (f"The total of the catalog is: {total} USD")

print_catalog_total()






def say_hello():
    print("Hello there!")

def print_the_sum(a,b):
    print(a+b)

def print_the_division(a,b):
    # if the denominator is zero, print an error "asdasdasd"
    # else divide and print the result
    if b == 0:
        print("Error: division by zero is not allowed")
    else:
        print(a/b)

def print_the_cheaper (num1,num2):
    #validate taht num1 and num2 are actual nums
    if type(num1) not in [int, float]:
        print("Error, num1 is not valid")
        return # return = do not continue on this function

    if num1 < num2:
        print(num1)
    elif num1 == num2:
        print("They are the same")
    else:
        print(num2)

def print_all_numbers():
    nums = [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    # create a for loop and print each number from the array
    for n in nums:
        print(n)

def print_the_sum():
    nums = [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    total = 0
    for n in nums:
        if n > 40:
            total = total + n

    print(total)


def print_count_lowers():
    nums = [47, 29, 50, 46, 40, 42, 63, 56, 38, 54, 52, 21]
    count = 0
    for n in nums:
        if n <= 50:
            count = count + 1

    print(count)
# how many numbers we have lower than or equal to 50

# say_hello()
# print_the_sum(21,21)    
# print_the_division (10,4)
# print_the_division(10, 0)

# print_the_cheaper(34,10) #10
# print_the_cheaper(3,100) #3

# print_all_numbers()

# print_the_sum()

# print_count_lowers()