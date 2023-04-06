'''with open("output.txt","r") as f:
    o=f.read()
with open("binaryfile.txt","r") as f:
    b=f.read()
print(len(o),len(b))
ic=0
c=0
try:
    for i in range(len(b)):
        if o[i] == b[i]:
            c+=1
        else:
            print(i)
            ic+=1
            break
except:
    pass
print(ic,i)'''


with open("ex.txt","r",encoding="utf-8") as f:
    b=f.read()


f = open("output.txt","r", encoding="utf8")
val = f.read()

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

strval = text_from_bits(str(val))
c=0
ic=0
for i in range(len(b)):
    if b[i] == strval[i]:
        c+=1
    else:
        ic+=1

print(ic,c)

