def isAlphabaticOrder(s):
 
    n = len(s)
 
    for i in range(1, n):
        print(s[i], s[i-1])
 
        # if element at index 'i' is less
        # than the element at index 'i-1'
        # then the string is not sorted
        if (s[i] < s[i - 1]) :
            return False
 
    return True

string = "abbb"
print(isAlphabaticOrder(string))