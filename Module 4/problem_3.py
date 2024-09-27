# def add_numbers(*args):
#     result = 0
#     for num in args:
#         result += num
#     return result

# print(add_numbers(2, 5, 8))
# print(add_numbers(1, 3, 7, 11))

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="John", age=30, city="New York")

