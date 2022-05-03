# * 찍기
print('\n--------------------------------------')

for x in range(1, 6) :
    for y in range(1, 6) : 
        print('*', end='')
    print('')

# * 찍기2
print('\n--------------------------------------')

for x in range(1, 6) :
    for y in range(x, 5) : 
        print(' ', end='')

    for y in range(1, x) :
        print('*', end='')
    print('')

## python star print 참고


# end
print('\n--------------------------------------')

print('Hello', end=' ')
print('World')




