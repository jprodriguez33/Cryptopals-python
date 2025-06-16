hex_one = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
bytes_one = bytes.fromhex(hex_one)


def single_byte_xor(ciphertext):

    for key in range(256):
        result = bytearray()

        for b1 in ciphertext:
            result.append(b1 ^ key)
        
        try:
            plaintext = result.decode("ascii")
            print(f"Key: {key} -> {plaintext}")

        except UnicodeDecodeError:
            pass

    return plaintext

single_byte_xor(bytes_one)