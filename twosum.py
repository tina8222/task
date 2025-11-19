numbers = [2,7,9,11,13]
target = 13
for i , num1 in enumerate(numbers):
    for j , num2 in enumerate(numbers[i+1:],start = i+1):
        if num1 + num2 == target:
            print([i,j])
            break
        