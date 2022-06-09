
print("""\nეს არის შიფრის პროგრამა\n
ტექსტის დაშიფვრა მოხდება დასაშიფრი სიტყვის მიხედვით,
მომხარებლის მიერ შეყვანილი სასურველი სიტყვის შემადგენელი
ასო-ბგერების ანბანში მდებარეობის მიხედვით მოხდება სიტყვაში
თითოეული ასოს სხვადასხვა ინტერვალით გადაწევა 
""")


while True:
        user_input_text = input("შეიყვანეთ სასურველი სიტყვა შიფრის გასაღებად: ").strip() 
        if len(user_input_text) <3:
            print("გთხოვთ შეიყვანეთ შედარებით გრძელი სიტყვა")
        else:
            user_input_text *= 3
            break    


while True:
    #pip install pyperclip
    #pip3 install pyperclip
    import pyperclip as clp
    ka_alfa="აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ" *3
    

    user_input = []
    for letter in user_input_text:
        if letter in ka_alfa:
            idx = ka_alfa.index(letter)
            user_input.append(idx)
    #print(user_input)        

    def codding(ka_alfa,user_input,answer):
        changed = ""

        user_text = input("დაწერეთ სასურველი ტექსტი დასაშიფრად:\n\n").strip().split()

        for item in user_text:

            if len(item)==1:
                if item in ka_alfa:
                    idx = ka_alfa[33:].index(item)
                    if answer in ("1","კოდირება"):
                        changed += ka_alfa[idx + user_input[0]]
                    else:
                        changed +=ka_alfa[idx - user_input[0]]    
                else:
                    changed += item    

            else:
                for x,y in zip(item,user_input[:len(item)]):
                    if x in ka_alfa:
                        idx = ka_alfa[33:].index(x)
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
    if answer in ("1","კოდირება","2","დეკოდირება"):
        if answer in ("1","კოდირება"):
            print("1. არჩეულია კოდირება")
        else:
            print("2. არჩეულია დეკოდირება")

        print("\n",codding(ka_alfa,user_input,answer))
        print("\n> ტექსტი მოკოპირებულია")

    exit = input("\nგსურთ კიდევ ცდა? (კი,არა,yes,no)")
    if exit not in ("კი","yes","Yes","YES"):
        break
