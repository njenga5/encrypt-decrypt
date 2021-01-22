

# Was experimenting with class methods
# class Test:
#     def __init__(self, name, password):
#         self.name = name
#         self.password = password

#     def login(self):
#         if self.name == 'JOHN' and self.password == 'JOHN':
#             print('correct password')

#     @classmethod
#     def get_pass(cls, name):
#         return cls(name, name)


# test = Test.get_pass('JOHN')
# test.login()

import string
mappings = {}
alpha = (string.ascii_letters + string.digits).replace('0', '')
# print(alpha)
# alpha = 'abcdefghijklmnopqrstuvwxyz123456789'
key = int('0b11', base=0)

for i in range(1, len(alpha)+1):
    mappings[i+key] = alpha[i-1]

# print(mappings)
reversed_mappings = dict([(value, key) for key, value in mappings.items()])

message = input(': ')


text = []
for char in message:
    text.append(str(reversed_mappings.get(char, char)))
encrypted_text = '-1'.join(text)
print(encrypted_text)

message = encrypted_text.split('-1')
decrypted_message = ''
for x in message:
    if x.isdigit():
        decrypted_message += mappings.get(int(x), x)
    else:
        decrypted_message += x

print(decrypted_message)
