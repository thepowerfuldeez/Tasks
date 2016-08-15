import re
def find(b,a):
    for i in range(len(b)-1):
        if ord(b[i].lower()) > ord(b[i+1].lower()):
            return i+2
    return 0

a = input()
b = re.findall('\D',a)
print(find(b,a))