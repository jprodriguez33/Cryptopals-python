
hex_one = "1c0111001f010100061a024b53535009181c"
bytes_one = bytes.fromhex(hex_one)

hex_two = "686974207468652062756c6c277320657965"
bytes_two = bytes.fromhex(hex_two)

result = bytearray()

for b1, b2 in zip(bytes_one, bytes_two):
    result.append(b1 ^ b2)

xor = bytes(result)
print(xor.hex())