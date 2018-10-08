def longest_consec(strarr, k):
    if len(strarr)==0 or k>len(strarr) or k<=0:
        return ""
    tmp=[len(i) for i in strarr]
    ind=0
    for i in range(1,len(strarr)-k+1):
        if sum(tmp[i:i+k])>sum(tmp[ind:ind+k]):
               ind=i
        print(tmp[i:i+k],tmp[ind:ind+k])
    return ''.join(strarr[ind:ind+k])
               
tmp=["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"]
tmp=["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"]
tmp=["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"]
print(longest_consec(tmp,3))
