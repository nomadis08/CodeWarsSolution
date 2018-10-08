def solution(s):
    result=[]
    if len(s)%2:
        s+='_'
    return([s[i:i+2] for i in range(0,len(s),2)])  

tmp='abcde'
print(solution(tmp))
