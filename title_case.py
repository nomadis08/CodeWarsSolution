def title_case(title, minor_words):
    result=[]
    title=title.lower()
    title=title.split()
    minor_words=minor_words.lower()
    minor_words=minor_words.split()
    count=0
    for i in title:
        if i in minor_words and count>0:
            result.append(i)
            continue
        count+=1
        result.append(i.capitalize())
    return ' '.join(result)

tmp='the quick brown fox'
tmp2=''
print(title_case(tmp,tmp2))
