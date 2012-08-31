
import profile

def isAnagram(str1, str2):
    if (len(str1) != len(str2)) or (len(str1) == 0):
        return False

    zeroList = [0 for x in range(256)]
    charCountList = [0 for x in range(256)]

    # for each char in either of str1 or str2
    #
    #      o occurrence in str1 counts as +1 
    #      o occurrence in str2 counts as -1
    #      o charCountList is a running count of each char
    #
    # if at the end of processing charCountList is all zero's,
    # then the two strings are anagrams of each other.
    
    for ch1, ch2 in zip(str1, str2):
       charCountList[ord(ch1)] += 1
       charCountList[ord(ch2)] -= 1

    return charCountList == zeroList

#--------- main  -------------
# s1, s2 = '', 'item'
# s1, s2 = 'time', ''
# s1, s2 = 'time', 'itemizer'
# s1, s2 = 'time', 'item'
    
s1, s2 = 'timetabla', 'tableitem'
profile.run('isAnagram(s1, s2)')

if isAnagram(s1, s2):
   print '=== ANAGRAMS: (', s1, ', ', s2, ') '
else:
   print '=== NOT anagrams: (', s1, ', ', s2, ') '

