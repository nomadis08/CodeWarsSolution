def diamond(n):
    mid=n%2
    if not mid:
        return None
    result='*'*n+'\n'
    for i in range(1,n//2+1):
        tmp=' '*i+'*'*(n-i*2)+'\n'
        result=tmp+result+tmp
    return result
    
print(diamond(1))

