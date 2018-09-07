def square(start, end):
    '''result = [(number+1)**2 for number in range(start, end, 2)]
    print(result)'''
    result = []
    for num in range(start, end, 2):
        num = (num+1)**2
        result.append(num)
    print(result)


square(1,10)
