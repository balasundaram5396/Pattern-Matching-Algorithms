import time
#BOYERMOORE ALGORITHM
def badCharHeuristic(string, size):
    badChar = [-1]*256
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar

def BoyerMoore(text, pattern):
    count = 0
    m = len(pattern)
    n = len(text)
    badChar = badCharHeuristic(pattern, m)
    s = 0
    while(s <= n-m):
        j = m-1
        while j >= 0 and pattern[j] == text[s+j]:
            j -= 1
            count = count+1
        if j < 0:
            print("Pattern found at index: {}".format(s))
            s += (m-badChar[ord(text[s+m])] if s+m < n else 1)
        else:
            s += max(1, j-badChar[ord(text[s+j])])
    print("Total number of comparisons in Boyer Moore Algorithm: "+str(count))

#HORSPOOL ALGORITHM
def shift_table(text, pattern):
    m = len(pattern)
    n = len(text)
    dict = {}
    for i in range(n):
        dict[text[i]] = m
    for j in range(m - 1):
        dict[pattern[j]] = m - 1 - j
    return dict

def Horspool(text, pattern):
    #Shift table
    table1 = shift_table(text, pattern)
    n = len(text)
    m = len(pattern)
    count = 0
    i = m - 1
    while i <= n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k = k + 1
            count += 1
        if k == m:
            i = i + k if i<n else 1
            break
        else:
            i = i + table1[text[i]]
            count += 1
    print('Total number of comparisons in Horspool Algorithm: '+str(count))
    return False

#NAIVE ALGORITHM
def Naive(text, pattern): 
    m = len(pattern) 
    n = len(text) 
    count = 0
    i=0
    for i in range(n - m+1): 
        j = 0
        while(j < m): 
            if (text[i + j] != pattern[j]): 
                count = count + 1
                break
            j += 1
            count = count+1
        if (j == m):
            print("Total number of comparisons in Brute Force Algorithm: "+str(count))
            return count

#MAIN FUNCTION
'''----------------------------------------------EXAMPLE 1--------------------------------------------------------'''
print("CASE 1")
text1 = "pandaiswhiteandblack"
pattern1 = "black"
print("Text: "+text1)
print("Pattern: "+pattern1)
start1 = time.time()
BoyerMoore(text1,pattern1)
Horspool(text1,pattern1)
Naive(text1,pattern1)
end1 = time.time()
timetotal1 = end1 - start1
print('Total time taken: '+str(timetotal1)+' seconds')

'''----------------------------------------------EXAMPLE 2--------------------------------------------------------'''
print("CASE 2")
text2 = "bagbrandiswildcraft"
pattern2 = "wild"
print("Text: "+text2)
print("Pattern: "+pattern2)
start2 = time.time()
BoyerMoore(text2,pattern2)
Horspool(text2,pattern2)
Naive(text2,pattern2)
end2 = time.time()
timetotal2 = end2 - start2
print('Total time taken: '+str(timetotal2)+' seconds')

'''----------------------------------------------EXAMPLE 3--------------------------------------------------------'''
print("CASE 3")
text3 = "santahasabeard"
pattern3 = "beard"
print("Text: "+text3)
print("Pattern: "+pattern3)
start3 = time.time()
BoyerMoore(text3,pattern3)
Horspool(text3,pattern3)
Naive(text3,pattern3)
end3 = time.time()
timetotal3 = end3 - start3
print('Total time taken: '+str(timetotal3)+' seconds')

'''----------------------------------------------EXAMPLE 4--------------------------------------------------------'''
print("CASE 4")
text4 = "doormirrorismainstays"
pattern4 = "main"
print("Text: "+text4)
print("Pattern: "+pattern4)
start4 = time.time()
BoyerMoore(text4,pattern4)
Horspool(text4,pattern4)
Naive(text4,pattern4)
end4 = time.time()
timetotal4 = end4 - start4
print('Total time taken: '+str(timetotal4)+' seconds')

'''----------------------------------------------EXAMPLE 5--------------------------------------------------------'''
print("CASE 5")
text5 = "new_juice_is_not_good"
pattern5 = "juice"
print("Text: "+text5)
print("Pattern: "+pattern5)
start5 = time.time()
BoyerMoore(text5,pattern5)
Horspool(text5,pattern5)
Naive(text5,pattern5)
end5 = time.time()
timetotal5 = end5 - start5
print('Total time taken: '+str(timetotal5)+' seconds')

'''----------------------------------------------EXAMPLE 6--------------------------------------------------------'''
print("CASE 6")
text6 = "christmas_is_near"
pattern6 = "near"
print("Text: "+text6)
print("Pattern: "+pattern6)
start6 = time.time()
BoyerMoore(text6,pattern6)
Horspool(text6,pattern6)
Naive(text6,pattern6)
end6 = time.time()
timetotal6 = end6 - start6
print('Total time taken: '+str(timetotal6)+' seconds')

'''----------------------------------------------EXAMPLE 7--------------------------------------------------------'''
print("CASE 7")
text7 = "new_laptop_is_awesome"
pattern7 = "awesome"
print("Text: "+text7)
print("Pattern: "+pattern7)
start7 = time.time()
BoyerMoore(text7,pattern7)
Horspool(text7,pattern7)
Naive(text7,pattern7)
end7 = time.time()
timetotal7 = end7 - start7
print('Total time taken: '+str(timetotal7)+' seconds')

'''----------------------------------------------EXAMPLE 8--------------------------------------------------------'''
print("CASE 8")
text8 = "cabababcd"
pattern8 = "ababc"
print("Text: "+text8)
print("Pattern: "+pattern8)
start8 = time.time()
BoyerMoore(text8,pattern8)
Horspool(text8,pattern8)
Naive(text8,pattern8)
end8 = time.time()
timetotal8 = end8 - start8
print('Total time taken: '+str(timetotal8)+' seconds')

'''----------------------------------------------EXAMPLE 9--------------------------------------------------------'''
print("CASE 9")
text9 = "fan_is_unstable"
pattern9 = "stable"
print("Text: "+text9)
print("Pattern: "+pattern9)
start9 = time.time()
BoyerMoore(text9,pattern9)
Horspool(text9,pattern9)
Naive(text9,pattern9)
end9 = time.time()
timetotal9 = end9 - start9
print('Total time taken: '+str(timetotal9)+' seconds')

'''----------------------------------------------EXAMPLE 10--------------------------------------------------------'''
print("CASE 10")
text10 = "nivedita"
pattern10 = "ved"
print("Text: "+text10)
print("Pattern: "+pattern10)
start10 = time.time()
BoyerMoore(text10,pattern10)
Horspool(text10,pattern10)
Naive(text10,pattern10)
end10 = time.time()
timetotal10 = end10 - start10
print('Total time taken: '+str(timetotal10)+' seconds')