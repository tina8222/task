# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack
# , or -1 if needle is not part of haystack

def strstr(haystack,needle):
    if needle =="":
        return 0
    m = len(haystack)
    n = len(needle)
    
    for i in range(m - n + 1):
        if haystack[i:i + n] == needle:
            return i
        
    return -1

print(strstr("butsad","sad")) #return 3
print(strstr("hello","mew")) #return -1
print(strstr("mewmew","")) #return 0








