def log_sum(func):
    def wrapper(*args, **kwargs):
        print(f"Starting sum...")
        print(f"Calling function : {func.__name__}")
        print(f"Arguments are : {args}")

        result = func(*args, **kwargs)

        print(f"The result of the function is : {result}")
        return result
    
    return wrapper

@log_sum
def sum(a,b):
    return a + b



result = sum(3,2)
print(f"Result : {result}")