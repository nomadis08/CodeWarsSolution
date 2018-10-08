import timeit
from memory_profiler import profile
import random

@profile
def scramble(s1, s2):
    d1=dict()
    for i in s1:
        if not d1.get(i):
            d1[i]=1
        else:
            d1[i]=d1[i]+1
    for i in s2:
        if not d1.get(i):
            return False
        if d1[i]==0:
            return False
        d1[i]-=1
    return True

@profile
def scramble2(s1,s2):
    for i in s2:
        if s1.count(i)<s2.count(i):
            return False
    return True

print('i')
s1=''
for i in range(1000000):
    s1+=chr(random.randint(97,122))

s2=''
for i in range(1000000):
    s2+=chr(random.randint(97,122))

print('1')

start=timeit.default_timer()
print(scramble(s1, s2))
end=timeit.default_timer()
print(end-start)

print('2')
start=timeit.default_timer()
print(scramble2('wrkqodlw', 'world'))
end=timeit.default_timer()
print(end-start)
