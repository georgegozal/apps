# Exercise 1:
mlist = ['bcde','abcde','jum','bcde','jum','jum','bcde','abcde']

def change(*args):
    d = {}
    for item in args[0]:
        c=args[0].count(item)
        d[item]=c
    print(len(d))
    for item in d.values():
        print(item,end=" ")
            
#change(tuple(mlist))
# output: 
    # 3  
    # 3 2 3 
