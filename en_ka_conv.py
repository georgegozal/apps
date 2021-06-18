"""
This code is for converting Georgian text writen with latin alphabet
"""

# -*- coding: utf-8 -*-
enlst=['a','b','g','d','e','v','z','T','i','k','l','m','n','o','p','J','r','s',
        't','u','f','q','R','y','S','C','c','Z','w','W','x','j','h']
kalst=['ა','ბ','გ','დ','ე','ვ','ზ','თ','ი','კ','ლ','მ','ნ','ო','პ','ჟ',
        'რ','ს','ტ','უ','ფ','ქ','ღ','ყ','შ','ჩ','ც','ძ','წ','ჭ','ხ','ჯ','ჰ']

url=input('Enter file url/name: ')


def converter(enlst,kalst,url):

    #import docx library for docx file read 
    import docx
    #read file
    file = docx.Document(url)
    text = ''
    for paragraph in file.paragraphs:
        #text_list.append(paragraph.text)
        for i in paragraph.text:
            text+=i

    #variable for converted text
    converted=''
    #iterate through the text and convert it
    for let in text:
        if let in enlst:
            idx=enlst.index(let)
            converted+=kalst[idx]
        else:
            converted+=let    
    
    return converted

converted_text=converter(enlst,kalst,url)
with open(f'{url[:-5]}-converted.docx', 'w') as f:
    f.write(converted_text)

