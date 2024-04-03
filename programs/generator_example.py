def count_to_n(n):
    value = 0

    while value < n:
        yield value
        value += 1




for num in count_to_n(10):
    print(num)