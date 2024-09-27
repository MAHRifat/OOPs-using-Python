numbers =[34,35,67,74,75,73,89,85]
odds=[]
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)

print(odds)

# for loop and odds_nums list was same output

odds_nums = [num for num in numbers if num % 2 == 1 if num % 5 == 0]

print(odds_nums)