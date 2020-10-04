'''2ndmaxValue.py -- To find the second max value in a list of numbers'''
alist = [2, 3, 4, 8, 1, 5, 7, 9, 20, 31, 28, 53, 22, 64]
max = 1
secmax = 0
for i in range(0, len(alist)):
    if alist[i] > max:
        secmax = max
        max = alist[i]
    else:
        pass


print(f'Second max value is {secmax}')
