"""
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, 
Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. 
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter 
some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be 
replaced by A, E would become B, and so on. The method is named after Julius Caesar, 
who used it in his private correspondence.[1]
"""
#url:  https://en.wikipedia.org/wiki/Caesar_cipher

while True:

    import string
    alfa1 = string.ascii_lowercase
    alfa1+=alfa1

    answer=input('This is Caesar shift.\n\nChoose a tool: \n1. Decode\n2. Encode \nanswer: ')

    def letter_dec(a):
	    changed=""
	    # user letter
	    my_text = input("input your text: ")
	    for let in my_text:
		    if let in a:
			    idx=a.index(let)
			    changed+= a[idx+3]
		    else:
			    changed+=let	
	    return changed

    alfa2 = string.ascii_lowercase
    alfa2+=alfa2

    def letter_enc(a):
	    changed=""
	    # user letter
	    my_text = input("input your text: ")
	    for let in my_text:
		    if let in a[25:]:
			    idx=a[26:].index(let)
			    changed+= a[idx-3]
		    else:
			    changed+=let	
	    return changed

    if answer == "1":
        print(letter_dec(alfa1))
    elif answer == "2":
        print(letter_enc(alfa2))

    answer2 =input('Do you need other try? (Y,N)').lower()
    if answer2 =='n':
        break        



