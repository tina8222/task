def roman_to_int(c):
    roman = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000            
    }
    total = 0
    
    for i in range(len(c)):
        if i + 1 < len(c) and roman[c[i]] < roman[c[i+1]]:
            total -= roman[c[i]]
        else:
            total += roman[c[i]]
            
    return total

print(roman_to_int("XIV"))
print(roman_to_int("III"))

