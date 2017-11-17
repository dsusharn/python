def _is_anagram(str):
    counter = 0
    while (counter < len(str) / 2):
        if str[counter] == str[len(str) - counter - 1]:
            checker = True
        else:
            checker = False
            break
        counter += 1
    if checker == True:
        print('IS an anagram')
    else: 
        print('is NOT an anagram')
    return checker

input_string = input("Type a string in '': \n")

_is_anagram(input_string)