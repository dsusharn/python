def isAnagram (str):
    i = 0
    reverse = str[::-1]
    while (i < len(str)):
        if str[i] == reverse[i]:
            i = i + 1
        else: break
    if i == len(str):
        print "IS an anagram"
        return 1   
    else:
        print "NOT an anagram"
        return 0
 
a = input()

isAnagram(a)
