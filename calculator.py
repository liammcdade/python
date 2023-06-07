def calculator():
    num_of_numbers = int(input("Enter the number of numbers: "))
    numbers = []

    for i in range(num_of_numbers):
        number = float(input("Enter number {}: ".format(i+1)))
        numbers.append(number)

    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = sum(numbers)
    elif operation == '-':
        result = numbers[0] - sum(numbers[1:])
    elif operation == '*':
        result = 1
        for num in numbers:
            result *= num
    elif operation == '/':
        result = numbers[0]
        for num in numbers[1:]:
            if num != 0:
                result /= num
            else:
                print("Error: Division by zero!")
                return
    else:
        print("Invalid operation!")
        return

    print("Result: {}".format(result))


calculator()
