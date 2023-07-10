for i in range(1,100):
    print(i,end=' ')
    if i%10%3==0 or i//10%3==0:
        print("짝",end='')
    print()
        