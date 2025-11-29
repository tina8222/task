def bingo(list):
    bingo_numbers = [2, 9, 14, 7, 15]  
    it = iter(list)
    return "WIN" if all(num in it for num in bingo_numbers) else "LOSE"


print(bingo([2, 5, 9, 14, 7, 15]))  
print(bingo([2, 9, 7, 14, 15]))      
print(bingo([2, 9, 14, 7, 15]))    