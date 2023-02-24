#numbers = [5, 2, 5, 2, 2]

#for num in numbers:
    #print ('*' * num)

numbers = [5, 2, 5, 2, 2]

for num in numbers:
    output = ''
    for numb in range(num):
        output = output + '*'
    print(output)