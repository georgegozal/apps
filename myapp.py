"""
well, მინდა დავწერო პროგრამა ტექსტის დაშიფრვრის, 
რომელიც სიტყბაში ყველა ასოს სხვადასხვა რიცხვით გადაწევს ანბანში 

"""

ka_alfa = ['ა','ბ','გ','დ','ე','ვ','ზ','თ','ი','კ','ლ','მ','ნ','ო','პ','ჟ',
        'რ','ს','ტ','უ','ფ','ქ','ღ','ყ','შ','ჩ','ც','ძ','წ','ჭ','ხ','ჯ','ჰ']

num_lst = [2,14,7,1,3,9,22,6,4,2,7,11,13]

ka_alfa = "".join(ka_alfa)*2
#user_input = input("enter some text: ").split()  
user_input = "როგორ ხარ ლამაზო?".split()

changed = ""

for item in user_input:
    #for letter in item:
        #if letter in ka_alfa[:33]:
        #    idx = ka_alfa[:33].index(letter)

    #    else:
    #        changed += letter    
    for x,y in zip(item,num_lst[:len(item)]):
        #print(x,y)
        if x in ka_alfa[:33]:
            idx = ka_alfa[:33].index(x)
            print(idx)
            changed += ka_alfa[idx + y]
            #pass
        else:
            changed += x    


print(changed)
#print(user_input)
#print(ka_alfa)