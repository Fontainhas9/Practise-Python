def max_of_three(a,b,c):
    max_3=0
    if a>b:
        if a>c:
            max_3=a
        else: 
            max_3=c
    else:
        if b>c:
            max_3=b
        else:
            max_3=c
    return max_3



print(max_of_three(5,6,7))