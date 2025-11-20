def palindrom(str):
    
    return str == str[::-1]

str = input("please enter your str:")
if palindrom(str):
    print(f"{str} is palindrom")
else:
    print(f"{str} is not palindrom")
    
    
