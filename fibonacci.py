def fibonacci(number):
    if number <= 0:
        print("Incorrect input")
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number - 2)

index = input("Enter the index of element of fibonacci row: \n") 

print("This element is")
print(fibonacci(index))