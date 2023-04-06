f = open("ex.txt","r",encoding="utf-8")
val = f.read()

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

bitval = text_to_bits(str(val))

with open("binaryfile.txt","w",encoding="utf-8") as f:
    f.write(str(bitval))
