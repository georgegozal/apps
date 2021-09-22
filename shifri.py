
print("""ეს არის შიფრის პროგრამა, სიტყვაში თითოეული ასო 
სხვადასხვა ინტერვალით არის გადაწეული ანბანში""")
#user_input = input("\nშეიყვანეთ სასურველი სიტყვა რომელიც იქნება გამოყენებული შიფრის გასაღებად: ")

while True:
    import pyperclip as clp
    ka_alfa="აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ" *3
    user_input = [2,14,7,1,3,9,22,6,4,2,7,11,13]


    def codding(ka_alfa,user_input,answer):
        changed = ""

        user_text = input("დაწერეთ სასურველი ტექსტი დასაშიფრად:\n").strip().split()

        for item in user_text:

            if len(item)==1:
                if item in ka_alfa:
                    idx = ka_alfa[:33].index(item)
                    if answer in ("1","კოდირება"):
                        changed += ka_alfa[idx + user_input[0]]
                    else:
                        changed +=ka_alfa[idx - user_input[0]]    
                else:
                    changed += item    

            else:
                for x,y in zip(item,user_input[:len(item)]):
                    if x in ka_alfa[:33]:
                        idx = ka_alfa[:33].index(x)
                        if answer in ("1","კოდირება"):
                            changed += ka_alfa[idx + y]
                        else:
                            changed += ka_alfa[idx - y]    
                    else:
                        changed += x

            # for adding space between words
            changed += " "                
        clp.copy(str(changed))
        
        return changed 


    while True:
        answer = input('\n ამოირჩიე ხელსაწყო: \n1.კოდირება \n2.დეკოდირება\n')
        if answer in ("1","2","კოდირება","დეკოდირება"):
            break
    if answer in ("1","კოდირება"):
        print("\n1. არჩეულია კოდირება")
        print(codding(ka_alfa,user_input,answer))

    if answer in ("2","დეკოდირება"):
        print("\n2. ამორჩეულია დეკოდირება")
        print(codding(ka_alfa,user_input,answer))

    
