
def get_int_number():
    try:
        num = int(input("Enter a number : "))
        print(f"You entered {num}")
        
    except ValueError:
        print("Please enter a number")


get_int_number()
