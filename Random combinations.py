# random combinations
import random
inp=str(input("What are your options? "))
choices=[]
result=[]
while inp != "done":
    choices.append(inp)
    inp=str(input("What are your other options,when you are done type 'done'? "))
"""for i in choices:
    print(i, end=', ')
print(len(choices))"""
if len(choices)>2:
    decider=int(input("How many do you need chosen out of the choices you've given? "))
    for i in range (0,decider):
        a=random.randint(0,len(choices)-1)
        result.append(choices[a])
        choices.pop(a)
else:
    if len(choices)==0:
        print("Complete")
    else:
        print(choices[random.randint(0,len(choices))])
print(result)
