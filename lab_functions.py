def print_triangle(number: int):
    for row in range(number, 0, -1):
        for new_number in range(row, 0, -1):
            print(new_number, end=" ")
        print()

user_number = int(input("Enter a number: "))
print_triangle(user_number)