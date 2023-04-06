f = open("output.txt","r", encoding="utf-8")
val = f.read()
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

strval = text_from_bits(str(val))

print(strval)

print(len(val))