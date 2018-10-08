def narcissistic(value):
    len_num=len(str(value))
    rest=value
    result=0
    for i in range(len_num-1,-1,-1):
        mult=10**i
        num=rest//mult
        rest=rest-num*mult
        result+=num**(len_num)
    return result==value

print(narcissistic(153))
