def double(arg):
    print('Before:', arg)
    arg = arg * 2
    print('After: ', arg)

def change(arg):
    print('Before:', arg)
    arg.append('more data')
    print('After: ', arg)
    
numbers = [42, 256, 16]

double(10)
double('hello ')
double(numbers)
print(numbers, 'after double')
change(['Give me'])
change(numbers)
print(numbers, 'after change')