def palindrom(num):
    str_num = str(num)
    return str_num == str_num[::-1]

num = int(input("please enter your number:"))
if palindrom(num):
    print(f"{num} is palindrom")
else:
    print(f"{num} is not palindrom")

