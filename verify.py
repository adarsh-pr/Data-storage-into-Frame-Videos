f = open("binaryfile.txt","r", encoding="utf-8")
val = f.read()
print("LEN",len(val))
k = open("ex.txt","r",encoding = "utf-8")
dat = k.read()


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

strval = text_from_bits(str(val))

def verify(binvalues,strvalues):
    if binvalues == strvalues:
        print("Verified")
    else:
        print("Both aren't same")

verify(strval,dat)