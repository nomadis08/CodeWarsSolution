def expanded_form(num):
    count=0
    result=list()
    tmp=str(num)
    for i in tmp:
        if i!='0':
            result.append(str(int(i)*pow(10,len(tmp)-count-1)))
        count+=1
    return(' + '.join(result))

value=42
print(expanded_form(value))
