def isAnagram (str):
    i = 0
    while (i < len(str) / 2):
        if str[i] == str[len(str) - 1]:
            print ('IS an anagram')
            return 1
        else:
            print ('is NOT an anagram')
            return 0
        i = i + 1
    
a = input()

isAnagram(a)
