# -*- coding: utf-8 -*-
"""
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, 
Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. 
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter 
some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be 
replaced by A, E would become B, and so on. The method is named after Julius Caesar, 
who used it in his private correspondence.
"""
#url:  https://en.wikipedia.org/wiki/Caesar_cipher


print('\nThis is Caesar shift.\n')
try:
    interval=int(input("შეიყვანეთ სასურველი ინტერვალი(ნაგულისხმევი არის 3): \nInput desired interval(default is 3):\n>>> "))
except:
    interval=3


while True:

    import pyperclip as clp
    import string
    # abcdefghijklmnopqrstuvwxyz
    en_alfa = string.ascii_lowercase 
    en_alfa *= 3 
    # 3 x alfabet 
    ka_alfa="აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
    ka_alfa *= 3


    answer=input('\nChoose a tool: \n1. Decode\n2. Encode \nanswer: ')

    def enjob(en,text,x, ntl):
        changed=""
        for let in text:
            if let in en[26:]:
                idx=en[26:].index(let)
                if x=="plus":
                    changed+= en[idx+ntl]
                elif x=="minus":
                    changed+= en[idx-ntl]    
            else:
                changed+=let

        return changed

    def kajob(ka,text,x,ntl):
        changed=""
        for let in text:
            if let in ka[33:]:
                idx=ka[33:].index(let)
                if x=="plus":
                    changed+= ka[idx+ntl]
                elif x=="minus":
                    changed+=ka[idx-ntl]    
            else:
                changed+=let

        return changed

    def letter_dec(en,ka):
        changed=""
        # user letter
        my_text = input("შეიყვანეთ სასურველი ტექსტი, input text: \n")
        for let in my_text:
            if let in en:
                changed += enjob(en,my_text,"plus",interval)
                break
            elif let in ka:
                changed += kajob(ka,my_text,"plus",interval)    
                break
        clp.copy(str(changed))    
        return changed


    def letter_enc(en,ka):
        changed=""
        # user letter
        my_text = input("შეიყვანეთ სასურველი ტექსტი, input text: \n")
        for let in my_text:
            if let in en:
                changed += enjob(en,my_text,"minus",interval)
                break
            elif let in ka:
                changed += kajob(ka,my_text,"minus",interval)    
                break
        clp.copy(str(changed)) 
        return changed


    r='\nშედეგი-Result: \n'
    t='\n\nტექსი მოკოპირებულია\ntext is copied in clipboard\n'

    if answer == "1":
        print(r, letter_dec(en_alfa,ka_alfa), t)
    elif answer == "2":
        print(r, letter_enc(en_alfa,ka_alfa), t)

    answer2 =input('Do you need other try? (Y,N)').lower()
    if answer2 =='n':
        break        



