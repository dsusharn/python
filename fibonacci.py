def fibonacci(nb):
    if nb < 0:
        print("Incorrect input")
    elif nb==1:
        return 0
    elif nb==2:
        return 1
    else:
        return fibonacci(nb-1)+fibonacci(nb-2)

a = input()

print (fibonacci(a))
    