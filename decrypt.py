from encrypt import encryptor

key = int(bin(3), base=0)
alpha = 'abcdefghijklmnopqrstuvwxyz'


def decryptor(message):
    decrypted_messsage = ''
    for char in message:
        if char.isalpha():
            index = alpha.index(char.lower())
            new_index = index - key
            decrypted_messsage += alpha[new_index]
        else:
            decrypted_messsage += char
    return decrypted_messsage


message = input(': ').upper()
encrypted_msg = encryptor(message)
print('Encrypted: %s' % encrypted_msg)
decrypted_msg = decryptor(encrypted_msg)
print('Decrypted: %s' % decrypted_msg)
