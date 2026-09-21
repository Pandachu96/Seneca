# num = int(input('Enter number: '))

# if num > 20:
#     print('Greater than 20')

# else:
#     print('Less than or equal to 20')

# finding the max number in a list
ls = [1,321,414,21]
max = ls[0]
for v in ls:
    if v > max:
        max = v
print(max)