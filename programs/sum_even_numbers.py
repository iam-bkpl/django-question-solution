# list initialization
mynums = []

user_input = input("Enter numbers and -1 when done : ")

while user_input != "-1":
    try:
        mynums.append(int(user_input))
    except ValueError:
        print("Please enter int number")
    
    user_input = input()

print("My list is :")
print(mynums)


# function that takes a list and check if it's even and sum all the even number in the list and returns the result
def calc_sum(myList:list):
    sum = 0
    for i in myList:
        if i % 2 == 0:
            sum +=i

    return sum


result = calc_sum(mynums)
print(f"The sum of all even numbers in the list is {result}")