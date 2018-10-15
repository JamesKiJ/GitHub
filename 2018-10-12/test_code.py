import chardet

def code_type(items,type):
    items_str =str(items)
    type_str = str(type)
    data = items_str.encode(type_str)
    type = chardet.detect(data)
    print(type)


print("Please enter your text...")
c = input()
print("Please enter you can test...")
b = input()
code_type(c,b)