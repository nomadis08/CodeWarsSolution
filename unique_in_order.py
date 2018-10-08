from itertools import groupby 
def unique_in_order(iterable):
    return([k for k,i in groupby(iterable)])

tmp='AAAABBBBBBBBCCDDDDAA'
print(unique_in_order(tmp))
