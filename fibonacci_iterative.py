def fibonacci_iterative(number):
    first = 0
    second = 1
    fibonacci = -1
    if number <= 0:
         print("Incorrect input")
    elif number == 1:
        return first
    elif number == 2:
        return second
    for _ in range(number - 2):
        fibonacci = first + second
        first = second
        second = fibonacci
    return fibonacci

index = input("Enter the index of element of fibonacci row: \n") 

print("This element is")
print(fibonacci_iterative(index))