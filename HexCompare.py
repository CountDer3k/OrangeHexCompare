import binascii
filename = 'test.png'
with open(filename, 'rb') as f:
    content = f.read()
print(binascii.hexlify(content))